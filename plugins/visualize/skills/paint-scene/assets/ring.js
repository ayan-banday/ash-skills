/* paint-scene ring.js: the Ring Eyes look. Flat Wada colour, wobbly hand lettering, black characters with white ring eyes.
   Ring.svg("fuji", {expr:"happy", pose:"wave"})  -> an SVG string in a 200x200 box.
   Ring.piece("#el", {format:"post", bg:"#afd472", words:[...], cast:[...]})  -> fills a template (formats below).
   Ring.mount()  -> swaps every <i data-ring="loop" data-expr="closed"></i> on the page for its SVG (the Touch level).
   Ring.names(), Ring.cast[name].meaning, Ring.EXPRS, Ring.POSES, Ring.FORMATS.  Menu and rules: references/ring-eyes.md. */
(function(root){
"use strict";
var INK="#111314",BALL="#F58E84",WHITE="#ffffff";
var Ring={INK:INK,BALL:BALL,cast:{},T:{}};

function lum(h){if(!h||h[0]!=="#")return 0;var n=parseInt(h.slice(1).padEnd(6,"0").slice(0,6),16),c=[n>>16,(n>>8)&255,n&255].map(function(v){v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4);});return .2126*c[0]+.7152*c[1]+.0722*c[2];}
function col(v,fb){if(v==null||v==="")return fb;if(v==="ink")return INK;if(v==="ball")return BALL;if(v==="white")return WHITE;if(v[0]!=="#"&&Ring.T[v])return Ring.T[v];return v;}
function rng(seed){return function(){seed=(seed*1664525+1013904223)>>>0;return seed/4294967296;};}

/* ---------- a character ----------
   Ring.add(name, {meaning, body(c) -> svg, face:{eyes:[[x,y],[x,y]], r, sw, mouth:[x,y], socket}, arms:{l:[x,y], r:[x,y]}, feet:{l:[x,y], r:[x,y]}, rot:[deg,cx,cy]})
   c = {body, eye, detail, ink, ball}. Draw only the body in body(); the engine adds eyes, mouth, arms and legs. */
Ring.add=function(name,def){def.name=name;Ring.cast[name]=def;return Ring;};
Ring.names=function(){return Object.keys(Ring.cast);};

/* ---------- expressions: everything lives in the eyes, plus a dot mouth ---------- */
Ring.EXPRS=["open","closed","happy","side","surprised","worried","sleepy","wink"];
function ring(x,y,r,sw,c){return '<circle cx="'+x+'" cy="'+y+'" r="'+r+'" fill="none" stroke="'+c+'" stroke-width="'+sw+'"/>';}
function arc(d,sw,c){return '<path d="'+d+'" fill="none" stroke="'+c+'" stroke-width="'+sw+'" stroke-linecap="round"/>';}
function face(def,c,o){var f=def.face;if(!f)return "";var e=o.expr||"open",r=f.r,sw=f.sw||Math.max(3.5,r*.3),ec=c.eye,out="",look=o.look==null?1:o.look;
  var mc=f.mouthColor?col(f.mouthColor,c.eye):c.eye;
  f.eyes.forEach(function(p,i){var x=p[0],y=p[1],ee=e==="wink"?(i===1?"closed":"open"):e;
    if(f.socket&&ee!=="closed"&&ee!=="happy")out+='<circle cx="'+x+'" cy="'+y+'" r="'+(r*1.55)+'" fill="'+INK+'"/>';
    if(ee==="open")out+=ring(x,y,r,sw,ec);
    else if(ee==="closed")out+=arc("M"+(x-r)+" "+y+" Q"+x+" "+(y+r*.9)+" "+(x+r)+" "+y,sw,f.socket?INK:ec);
    else if(ee==="happy")out+=arc("M"+(x-r)+" "+(y+r*.35)+" Q"+x+" "+(y-r*.95)+" "+(x+r)+" "+(y+r*.35),sw,f.socket?INK:ec);
    else if(ee==="side")out+=ring(x,y,r,sw,ec)+'<circle cx="'+(x+look*r*.42)+'" cy="'+y+'" r="'+(r*.42)+'" fill="'+ec+'"/>';
    else if(ee==="surprised")out+=ring(x,y-r*.1,r*1.22,sw,ec);
    else if(ee==="worried")out+=ring(x,y,r*.9,sw,ec)+arc("M"+(x-r*.9)+" "+(y-r*(i?1.45:1.85))+" L"+(x+r*.9)+" "+(y-r*(i?1.85:1.45)),sw*.9,ec);
    else if(ee==="sleepy")out+=arc("M"+(x-r)+" "+y+" A"+r+" "+r+" 0 0 0 "+(x+r)+" "+y,sw,ec)+arc("M"+(x-r*1.15)+" "+y+" L"+(x+r*1.15)+" "+y,sw,ec);});
  if(f.mouth){var mx=f.mouth[0],my=f.mouth[1];
    if(e==="surprised")out+=ring(mx,my+2,Math.max(4,r*.3),Math.max(2.5,sw*.6),mc);
    else if(e==="happy")out+=arc("M"+(mx-r*.45)+" "+(my-2)+" Q"+mx+" "+(my+r*.5)+" "+(mx+r*.45)+" "+(my-2),Math.max(2.5,sw*.6),mc);
    else if(e==="worried")out+=arc("M"+(mx-r*.4)+" "+(my+3)+" Q"+mx+" "+(my-r*.3)+" "+(mx+r*.4)+" "+(my+3),Math.max(2.5,sw*.6),mc);
    else out+='<circle cx="'+mx+'" cy="'+my+'" r="3.5" fill="'+mc+'"/>';}
  return out;}

/* ---------- poses: stick limbs from the body's shoulder and hip points ---------- */
Ring.POSES=["still","stand","walk","wave","cheer","point","hold","shrug","sit","hop"];
var ARM={rest:function(p,s){return [[p[0]+s*6,p[1]+30],[p[0]+s*8,p[1]+56]];},
 wave:function(p,s){return [[p[0]+s*30,p[1]-18],[p[0]+s*26,p[1]-56]];},
 up:function(p,s){return [[p[0]+s*22,p[1]-30],[p[0]+s*34,p[1]-62]];},
 out:function(p,s){return [[p[0]+s*32,p[1]-2],[p[0]+s*66,p[1]-6]];},
 hold:function(p,s){return [[p[0]+s*14,p[1]+28],[p[0]-s*14,p[1]+40]];},
 shrug:function(p,s){return [[p[0]+s*28,p[1]+10],[p[0]+s*44,p[1]-16]];}};
var POSE={still:[null,null,null],stand:["rest","rest","stand"],walk:["rest","rest","walk"],wave:["rest","wave","stand"],cheer:["up","up","stand"],
 point:["rest","out","stand"],hold:["hold","hold","stand"],shrug:["shrug","shrug","stand"],sit:["rest","rest","sit"],hop:["up","up","hop"]};
function limbs(def,c,o){var pz=POSE[o.pose||"still"]||POSE.still,out="",lc=c.limb,w=o.limbW||9;
  function path(pts){return '<path d="M'+pts.map(function(q){return q[0].toFixed(1)+" "+q[1].toFixed(1);}).join(" L")+'" fill="none" stroke="'+lc+'" stroke-width="'+w+'" stroke-linecap="round" stroke-linejoin="round"/>';}
  if(def.arms&&pz[0]){var L=def.arms.l,R=def.arms.r;out+=path([L].concat(ARM[pz[0]](L,-1)))+path([R].concat(ARM[pz[1]](R,1)));}
  return out;}
function legs(def,c,o){var pz=POSE[o.pose||"still"]||POSE.still,k=pz[2];if(!def.feet||!k)return "";var L=def.feet.l,R=def.feet.r,lc=c.limb,w=(o.limbW||9)+1,out="";
  function path(pts){return '<path d="M'+pts.map(function(q){return q[0].toFixed(1)+" "+q[1].toFixed(1);}).join(" L")+'" fill="none" stroke="'+lc+'" stroke-width="'+w+'" stroke-linecap="round" stroke-linejoin="round"/>';}
  var g=def.legLen||40;
  if(k==="stand")out=path([L,[L[0]-2,L[1]+g],[L[0]-12,L[1]+g]])+path([R,[R[0]+2,R[1]+g],[R[0]+12,R[1]+g]]);
  if(k==="walk")out=path([L,[L[0]-14,L[1]+g*.55],[L[0]-24,L[1]+g]])+path([R,[R[0]+10,R[1]+g*.5],[R[0]+8,R[1]+g],[R[0]+20,R[1]+g]]);
  if(k==="sit")out=path([L,[L[0]+30,L[1]+4],[L[0]+32,L[1]+g]])+path([R,[R[0]+30,R[1]+4],[R[0]+32,R[1]+g]]);
  if(k==="hop")out=path([L,[L[0]-12,L[1]+g*.45],[L[0]+2,L[1]+g*.7]])+path([R,[R[0]+12,R[1]+g*.45],[R[0]-2,R[1]+g*.7]]);
  return out;}

/* ---------- one character as SVG ----------
   o: {body, eye, detail, limb, expr, look (1 right, -1 left), pose, tilt (deg), flip, title} */
Ring.inner=function(name,o){var def=Ring.cast[name];if(!def)throw new Error("Ring: no character '"+name+"'. Ring.names() lists them.");o=o||{};
  var body=col(o.body,def.defaultBody||INK),light=lum(body)>.35;
  var c={body:body,eye:col(o.eye,def.eye||(light?INK:WHITE)),detail:col(o.detail,light?INK:WHITE),ink:INK,ball:BALL,limb:col(o.limb,def.limb||(lum(body)<.06?body:INK))};
  var pz=POSE[o.pose||"still"]||POSE.still,hasLegs=!!(def.feet&&pz[2]),g=def.legLen||40;
  var bd=def.body(c,o);
  // coral is the one bright thing: with coral:false (set for you when the ball is in the piece) a character's coral details turn to its detail colour
  if(o.coral===false&&name!=="ball")bd=bd.replace(/#F58E84/gi,c.detail);
  var inner=bd+face(def,c,o),lim=limbs(def,c,o);
  if(def.rot)inner='<g transform="rotate('+def.rot.join(" ")+')">'+inner+lim+'</g>';else inner=inner+lim;
  var lg=legs(def,c,o);
  if(hasLegs){var lowest=Math.max(def.feet.l[1],def.feet.r[1])+g*(pz[2]==="hop"?.7:1),k=Math.min(1,196/lowest),dy=pz[2]==="hop"?-6:0;
    inner='<g transform="translate('+(100-100*k)+' '+dy+') scale('+k+')">'+lg+inner+'</g>';}
  var t=[];if(o.flip)t.push("translate(200 0) scale(-1 1)");if(o.tilt)t.push("rotate("+o.tilt+" 100 120)");
  return t.length?'<g transform="'+t.join(" ")+'">'+inner+'</g>':inner;};
Ring.svg=function(name,o){o=o||{};return '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" overflow="visible" style="overflow:visible"'+(o.title?' role="img" aria-label="'+o.title+'"':' aria-hidden="true"')+'>'+Ring.inner(name,o)+'</svg>';};

/* ---------- the first cast (from the Fuji ring-eyes study, Nov 11 2026) ---------- */
Ring.add("fuji",{meaning:"Fuji itself, any map or system; a mountain to climb",body:function(c){return '<path d="M0 200 C8 135 42 60 80 36 Q100 24 120 36 C158 60 192 135 200 200Z" fill="'+c.body+'"/>';},
  face:{eyes:[[74,112],[126,112]],r:18,sw:5,mouth:[100,140]},arms:{l:[44,128],r:[156,128]},feet:{l:[78,198],r:[122,198]}});
Ring.add("ball",{meaning:"the coral tennis ball: a tennis task, the thing the reader gets or decides",defaultBody:BALL,eye:WHITE,limb:INK,
  body:function(c){return '<circle cx="100" cy="100" r="92" fill="'+c.body+'"/><path d="M24 46 C70 78 70 124 24 156" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".75"/><path d="M176 46 C130 78 130 124 176 156" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".75"/>';},
  face:{eyes:[[78,96],[122,96]],r:16,sw:5,mouth:[100,126],mouthColor:"ink",socket:true},arms:{l:[12,110],r:[188,110]},feet:{l:[76,186],r:[124,186]}});
Ring.add("racket",{meaning:"a tennis task, back-and-forth work with someone",body:function(c){return '<ellipse cx="100" cy="76" rx="58" ry="70" fill="'+c.body+'"/><path d="M72 138 Q100 156 128 138 L110 160 L90 160Z" fill="'+c.body+'"/><rect x="91" y="150" width="18" height="50" rx="8" fill="'+c.body+'"/>';},
  face:{eyes:[[78,74],[122,74]],r:16,sw:5},arms:{l:[44,96],r:[156,96]}});
Ring.add("lamp",{meaning:"the night run, focus, a work session",body:function(c){return '<ellipse cx="62" cy="192" rx="48" ry="9" fill="'+c.body+'"/><path d="M62 188 L74 124 L112 78" fill="none" stroke="'+c.body+'" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/><path d="M82 34 L182 54 L164 132 L60 106Z" fill="'+c.body+'"/>';},
  face:{eyes:[[106,82],[144,82]],r:14,sw:4.5}});
Ring.add("loop",{meaning:"an open loop with a finish line, set the night before",body:function(c){return '<path d="M150 56 A64 64 0 1 0 150 132" fill="none" stroke="'+c.body+'" stroke-width="24" stroke-linecap="round"/><circle cx="156" cy="128" r="28" fill="'+c.body+'"/>';},
  face:{eyes:[[146,124],[168,124]],r:8,sw:3.5}});
Ring.add("note",{meaning:"a note, a raw reflection, a fog idea written down",rot:[-5,100,100],body:function(c){return '<path d="M28 28 H172 V140 L140 172 H28Z" fill="'+c.body+'"/><path d="M172 140 H140 V172Z" fill="'+c.detail+'" opacity=".35"/>';},
  face:{eyes:[[78,92],[122,92]],r:17,sw:5},arms:{l:[28,100],r:[172,100]},feet:{l:[70,172],r:[130,172]}});
Ring.add("flag",{meaning:"a finish line, a timebox, a goal reached",body:function(c){return '<rect x="40" y="16" width="10" height="184" rx="5" fill="'+c.body+'"/><path d="M50 22 L182 56 L50 102Z" fill="'+c.body+'"/>';},
  face:{eyes:[[86,60],[118,60]],r:11,sw:4}});
Ring.add("phone",{meaning:"capture on the phone, a message, a notification",body:function(c){return '<rect x="52" y="8" width="96" height="186" rx="20" fill="'+c.body+'"/><circle cx="138" cy="26" r="9" fill="'+BALL+'"/>';},
  face:{eyes:[[80,78],[120,78]],r:15,sw:5},arms:{l:[52,112],r:[148,112]},feet:{l:[80,192],r:[120,192]}});
Ring.add("sandwich",{meaning:"the Sandwich study method: tennis, golf, tennis",body:function(c){return '<path d="M20 90 Q20 30 100 30 Q180 30 180 90Z" fill="'+c.body+'"/><path d="M12 98 Q34 86 56 98 T100 98 T144 98 T188 98 V118 H12Z" fill="'+BALL+'"/><rect x="22" y="124" width="156" height="42" rx="14" fill="'+c.body+'"/>';},
  face:{eyes:[[78,66],[122,66]],r:15,sw:5},arms:{l:[22,106],r:[178,106]},feet:{l:[64,164],r:[136,164]}});
Ring.add("fog",{meaning:"the fog: ideas with no map yet",body:function(c){return '<g fill="'+c.body+'"><circle cx="66" cy="112" r="46"/><circle cx="112" cy="86" r="58"/><circle cx="158" cy="118" r="38"/><circle cx="104" cy="138" r="44"/></g>';},
  face:{eyes:[[92,104],[134,104]],r:15,sw:5},arms:{l:[22,120],r:[194,120]}});

/* @@CAST@@ (new characters are added below this line) */
/* planning and the log (drawn Nov 11 2026) */
Ring.add("calendar",{meaning:"a day set the night before: a wall-calendar page with its date waiting",body:function(c){return '<rect x="20" y="30" width="160" height="160" rx="16" fill="'+c.body+'"/><rect x="50" y="8" width="14" height="44" rx="7" fill="'+c.body+'"/><rect x="136" y="8" width="14" height="44" rx="7" fill="'+c.body+'"/><rect x="20" y="66" width="160" height="4" fill="'+c.detail+'" opacity=".6"/>';},
  face:{eyes:[[78,120],[122,120]],r:17,sw:5,mouth:[100,152]},arms:{l:[20,128],r:[180,128]},feet:{l:[70,190],r:[130,190]}});
Ring.add("ticket",{meaning:"a Fuji ticket: one piece of work",rot:[-4,100,100],body:function(c){return '<path d="M12 40 H188 V82 A18 18 0 0 0 188 118 V160 H12 V118 A18 18 0 0 0 12 82Z" fill="'+c.body+'"/><path d="M150 50 V150" stroke="'+c.detail+'" stroke-width="4" stroke-dasharray="9 8" stroke-linecap="round" opacity=".7"/>';},
  face:{eyes:[[58,100],[104,100]],r:17,sw:5,mouth:[81,134]},arms:{l:[12,136],r:[188,136]},feet:{l:[60,160],r:[120,160]}});
Ring.add("map",{meaning:"a map in Fuji: one outcome, folded and ready to unfold",body:function(c){return '<path d="M8 58 L52 38 L148 58 L192 38 V150 L148 172 L52 152 L8 172Z" fill="'+c.body+'"/><path d="M52 38 V152 M148 58 V172" stroke="'+c.detail+'" stroke-width="4" opacity=".6"/>';},
  face:{eyes:[[76,100],[124,100]],r:15,sw:5,mouth:[100,130]},arms:{l:[10,110],r:[190,100]},feet:{l:[70,160],r:[130,166]}});
Ring.add("clock",{meaning:"a timebox: a golf task with an alarm at the end",body:function(c){return '<circle cx="100" cy="112" r="70" fill="'+c.body+'"/><circle cx="48" cy="52" r="24" fill="'+c.body+'"/><circle cx="152" cy="52" r="24" fill="'+c.body+'"/><path d="M62 34 Q100 14 138 34" fill="none" stroke="'+c.body+'" stroke-width="8" stroke-linecap="round"/><path d="M74 168 L58 192 M126 168 L142 192" stroke="'+c.body+'" stroke-width="12" stroke-linecap="round"/><rect x="97" y="52" width="6" height="12" rx="3" fill="'+c.detail+'" opacity=".7"/>';},
  face:{eyes:[[78,108],[122,108]],r:16,sw:5,mouth:[100,140]},arms:{l:[32,124],r:[168,124]}});
Ring.add("folder",{meaning:"a folder: the three-maps-per-folder rule",body:function(c){return '<path d="M12 50 Q12 38 24 38 H78 L94 58 H176 Q188 58 188 70 V170 Q188 182 176 182 H24 Q12 182 12 170Z" fill="'+c.body+'"/><rect x="12" y="76" width="176" height="4" fill="'+c.detail+'" opacity=".6"/>';},
  face:{eyes:[[76,122],[124,122]],r:17,sw:5,mouth:[100,156]},arms:{l:[12,132],r:[188,132]},feet:{l:[68,182],r:[132,182]}});
Ring.add("compass",{meaning:"direction: the compass needle points at the destination",body:function(c){return '<circle cx="100" cy="108" r="88" fill="'+c.body+'"/><rect x="88" y="6" width="24" height="18" rx="6" fill="'+c.body+'"/><g transform="rotate(40 100 148)"><path d="M100 108 L112 148 L88 148Z" fill="#F58E84"/><path d="M100 188 L112 148 L88 148Z" fill="'+c.detail+'" opacity=".85"/></g>';},
  face:{eyes:[[76,86],[124,86]],r:16,sw:5},arms:{l:[14,112],r:[186,112]}});
Ring.add("scroll",{meaning:"the log: a scroll where every write appends a line",body:function(c){return '<rect x="34" y="30" width="132" height="140" fill="'+c.body+'"/><rect x="18" y="14" width="164" height="28" rx="14" fill="'+c.body+'"/><rect x="18" y="158" width="164" height="28" rx="14" fill="'+c.body+'"/><path d="M34 46 H166 M34 154 H166" stroke="'+c.detail+'" stroke-width="3" opacity=".6"/>';},
  face:{eyes:[[78,98],[122,98]],r:16,sw:5,mouth:[100,128]},arms:{l:[34,108],r:[166,108]},feet:{l:[76,186],r:[124,186]}});
Ring.add("pencil",{meaning:"writing: a pencil, a raw reflection put down",body:function(c){return '<rect x="50" y="8" width="100" height="32" rx="14" fill="#F58E84"/><rect x="50" y="36" width="100" height="112" fill="'+c.body+'"/><path d="M50 146 H150 L100 196Z" fill="'+c.body+'"/><rect x="50" y="36" width="100" height="9" fill="'+c.detail+'" opacity=".6"/>';},
  face:{eyes:[[78,92],[122,92]],r:15,sw:5,mouth:[100,124]},arms:{l:[50,100],r:[150,100]}});
/* places, body and world (drawn Nov 11 2026) */
Ring.add("range",{meaning:"all the maps together, a mountain range; Olympus",body:function(c){return '<path d="M0 200 V160 L36 84 L70 132 L110 18 L150 104 L174 58 L200 106 V200Z" fill="'+c.body+'"/><path d="M110 18 L90 58 L104 52 L112 62 L124 50Z" fill="'+c.detail+'"/>';},
  face:{eyes:[[84,142],[128,142]],r:16,sw:5},arms:{l:[22,150],r:[178,150]},feet:{l:[78,198],r:[128,198]}});
Ring.add("tent",{meaning:"base camp: a pause point on a climb",body:function(c){return '<path d="M100 12 L198 190 L2 190Z" fill="'+c.body+'"/><path d="M100 142 L128 190 L72 190Z" fill="'+c.detail+'"/>';},
  face:{eyes:[[78,114],[122,114]],r:15,sw:5},arms:{l:[44,120],r:[156,120]},feet:{l:[56,190],r:[144,190]}});
Ring.add("book",{meaning:"Shasta, the learning library; a study page",body:function(c){return '<rect x="36" y="10" width="128" height="178" rx="12" fill="'+c.body+'"/><rect x="50" y="170" width="114" height="10" rx="5" fill="'+c.detail+'"/>';},
  face:{eyes:[[78,70],[122,70]],r:17,sw:5},arms:{l:[36,104],r:[164,104]},feet:{l:[74,188],r:[126,188]}});
Ring.add("bubble",{meaning:"capture an idea in a WhatsApp message",body:function(c){return '<path d="M54 18 H146 Q192 18 192 64 V108 Q192 154 146 154 H92 L38 190 L50 150 Q8 142 8 108 V64 Q8 18 54 18Z" fill="'+c.body+'"/>';},
  face:{eyes:[[76,80],[124,80]],r:17,sw:5},arms:{l:[8,92],r:[192,92]},feet:{l:[96,154],r:[140,154]}});
Ring.add("kettle",{meaning:"the plateau: food, a break",body:function(c){return '<circle cx="100" cy="122" r="68" fill="'+c.body+'"/><rect x="70" y="42" width="60" height="18" rx="9" fill="'+c.body+'"/><circle cx="100" cy="32" r="12" fill="'+c.body+'"/><path d="M158 112 L192 66 L200 80 L170 148Z" fill="'+c.body+'"/><path d="M38 96 C-4 84 -6 164 42 152" fill="none" stroke="'+c.body+'" stroke-width="13" stroke-linecap="round"/>';},
  face:{eyes:[[76,124],[124,124]],r:16,sw:5},arms:{l:[36,134],r:[164,134]},feet:{l:[78,188],r:[122,188]}});
Ring.add("moon",{meaning:"Callisto, a moon; the 12:47 am night run",body:function(c){return '<defs><mask id="ringMoonMask"><rect width="200" height="200" fill="#fff"/><circle cx="154" cy="66" r="68" fill="#000"/></mask></defs><circle cx="100" cy="100" r="92" fill="'+c.body+'" mask="url(#ringMoonMask)"/><circle cx="30" cy="62" r="6" fill="'+c.detail+'"/>';},
  face:{eyes:[[34,122],[74,122]],r:13,sw:4.5},arms:{l:[12,130],r:[90,140]},feet:{l:[48,172],r:[84,184]}});
Ring.add("seedling",{meaning:"Udyaan, growth, a first step",body:function(c){return '<path d="M8 200 C8 150 50 128 100 128 C150 128 192 150 192 200Z" fill="'+c.body+'"/><rect x="94" y="54" width="12" height="80" rx="6" fill="'+c.body+'"/><path d="M100 98 C58 106 28 82 26 40 C70 36 98 60 100 98Z" fill="'+c.body+'"/><path d="M100 72 C104 30 142 6 182 12 C184 54 152 84 100 72Z" fill="'+c.body+'"/>';},
  face:{eyes:[[76,166],[124,166]],r:15,sw:5},arms:{l:[22,166],r:[178,166]},feet:{l:[74,198],r:[126,198]}});
Ring.add("laptop",{meaning:"a build session, working with Claude",body:function(c){return '<rect x="22" y="14" width="156" height="122" rx="14" fill="'+c.body+'"/><path d="M0 146 H200 L192 170 Q190 176 182 176 H18 Q10 176 8 170Z" fill="'+c.body+'"/><rect x="80" y="146" width="40" height="7" rx="3.5" fill="'+c.detail+'"/>';},
  face:{eyes:[[76,76],[124,76]],r:18,sw:5},arms:{l:[22,90],r:[178,90]},feet:{l:[70,176],r:[130,176]}});

/* ---------- templates: a few lines of settings each ---------- */
var CSS='.rg{position:relative;overflow:hidden;border-radius:4px;container-type:inline-size;line-height:1.05;color:'+INK+';--hand:"Gaegu","Comic Sans MS",cursive;--tall:"Amatic SC","Gaegu",cursive}'+
 '.rg *{box-sizing:border-box}.rg svg{display:block;width:100%;height:auto;overflow:visible}.rg .a{position:absolute}'+
 '.rg .h{font-family:var(--hand);font-weight:400;line-height:1.02}.rg .hb{font-family:var(--hand);font-weight:700;line-height:1}.rg .t{font-family:var(--tall);font-weight:700;line-height:.9;letter-spacing:.01em}'+
 '.rg .w span{display:block;width:max-content;max-width:100%}'+
 '.rg .bub{background:#fff;border:.5cqw solid '+INK+';border-radius:3.6cqw;padding:.45em .75em;position:relative}'+
 '.rg .btn{border:.45cqw solid currentColor;border-radius:3px;font-family:var(--hand);font-weight:700;padding:.35em .9em;display:inline-block}'+
 '.rg .stk{filter:drop-shadow(.5cqw 0 0 #fff) drop-shadow(-.5cqw 0 0 #fff) drop-shadow(0 .5cqw 0 #fff) drop-shadow(0 -.5cqw 0 #fff)}'+
 '.rg-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2cqw;padding:1.2cqw;background:'+INK+'}.rg-strip>.pn{position:relative;overflow:hidden;border-radius:3px;container-type:inline-size}'+
 '.rg-row{display:grid;gap:3%}.rg-row>.rg{border-radius:50%}.rg-row>.rg.sq{border-radius:22%}'+
 '.ring-mark{display:inline-block;width:1.6em;vertical-align:-.35em}.ring-mark svg{display:block;width:100%;height:auto;overflow:visible}';
function css(){if(typeof document==="undefined"||document.getElementById("ring-css"))return;var s=document.createElement("style");s.id="ring-css";s.textContent=CSS;document.head.appendChild(s);}
function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/"/g,"&quot;");}
function at(style,html){return '<div class="a" style="'+style+'">'+html+'</div>';}
// a stack of hand-lettered lines: strings are lines, {big:"WORD."} is the punchline, {mid:"..."} a bold line. Each line tilts a little.
function lines(ws,o){o=o||{};var R=rng(o.seed||7),sz=o.size||11,bs=o.big||27,ms=o.mid||13;
  return '<div class="w">'+ws.map(function(l,k){var tilt=((R()*5|0)-2)*.6,nudge=(R()*4|0)*1.1,st=' style="transform:rotate('+tilt+'deg);margin-left:'+nudge+'cqw';
    if(typeof l==="string")return '<span class="h"'+st+';font-size:'+sz+'cqw">'+esc(l)+'</span>';
    if(l.big)return '<span class="t"'+st+';font-size:'+bs+'cqw;margin-top:.6cqw'+(l.c?';color:'+col(l.c):'')+'">'+esc(l.big)+'</span>';
    return '<span class="hb"'+st+';font-size:'+ms+'cqw">'+esc(l.mid)+'</span>';}).join("")+'</div>';}
function plain(ws){return ws.map(function(l){return typeof l==="string"?l:(l.big||l.mid);}).join(" ");}
// a cast member: {who, at:"right:-10%;bottom:-12%", w:55 (percent of the piece's width), expr, pose, tilt, flip, body, eye, look, sticker}
function member(m,def){m=Object.assign({},def||{},m);var st=(m.at||"right:-8%;bottom:-12%")+";width:"+(m.w||55)+"%";
  return at(st,'<div'+(m.sticker?' class="stk"':'')+'>'+Ring.svg(m.who,m)+'</div>');}
function castOf(c){return (c.cast||[]).map(function(m){return m.who;}).join(", ");}

Ring.FORMATS={
 // 4:5 post: lines top-left, one big word, one character cropped by the edge
 post:function(c){return {ratio:"4/5",html:at("left:7%;top:5%;right:7%",lines(c.words,{size:c.size||11,big:c.bigSize||27,seed:c.seed}))+(c.cast||[]).map(function(m){return member(m,{at:"right:-8%;bottom:-14%",w:56});}).join("")};},
 // 9:16 phone story: lead lines, a huge word, a character rising from the bottom edge
 story:function(c){return {ratio:"9/16",html:at("left:9%;top:6%;right:8%",lines(c.words,{size:c.size||11,big:c.bigSize||40,seed:c.seed}))+(c.cast||[]).map(function(m){return member(m,{at:"left:6%;bottom:-14%",w:88});}).join("")};},
 // 4:5 stat card: one huge number, a label, a big word, a row of characters on the bottom edge
 stat:function(c){var n=c.cast||[];return {ratio:"4/5",html:at("left:7%;top:0%",'<span class="t" style="font-size:'+(c.numSize||70)+'cqw">'+esc(c.number)+'</span>')+
   at("left:50%;top:14%;right:5%",lines(c.words,{size:9,big:16,seed:c.seed}))+n.map(function(m,i){return member(m,{at:"left:"+(6+i*(88/n.length))+"%;bottom:-3%",w:Math.min(40,84/n.length)});}).join("")};},
 // 4:5 dark post: ink ground, a flat light wedge onto the message, a character in a light colour with ink eyes
 dark:function(c){var lc=col(c.light,"#fdbf68");return {ratio:"4/5",bg:INK,fg:lc,html:'<svg class="a" style="left:0;top:0;width:100%;height:100%" viewBox="0 0 100 125" preserveAspectRatio="none" aria-hidden="true"><path d="'+(c.wedge||"M56 62 L100 74 L100 125 L18 125Z")+'" fill="'+lc+'" opacity=".14"/></svg>'+
   at("left:8%;top:6%;right:8%",lines(c.words,{size:c.size||9,big:c.bigSize||24,seed:c.seed}))+(c.cast||[]).map(function(m){return member(m,{at:"right:-2%;bottom:-2%",w:62,body:lc,eye:INK,limb:lc});}).join("")};},
 // 16:9 slide that explains a method: kicker, big word, note, one character, up to three labelled points
 slide:function(c){var pts=c.points||[];return {ratio:"16/9",html:at("left:6%;top:8%;width:42%",lines(c.words,{size:4.6,big:13,mid:3.2,seed:c.seed}))+
   (c.note?at("left:6%;bottom:9%;width:36%;font-size:2.3cqw",'<span class="h">'+esc(c.note)+'</span>'):"")+
   (c.cast||[]).map(function(m){return member(m,{at:"left:46%;top:18%",w:27});}).join("")+
   pts.map(function(p,i){return at("left:76%;right:3%;top:"+(22+i*(56/Math.max(1,pts.length)))+"%;font-size:2.4cqw",'<span class="hb">'+esc(p[0])+'</span><br><span class="h">'+esc(p[1]||"")+'</span>');}).join("")};},
 // 3:1 banner: kicker and big word left, a parade of characters on a ground line right
 banner:function(c){var n=c.cast||[],x0=c.paradeAt||36,step=(96-x0)/Math.max(1,n.length);return {ratio:"3/1",html:at("left:4%;top:10%;width:"+(x0-4)+"%",lines(c.words,{size:3,big:12,seed:c.seed}))+
   '<div class="a" style="left:0;right:0;bottom:0;height:3.4%;background:'+INK+'"></div>'+
   n.map(function(m,i){return member(m,{at:"left:"+(x0+i*step)+"%;bottom:3.2%",w:Math.min(10,step*.86),tilt:i%2?4:-4});}).join("")};},
 // 16:5 comic strip, three panels: [{bg, say:["line",{big:"WORD"}], cast:[...]}]
 comic:function(c){return {ratio:"16/5",strip:true,html:(c.panels||[]).map(function(p,i){return '<div class="pn" style="background:'+col(p.bg,"#fdbf68")+'">'+
   at("left:6%;top:6%;right:6%",lines(p.say||[],{size:p.size||8.6,big:p.bigSize||24,seed:(c.seed||3)+i}))+(p.cast||[]).map(function(m){return member(m,{at:"left:40%;bottom:-8%",w:50});}).join("")+'</div>';}).join("")};},
 // 4:5 dialogue: two speech bubbles, two characters
 dialogue:function(c){var s=c.say||[],n=c.cast||[];return {ratio:"4/5",html:(s[0]?at("left:6%;top:6%;max-width:66%;font-size:6.4cqw",'<div class="bub h">'+esc(s[0])+'</div>'):"")+
   (s[1]?at("right:6%;top:31%;max-width:66%;font-size:6.4cqw;text-align:right",'<div class="bub hb">'+esc(s[1])+'</div>'):"")+
   (n[0]?member(n[0],{at:"left:3%;bottom:-5%",w:40}):"")+(n[1]?member(n[1],{at:"right:3%;bottom:-2%",w:42,flip:1}):"")};},
 // 1:1 sticker sheet: a title and the cast in white outlines with names
 stickers:function(c){var n=c.cast||[],cols=c.cols||(n.length<=3?n.length:Math.min(6,Math.ceil(Math.sqrt(n.length*2.5))));return {ratio:"1/1",html:at("left:6%;top:3%",'<span class="t" style="font-size:12cqw">'+esc(c.title||"THE CAST")+'</span>')+
   at("left:4%;right:4%;top:22%;bottom:3%;display:grid;grid-template-columns:repeat("+cols+",1fr);gap:4cqw 3cqw;align-items:end",n.map(function(m,i){
     return '<div style="text-align:center;transform:rotate('+(((i%3)-1)*5)+'deg)"><div class="stk">'+Ring.svg(m.who,m)+'</div><div class="hb" style="font-size:'+(22/cols)+'cqw;margin-top:.6cqw">'+esc(m.label||(m.who[0].toUpperCase()+m.who.slice(1)))+'</div></div>';}).join(""))};},
 // 4:5 app empty state: a resting character, a line, a big word, one button
 empty:function(c){return {ratio:c.ratio||"4/5",html:(c.cast||[]).map(function(m){return member(m,{at:"left:22%;top:8%",w:56,expr:"closed"});}).join("")+
   at("left:0;right:0;top:60%;text-align:center;font-size:8cqw",'<span class="h">'+esc(c.line||"")+'</span>')+at("left:0;right:0;top:69%;text-align:center;font-size:"+(c.bigSize||17)+"cqw",'<span class="t">'+esc(c.big||"")+'</span>')+
   (c.button?at("left:0;right:0;bottom:7%;text-align:center;font-size:4.6cqw",'<span class="btn">'+esc(c.button)+'</span>'):"")};},
 // avatars and app icons: a row of round (or rounded-square) heads, each on its own colour
 avatars:function(c){return {row:true,html:(c.cast||[]).map(function(m){return '<div class="rg'+(c.square?" sq":"")+'" style="aspect-ratio:1;background:'+col(m.bg,"#fdbf68")+'">'+at("left:12%;top:18%;width:76%",Ring.svg(m.who,m))+'</div>';}).join("")};}
};

/* Ring.piece(target, {format, bg, words|say|panels|points|number|line|big|button, cast:[...], alt, id, theme}) */
Ring.piece=function(target,c){css();var el=typeof target==="string"?document.querySelector(target):target;Ring.T=Object.assign({},c.tokens||{});
  var F=Ring.FORMATS[c.format||"post"];if(!F)throw new Error("Ring: format is one of "+Object.keys(Ring.FORMATS).join(", "));
  // one coral per piece: when the ball is cast (in any panel), every other character drops its coral detail
  var all=(c.cast||[]).concat.apply(c.cast||[],(c.panels||[]).map(function(p){return p.cast||[];}));
  if(c.coral!==true&&all.some(function(m){return m.who==="ball";}))all.forEach(function(m){if(m.who!=="ball"&&m.coral==null)m.coral=false;});
  var r=F(c),alt=c.alt||(plain(c.words||c.say||[])+(castOf(c)?" ("+castOf(c)+" with ring eyes)":""));
  if(r.row){el.className="rg-row "+(el.className||"");el.style.gridTemplateColumns="repeat("+((c.cast||[]).length)+",minmax(0,1fr))";el.innerHTML=r.html;}
  else{el.classList.add("rg");if(r.strip)el.classList.add("rg-strip");el.style.aspectRatio=r.ratio;el.style.background=r.strip?INK:col(c.bg,r.bg||"#fdbf68");if(r.fg)el.style.color=r.fg;el.innerHTML=r.html;}
  el.setAttribute("role","img");el.setAttribute("aria-label",alt);el.setAttribute("data-export",c.id||el.id||("ring-"+(c.format||"post")));
  warn(el,c);return el;};
// cheap clarity checks: one big word, at most three characters on a post, the big word short enough to be huge
function warn(el,c){var w=[],ws=c.words||[],bigs=ws.filter(function(l){return l&&typeof l==="object"&&l.big;});
  if(bigs.length>1)w.push("two big words: keep one");bigs.forEach(function(b){if(b.big.replace(/[^\w]/g,"").length>10)w.push("big word '"+b.big+"' over 10 letters: shorten it");});
  if((c.cast||[]).length>3&&["post","story","dark","dialogue"].indexOf(c.format||"post")>=0)w.push("more than three characters on a "+(c.format||"post"));
  (c.cast||[]).forEach(function(m){if(!Ring.cast[m.who])w.push("no character '"+m.who+"'");});
  el.dataset.inkWarn=w.join(" | ");if(w.length&&root.console)console.warn("Ring:",w.join(" | "));}

/* Touch: <i class="ring-mark" data-ring="loop" data-expr="closed" data-pose="wave" data-body="b2"></i> */
Ring.mount=function(scope){css();(scope||document).querySelectorAll("[data-ring]").forEach(function(el){var d=el.dataset;
  el.innerHTML=Ring.svg(d.ring,{expr:d.expr,pose:d.pose,body:d.body,eye:d.eye,tilt:d.tilt?+d.tilt:0,flip:d.flip!=null,look:d.look?+d.look:1});
  if(!el.classList.contains("ring-mark")&&el.tagName==="I")el.classList.add("ring-mark");});};

if(typeof document!=="undefined"){if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",function(){Ring.mount();});else setTimeout(function(){Ring.mount();},0);}
root.Ring=Ring;
})(typeof window!=="undefined"?window:this);
