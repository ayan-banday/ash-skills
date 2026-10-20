---
name: build-ticket-matt
description: "[Matt] How do I get one decided ticket built without Claude redesigning it? Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Call the Skill tool with "build:test-first-matt" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, call the Skill tool with "build:review-code-matt" to review the work.

Commit your work to the current branch.
