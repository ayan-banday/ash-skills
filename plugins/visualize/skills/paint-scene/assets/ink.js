/* paint-scene ink.js: the Scene level. A picture assembled from the kit with about ten lines of settings.
   Ink.scene(canvasOrSelector, cfg) -> Promise<canvas>.  Ink.png(canvas, "name.png") saves it.
   Ink.svg("sit-write", "#111") -> an SVG string of one part (for Figma or an inline picture).  Ink.names() lists parts.
   Masks and tiles arrive in Ink.assets from `python scripts/kit.py bundle`. Menu and rules: references/character.md. */
(function(root){
"use strict";
var BALL="#F58E84";
var Ink={assets:{masks:{},tiles:{}},BALL:BALL,pending:[]};

/* ---------- parts: silhouettes in units where a standing figure is 200 tall, anchored at its feet (0,0), y up is negative.
   ops: c circle, e ellipse, r rect, p filled path, s stroked path [width,d], u another part [name,x,y,dir].
   A first letter L draws in the light colour, l in faint light, B in the ground colour. Figures face right; dir -1 flips. */
var P={
 /* ---- figures ---- */
 "stand":{k:"figure",b:[-36,-200,36,0],a:{hand:[30,-80],head:[0,-182]},o:[
  ["c",0,-182,17],["p","M-21,-160Q0,-169 21,-160L18,-88L-18,-88Z"],["s",14,"M-8,-92L-10,0M8,-92L11,0"],["s",10,"M-20,-152L-28,-110L-29,-82M20,-152L28,-110L29,-82"]]},
 "stand-raise":{k:"figure",b:[-36,-240,60,0],a:{hand:[52,-234],head:[0,-182]},o:[
  ["c",0,-182,17],["p","M-21,-160Q0,-169 21,-160L18,-88L-18,-88Z"],["s",14,"M-8,-92L-10,0M8,-92L11,0"],["s",10,"M-20,-152L-28,-110L-29,-82M20,-152L42,-190L50,-224"]]},
 "stand-point":{k:"figure",b:[-36,-200,104,0],a:{hand:[100,-152],head:[0,-182]},o:[
  ["c",0,-182,17],["p","M-21,-160Q0,-169 21,-160L18,-88L-18,-88Z"],["s",14,"M-8,-92L-10,0M8,-92L11,0"],["s",10,"M-20,-152L-28,-110L-29,-82M20,-152L60,-150L94,-153"]]},
 "stand-phone":{k:"figure",b:[-36,-200,36,0],a:{hand:[2,-140],head:[0,-182]},o:[
  ["c",3,-180,17],["p","M-21,-160Q0,-169 21,-160L18,-88L-18,-88Z"],["s",14,"M-8,-92L-10,0M8,-92L11,0"],["s",10,"M20,-152L26,-116L8,-128M-20,-152L-24,-116L-4,-128"],
  ["r",-8,-152,18,26],["Lr",-5,-149,12,20]]},
 "walk":{k:"figure",b:[-44,-200,44,0],a:{hand:[42,-90],head:[4,-182]},o:[
  ["c",4,-182,17],["p","M-18,-160Q3,-169 23,-160L18,-88L-16,-88Z"],["s",14,"M-6,-92L-24,-46L-36,0M6,-92L18,-48L32,-2"],["s",10,"M-18,-152L-32,-118L-40,-90M21,-152L33,-116L42,-92"]]},
 "stand-basket":{k:"figure",b:[-44,-212,36,0],a:{hand:[-16,-116],head:[0,-182]},o:[
  ["c",0,-182,17],["e",0,-197,32,6,0],["p","M-17,-198Q0,-224 17,-198Z"],["p","M-21,-160Q0,-169 21,-160L18,-88L-18,-88Z"],["s",14,"M-8,-92L-10,0M8,-92L11,0"],
  ["s",10,"M20,-152L28,-110L29,-82M-20,-152L-30,-112L-14,-100"],["p","M-40,-110L6,-110L-2,-80L-32,-80Z"]]},
 "sit-write":{k:"figure",b:[-24,-190,80,0],a:{hand:[74,-104],head:[30,-172]},o:[
  ["c",30,-172,16],["p","M-20,-92L-8,-156Q10,-170 28,-152L20,-92Z"],["s",10,"M14,-148L42,-118L74,-104"],["s",15,"M-10,-92L38,-90"],["s",12,"M38,-90L40,-10"],["s",9,"M40,-6L54,-4"]]},
 "sit-read":{k:"figure",b:[-24,-196,66,0],a:{hand:[46,-130],head:[8,-178]},o:[
  ["c",8,-178,16],["p","M-18,-92L-15,-158Q2,-168 19,-158L18,-92Z"],["s",10,"M14,-150L28,-116L44,-128"],["p","M36,-150L60,-140L52,-116L28,-126Z"],
  ["s",15,"M-10,-92L38,-90"],["s",12,"M38,-90L40,-10"],["s",9,"M40,-6L54,-4"]]},
 "sit-think":{k:"figure",b:[-24,-196,60,0],a:{hand:[18,-162],head:[8,-180]},o:[
  ["c",8,-180,16],["p","M-18,-92L-15,-158Q2,-168 19,-158L18,-92Z"],["s",10,"M14,-150L34,-108L18,-160"],["s",15,"M-10,-92L38,-90"],["s",12,"M38,-90L40,-10"],["s",9,"M40,-6L54,-4"]]},
 "sit-ground":{k:"figure",b:[-22,-110,70,0],a:{hand:[48,-60],head:[20,-92]},o:[
  ["c",20,-92,15],["p","M-16,-4L-10,-72Q4,-82 18,-70L16,-4Z"],["s",14,"M8,-8L42,-46L62,-4"],["s",9,"M14,-64L36,-50L48,-60"],["p","M40,-74L60,-66L56,-48L36,-56Z"]]},
 "hand-phone":{k:"figure",b:[-70,-270,72,0],a:{hand:[0,-262],screen:[0,-170]},o:[
  ["p","M-62,0Q-64,-80 -40,-118L-26,-84Q8,-66 52,-86L66,-56Q52,-6 46,0Z"],["r",-50,-264,100,190],["Lr",-41,-254,82,168],
  ["Br",-34,-240,44,16],["Br",-14,-212,48,16],["Br",-34,-184,56,22],["Br",-6,-152,40,16],["s",18,"M52,-84L60,-128"],["s",16,"M-40,-112L-52,-148"]]},
 "pair-table":{k:"figure",b:[-170,-190,170,0],a:{hand:[0,-150],middle:[0,-150]},o:[
  ["u","chair",-130,0,1],["u","chair",130,0,-1],["u","sit-write",-120,0,1],["u","sit-write",120,0,-1],["r",-74,-106,148,8],["r",-4,-98,8,92],["e",0,-4,34,5,0]]},
 "audience":{k:"figure",b:[-170,-80,170,0],a:{middle:[0,-80]},o:[
  ["c",-140,-52,17],["e",-140,-2,32,26,0],["c",-70,-60,17],["e",-70,-6,32,30,0],["c",0,-54,17],["e",0,-2,32,28,0],["c",70,-62,17],["e",70,-8,32,30,0],["c",140,-52,17],["e",140,-2,32,26,0],
  ["r",-175,-4,350,8]]},
 /* ---- props ---- */
 "desk":{k:"prop",b:[-110,-104,110,0],a:{top:[0,-104],left:[-80,-104],right:[80,-104]},o:[["r",-110,-104,220,9],["r",-100,-96,8,96],["r",92,-96,8,96]]},
 "table":{k:"prop",b:[-74,-106,74,0],a:{top:[0,-106]},o:[["r",-74,-106,148,8],["r",-4,-98,8,92],["e",0,-4,34,5,0]]},
 "chair":{k:"prop",b:[-32,-172,26,0],a:{seat:[0,-92]},o:[["s",6,"M-24,-92L-30,-170"],["r",-28,-95,52,7],["s",5,"M-22,-88L-24,0M20,-88L22,0"]]},
 "lamp":{k:"prop",b:[-24,-102,72,0],a:{light:[50,-70]},o:[["e",0,-3,22,4,0],["s",5,"M0,-4L12,-56L40,-84"],["p","M28,-100L72,-88L60,-64L18,-76Z"],["Lp","M60,-64L18,-76L22,-70L56,-60Z"]]},
 "laptop":{k:"prop",b:[-36,-52,36,0],a:{screen:[1,-28]},o:[["p","M-36,0L36,0L31,-5L-31,-5Z"],["p","M-27,-5L-23,-52L26,-52L29,-5Z"],["lp","M-22,-10L-19,-47L21,-47L24,-10Z"]]},
 "window":{k:"prop",b:[-92,-204,92,6],a:{centre:[0,-100]},o:[["lr",-80,-200,160,200],["s",8,"M-80,-200L80,-200L80,0L-80,0ZM0,-200L0,0M-80,-100L80,-100"],["r",-92,-2,184,8]]},
 "stage":{k:"prop",b:[-300,-44,300,0],a:{top:[0,-44]},o:[["r",-300,-44,600,44],["Br",-300,-44,600,3]]},
 "hills":{k:"prop",b:[-400,-140,400,0],a:{peak:[150,-130]},o:[["p","M-400,0L-400,-60Q-300,-110 -180,-80Q-60,-50 40,-96Q160,-142 280,-90Q350,-64 400,-74L400,0Z"]]},
 "field-rows":{k:"prop",b:[-400,-150,400,0],a:{far:[0,-150]},o:[["s",3,(function(){var d="";for(var x=-400;x<=400;x+=50)d+="M0,-150L"+x+",0";return d;})()],
  ["s",2,"M-46,-132L46,-132M-96,-110L96,-110M-160,-82L160,-82M-250,-44L250,-44"]]},
 "skyline":{k:"prop",b:[-400,-230,400,0],a:{top:[60,-230]},o:(function(){var o=[],x=-400,s=17;function R(){s=(s*1664525+1013904223)>>>0;return s/4294967296;}
  while(x<400){var w=50+R()*70,h=90+R()*140;o.push(["r",x,-h,w-4,h]);for(var wx=x+8;wx<x+w-16;wx+=14)for(var wy=-h+10;wy<-12;wy+=18)if(R()<.3)o.push(["lr",wx,wy,6,9]);x+=w;}return o;})()},
 "flag":{k:"prop",b:[-3,-122,46,0],a:{top:[0,-120]},o:[["s",4,"M0,0L0,-120"],["Lp","M2,-120L44,-108L2,-96Z"]]},
 "plant":{k:"prop",b:[-44,-112,44,0],a:{top:[8,-110]},o:[["p","M-18,0L18,0L22,-34L-22,-34Z"],["s",6,"M0,-34Q-10,-70 -30,-90M0,-34Q4,-80 8,-110M0,-34Q14,-64 34,-84M0,-34Q-22,-52 -42,-56M0,-34Q20,-46 40,-50"]]},
 "seedling":{k:"prop",b:[-30,-70,30,0],a:{top:[4,-66]},o:[["e",0,-2,26,4,0],["s",5,"M0,-2Q-2,-30 2,-56"],["p","M1,-34Q-24,-50 -30,-36Q-18,-24 1,-30Z"],["p","M2,-50Q22,-70 30,-58Q22,-42 2,-46Z"]]},
 "book":{k:"prop",b:[-40,-22,40,0],a:{top:[0,-12]},o:[["p","M-38,-3L-38,-9Q-18,-21 0,-11Q18,-21 38,-9L38,-3Q18,-13 0,-4Q-18,-13 -38,-3Z"],["r",-38,-4,76,4]]},
 "phone":{k:"prop",b:[-15,-52,15,0],a:{screen:[0,-26]},o:[["r",-15,-52,30,52],["Lr",-11,-47,22,40]]},
 "basket":{k:"prop",b:[-32,-62,32,0],a:{top:[0,-46]},o:[["p","M-32,-30L32,-30L25,0L-25,0Z"],["s",4,"M-24,-30Q0,-66 24,-30"],["Bs",2,"M-28,-20L28,-20M-26,-10L26,-10"]]}
};
Ink.parts=P;
Ink.names=function(kind){return Object.keys(P).filter(function(n){return !kind||P[n].k===kind;});};

/* ---------- colour ---------- */
var T={};// tokens for the current scene
function col(v,fb){if(v==null)v=fb;if(v==null)return null;if(v==="ball")return BALL;if(typeof v==="string"&&v[0]!=="#"&&v.indexOf("(")<0&&T[v])return T[v];return v;}
function rgba(h,a){var n=parseInt(h.slice(1),16);return "rgba("+(n>>16)+","+((n>>8)&255)+","+(n&255)+","+a+")";}
function rng(seed){return function(){seed=(seed*1664525+1013904223)>>>0;return seed/4294967296;};}
function lum(h){var n=parseInt(h.slice(1),16),c=[n>>16,(n>>8)&255,n&255].map(function(v){v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4);});return .2126*c[0]+.7152*c[1]+.0722*c[2];}

/* ---------- drawing a part ---------- */
function drawOps(g,name,cs){var part=P[name];if(!part)throw new Error("Ink: no part '"+name+"'. Ink.names() lists them.");
  part.o.forEach(function(op){var t=op[0],pre=t.length>1?t[0]:"",kind=t.length>1?t.slice(1):t,c=cs.ink,a=1;
    if(pre==="L")c=cs.light;else if(pre==="l"){c=cs.light;a=.3;}else if(pre==="B")c=cs.ground;
    if(cs.solid&&pre)return;  // the rim pass draws the silhouette only
    g.globalAlpha=a;g.fillStyle=c;g.strokeStyle=c;g.lineCap="round";g.lineJoin="round";
    if(kind==="c"){g.beginPath();g.arc(op[1],op[2],op[3],0,7);g.fill();}
    else if(kind==="e"){g.beginPath();g.ellipse(op[1],op[2],op[3],op[4],op[5]||0,0,7);g.fill();}
    else if(kind==="r"){g.fillRect(op[1],op[2],op[3],op[4]);}
    else if(kind==="p"){g.fill(new Path2D(op[1]));}
    else if(kind==="s"){g.lineWidth=op[1];g.stroke(new Path2D(op[2]));}
    else if(kind==="u"){g.save();g.translate(op[2],op[3]);g.scale(op[4]||1,1);drawOps(g,op[1],cs);g.restore();}
    g.globalAlpha=1;});}

Ink.svg=function(name,ink,light,ground){var part=P[name],b=part.b,pad=8;ink=ink||"#1b1b1b";light=light||"#F2D9A0";ground=ground||"#ffffff";
  function ops(nm,tf){return P[nm].o.map(function(op){var t=op[0],pre=t.length>1?t[0]:"",k=t.length>1?t.slice(1):t,c=pre==="L"?light:pre==="l"?light:pre==="B"?ground:ink,
    o=pre==="l"?' fill-opacity=".3"':"";
    if(k==="c")return '<circle cx="'+op[1]+'" cy="'+op[2]+'" r="'+op[3]+'" fill="'+c+'"'+o+'/>';
    if(k==="e")return '<ellipse cx="'+op[1]+'" cy="'+op[2]+'" rx="'+op[3]+'" ry="'+op[4]+'" fill="'+c+'"'+o+'/>';
    if(k==="r")return '<rect x="'+op[1]+'" y="'+op[2]+'" width="'+op[3]+'" height="'+op[4]+'" fill="'+c+'"'+o+'/>';
    if(k==="p")return '<path d="'+op[1]+'" fill="'+c+'"'+o+'/>';
    if(k==="s")return '<path d="'+op[2]+'" fill="none" stroke="'+c+'" stroke-width="'+op[1]+'" stroke-linecap="round" stroke-linejoin="round"/>';
    if(k==="u")return '<g transform="translate('+op[2]+' '+op[3]+') scale('+(op[4]||1)+' 1)">'+ops(op[1])+'</g>';return "";}).join("");}
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="'+(b[0]-pad)+' '+(b[1]-pad)+' '+(b[2]-b[0]+2*pad)+' '+(b[3]-b[1]+2*pad)+'">'+ops(name)+'</svg>';};

/* ---------- light ---------- */
function loopPts(cx,cy,r,rx,ry,wob,ph){var p=[],n=110;for(var i=0;i<n;i++){var t=i/n*Math.PI*2,k=1+wob*(Math.sin(3*t+ph)*.5+Math.sin(5*t+ph*1.7)*.3+Math.sin(9*t+ph*.6)*.2);p.push([cx+Math.cos(t)*r*rx*k,cy+Math.sin(t)*r*ry*k]);}return p;}
function poly(g,p){g.beginPath();p.forEach(function(q,i){i?g.lineTo(q[0],q[1]):g.moveTo(q[0],q[1]);});g.closePath();}
var LIGHT={
 // steps: flat stepped pools on the message, with a stepped wedge from the source when there is one. The default.
 steps:function(g,L,u){var to=L.to,c=L.c,n=4,R=u*(L.size||.28);
  if(L.from){var dx=to[0]-L.from[0],dy=to[1]-L.from[1],d=Math.hypot(dx,dy)||1,nx=-dy/d,ny=dx/d;
    for(var j=0;j<3;j++){var w=R*(1-j*.28);g.fillStyle=rgba(c,.045);g.beginPath();g.moveTo(L.from[0],L.from[1]);g.lineTo(to[0]+nx*w,to[1]+ny*w);g.lineTo(to[0]-nx*w,to[1]-ny*w);g.closePath();g.fill();}}
  for(var i=0;i<n;i++){var r=R*(1-i/n);poly(g,loopPts(to[0],to[1],r,1.25,.8,.04,i));g.fillStyle=rgba(c,.05+i*.012);g.fill();}},
 // trail: a dashed route that leads the eye from a start to the message
 trail:function(g,L,u){var a=L.from||[to0(L)],b=L.to,mx=(a[0]+b[0])/2,my=(a[1]+b[1])/2,dx=b[0]-a[0],dy=b[1]-a[1];
  g.strokeStyle=rgba(L.c,.85);g.lineWidth=Math.max(2,u*.006);g.lineCap="round";g.setLineDash([u*.018,u*.016]);
  g.beginPath();g.moveTo(a[0],a[1]);g.quadraticCurveTo(mx-dy*.25,my+dx*.25,b[0],b[1]);g.stroke();g.setLineDash([]);
  function to0(){return [b[0]-u*.4,b[1]+u*.2];}},
 // contours: rings. One hero per piece, never everywhere.
 contours:function(g,L,u){var n=L.rings||9,step=u*(L.size||.3)/n;
  for(var i=n;i>=1;i--){poly(g,loopPts(L.to[0],L.to[1],i*step,1.2,1,.06,i*.9));g.fillStyle=rgba(L.c,.06*(n+1-i)/n);g.fill();g.strokeStyle=rgba(L.c,.07+.4*(n+1-i)/n);g.lineWidth=Math.max(1.5,u*.0028);g.stroke();}},
 // grid: survey crosses that step brighter near the message
 grid:function(g,L,u,W,H){var s=u*.07,R=u*(L.size||.3);g.lineWidth=Math.max(1.2,u*.0022);
  for(var x=s/2;x<W;x+=s)for(var y=s/2;y<H;y+=s){if(L.skip&&L.skip(x,y))continue;var d=Math.hypot(x-L.to[0],y-L.to[1]),a=d<R*.33?.75:d<R*.66?.48:d<R?.26:0;if(!a)continue;
   g.strokeStyle=rgba(L.c,a);g.beginPath();g.moveTo(x-s*.09,y);g.lineTo(x+s*.09,y);g.moveTo(x,y-s*.09);g.lineTo(x,y+s*.09);g.stroke();}}
};

/* ---------- images from the bundled assets ---------- */
var cache={};
function img(url){if(!url)return Promise.resolve(null);if(cache[url])return cache[url];var im=new Image();im.src=url;cache[url]=(im.decode?im.decode():new Promise(function(r){im.onload=r;})).then(function(){return im;},function(){return null;});return cache[url];}
function tinted(im,w,h,c){var t=document.createElement("canvas");t.width=Math.max(1,w|0);t.height=Math.max(1,h|0);var x=t.getContext("2d");x.drawImage(im,0,0,t.width,t.height);x.globalCompositeOperation="source-in";x.fillStyle=c;x.fillRect(0,0,t.width,t.height);return t;}

var SHAPES={"16:9":[1600,900],"4:5":[1080,1350],"9:16":[1080,1920],"3:1":[1500,500],"1:1":[1080,1080]};

/* ---------- the scene ---------- */
Ink.scene=function(target,cfg){
  var cv=typeof target==="string"?document.querySelector(target):target;cfg=cfg||{};
  T=Object.assign({},cfg.tokens||{});
  var sz=cfg.size||SHAPES[cfg.shape||"16:9"];if(!sz)throw new Error("Ink: shape is one of "+Object.keys(SHAPES).join(", "));
  var W=sz[0],H=sz[1],u=Math.min(W,H),g;cv.width=W;cv.height=H;g=cv.getContext("2d");
  var warn=[],placed={},ground=col(cfg.ground,"bg")||"#141613",dark=lum(ground)<.2;
  var ink=col(cfg.ink)||(dark?"#07090a":(T.tx||"#1d1b1a")),light=col(cfg.light,"p1")||"#F2D9A0";
  function pt(v){if(v==null)return null;if(Array.isArray(v))return [v[0]*W,v[1]*H];var m=String(v).split(".");var p=placed[m[0]];
    if(!p){warn.push("no placed part '"+m[0]+"' for "+v);return null;}var a=P[p.name].a[m[1]];if(!a){warn.push("part "+p.name+" has no anchor '"+m[1]+"'");return null;}
    return [p.x+a[0]*p.s*p.dir,p.y+a[1]*p.s];}
  var fonts=(document.fonts&&document.fonts.ready)?document.fonts.ready:Promise.resolve();
  var B=cfg.bloom,Ld=cfg.land,Ht=cfg.hatch;
  var job=Promise.all([fonts,img(B&&Ink.assets.masks[B.name]),img(Ld&&Ink.assets.masks[Ld.name||"ground"]),img(Ht&&Ink.assets.tiles["hatch-"+(Ht.tile||"slant")]),img(cfg.grain!==false&&Ink.assets.tiles.grain)]).then(function(r){
    var bIm=r[1],lIm=r[2],hIm=r[3],gIm=r[4];
    if(B&&!bIm)warn.push("bloom '"+B.name+"' not bundled: run kit.py bundle");
    // 1 ground and grid
    g.fillStyle=ground;g.fillRect(0,0,W,H);
    // the words' box, measured first: the grid and the light keep out of it
    var tc=col(cfg.text&&cfg.text.c,"tx")||(dark?"#EDEAE4":ink),tb=cfg.text?words(g,cfg.text,W,H,u,tc,null,true):null,tpad=u*.03;
    function inText(x,y){return tb&&x>tb[0]-tpad&&x<tb[2]+tpad&&y>tb[1]-tpad&&y<tb[3]+tpad;}
    if(cfg.grid!==false){var gc=col(cfg.grid&&cfg.grid!==true?cfg.grid:null,dark?"#E9EAE4":ink),s=u*.07;g.strokeStyle=rgba(gc,dark?.06:.08);g.lineWidth=Math.max(1.2,u*.0022);
      for(var x=s/2;x<W;x+=s)for(var y=s/2;y<H;y+=s){if(inText(x,y))continue;g.beginPath();g.moveTo(x-s*.09,y);g.lineTo(x+s*.09,y);g.moveTo(x,y-s*.09);g.lineTo(x,y+s*.09);g.stroke();}}
    // place parts first (anchors only) so light and ball can aim at them
    // a part sits at [x,y] (0..1, its feet) or on an earlier part's anchor: ["lamp","desk.left",1]
    var parts=[];(cfg.parts||[]).forEach(function(it){var on=typeof it[1]==="string",q=on?pt(it[1]):[it[1]*W,it[2]*H],o=(on?it[3]:it[4])||{},sc=(on?it[2]:it[3])||1;
      if(!P[it[0]])throw new Error("Ink: no part '"+it[0]+"'");if(!q)return;var p={name:it[0],x:q[0],y:q[1],s:sc*u/600,dir:o.dir||1,o:o};placed[o.id||p.name]=p;parts.push(p);});
    var ballAt=pt(cfg.ball);
    // 2 bloom (one per picture) and land
    var bloomBox=null;
    if(B&&bIm){var c=pt(B.at||[.6,.4]),bs=u*(B.size||.6);bloomBox=[c[0]-bs*.42,c[1]-bs*.42,c[0]+bs*.42,c[1]+bs*.42];
      g.globalAlpha=B.o==null?.85:B.o;g.drawImage(tinted(bIm,bs,bs,col(B.c,"b2")||light),c[0]-bs/2,c[1]-bs/2);g.globalAlpha=1;}
    if(Ld&&lIm){var top=(Ld.top==null?.7:Ld.top)*H,lh=(H-top)*1.9;g.globalAlpha=Ld.o==null?.9:Ld.o;g.drawImage(tinted(lIm,W*1.1,lh,col(Ld.c,"b3")||ink),-W*.05,top-lh*.44);g.globalAlpha=1;}
    // 3 light: one kind, aimed at the message
    var Lt=cfg.light;if(Lt){var kind=Lt.kind||"steps";if(!LIGHT[kind])throw new Error("Ink: light is steps, trail, contours or grid");
      var L={to:pt(Lt.to||cfg.ball),from:pt(Lt.from),c:col(Lt.c,"p1")||light,size:Lt.size,rings:Lt.rings,skip:inText};
      if(!L.to)warn.push("light has no target: give light.to or a ball");else LIGHT[kind](g,L,u,W,H);}
    // 4 hatching on an area (ground, a wall, a band)
    if(Ht&&hIm){var A=Ht.area||[0,.82,1,1],hx=A[0]*W,hy=A[1]*H,hw=(A[2]-A[0])*W,hh=(A[3]-A[1])*H,tile=tinted(hIm,u*.32,u*.32,col(Ht.c,dark?"p2":"mu")||ink);
      g.save();g.beginPath();g.rect(hx,hy,hw,hh);g.clip();g.globalAlpha=Ht.o==null?.45:Ht.o;g.fillStyle=g.createPattern(tile,"repeat");g.fillRect(hx,hy,hw,hh);g.restore();g.globalAlpha=1;}
    // 5 parts: rim pass (offset, rim colour) then ink
    parts.forEach(function(p){var o=p.o,rim=col(o.rim!=null?o.rim:(P[p.name].k==="figure"?cfg.rim:null));
      var cs={ink:col(o.c)||ink,light:col(o.light)||light,ground:ground};
      if(rim){g.save();g.translate(p.x+u*.006*p.dir,p.y-u*.004);g.scale(p.s*p.dir,p.s);drawOps(g,p.name,{ink:rim,light:rim,ground:rim,solid:true});g.restore();}
      g.save();g.translate(p.x,p.y);g.scale(p.s*p.dir,p.s);drawOps(g,p.name,cs);g.restore();});
    // 6 the ball: the one bright thing
    if(ballAt){var br=u*(cfg.ballSize||.018);g.fillStyle=BALL;g.beginPath();g.arc(ballAt[0],ballAt[1],br,0,7);g.fill();
      g.strokeStyle="rgba(255,255,255,.6)";g.lineWidth=Math.max(1.5,br*.14);g.beginPath();g.arc(ballAt[0]-br*.8,ballAt[1],br*.82,-1.1,1.1);g.stroke();
      if(!dark){g.strokeStyle=rgba(ink,.8);g.lineWidth=Math.max(1.5,br*.1);g.beginPath();g.arc(ballAt[0],ballAt[1],br,0,7);g.stroke();}}
    // 7 words: a clear band, checked against the bloom
    if(cfg.text){tb=words(g,cfg.text,W,H,u,tc,col(cfg.text.sub_c,"mu"));
      if(bloomBox&&tb&&!(tb[2]<bloomBox[0]||tb[0]>bloomBox[2]||tb[3]<bloomBox[1]||tb[1]>bloomBox[3]))warn.push("text sits on the bloom: move bloom.at or text.at");}
    // 8 signature: stamp and field tag, then grain
    var mc=col(cfg.mark,"mu")||rgba(dark?"#E9EAE4":ink,.6),fs=Math.round(u*.019);g.font="500 "+fs+"px 'Overpass Mono', ui-monospace, monospace";g.fillStyle=mc;
    if(cfg.stamp){g.textAlign="right";g.fillText(cfg.stamp,W-u*.04,H-u*.04);g.textAlign="left";}
    if(cfg.tag){var tx=u*.04,ty=u*.05;g.strokeStyle=mc;g.lineWidth=Math.max(1.2,fs*.08);g.beginPath();g.moveTo(tx,ty-fs*.35);g.lineTo(tx+fs*.7,ty-fs*.35);g.moveTo(tx+fs*.35,ty-fs*.7);g.lineTo(tx+fs*.35,ty);g.stroke();
      g.fillText(String(cfg.tag).toUpperCase(),tx+fs*1.2,ty);}
    if(gIm){g.globalAlpha=dark?.5:.35;g.fillStyle=g.createPattern(gIm,"repeat");g.fillRect(0,0,W,H);g.globalAlpha=1;}
    cv.dataset.inkWarn=warn.join(" | ");if(warn.length&&root.console)console.warn("Ink:",warn.join(" | "));
    if(!cv.getAttribute("role")){cv.setAttribute("role","img");if(cfg.alt)cv.setAttribute("aria-label",cfg.alt);}
    return cv;});
  Ink.pending.push(job);return job;
};

// title and sub in a band at top, bottom or left; returns the box it used
function words(g,t,W,H,u,c,mc,measure){var pad=u*.07,at=t.at||"top",maxW=at==="left"?W*.42:W-pad*2,ts=u*(t.size||.072),ss=ts*.46;
  g.fillStyle=c;g.textBaseline="top";g.font="800 "+ts+"px Overpass, system-ui, sans-serif";var tl=wrap(g,t.title||"",maxW);
  g.font="400 "+ss+"px 'Atkinson Hyperlegible', system-ui, sans-serif";var sl=wrap(g,t.sub||"",maxW);
  var h=tl.length*ts*1.08+(sl.length?ss*.8+sl.length*ss*1.4:0),x=pad,y=at==="bottom"?H-pad-h:at==="left"?(H-h)/2:pad*1.15;
  if(measure){g.textBaseline="alphabetic";var mw=0;g.font="800 "+ts+"px Overpass, system-ui, sans-serif";tl.forEach(function(l){mw=Math.max(mw,g.measureText(l).width);});return [x,y,x+mw,y+h];}
  g.font="800 "+ts+"px Overpass, system-ui, sans-serif";tl.forEach(function(l,i){g.fillText(l,x,y+i*ts*1.08);});
  g.font="400 "+ss+"px 'Atkinson Hyperlegible', system-ui, sans-serif";g.fillStyle=mc||c;var y2=y+tl.length*ts*1.08+ss*.8;sl.forEach(function(l,i){g.fillText(l,x,y2+i*ss*1.4);});
  g.textBaseline="alphabetic";var w=0;g.font="800 "+ts+"px Overpass";tl.forEach(function(l){w=Math.max(w,g.measureText(l).width);});return [x,y,x+Math.max(w,maxW*.6),y+h];}
function wrap(g,s,m){var out=[],line="";String(s).split(/\s+/).forEach(function(w){if(!w)return;var t=line?line+" "+w:w;if(g.measureText(t).width>m&&line){out.push(line);line=w;}else line=t;});if(line)out.push(line);return out;}

Ink.png=function(cv,name){cv=typeof cv==="string"?document.querySelector(cv):cv;var a=document.createElement("a");a.download=name||"scene.png";a.href=cv.toDataURL("image/png");a.click();};
Ink.shapes=SHAPES;
root.Ink=Ink;
})(typeof window!=="undefined"?window:this);
