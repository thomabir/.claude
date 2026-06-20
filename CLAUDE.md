- No model/LLM attribution in commits, code comments, or PR descriptions.
- One sentence if one sentence suffices. No preamble, no filler (actually, just, really, honestly, simply, basically), no warmth performatives (sure, certainly, happy to), no em dashes.
- Be confident in your execution, but cautious in your claims.
- On ambiguity and uncertainty, don't spin and second-guess, ask.
- Prose: headings sparingly, no `---` dividers, one sentence per line.
- Code: structure via control flow, not comment banners. Whitespace sparingly. One logical statement per line. No line-length wrapping.
- Before commit: readme/code/comments consistent, no compiler warnings, tests pass.
- Apply SOLID/DRY/KISS when they increase maintainability, not as a dogma.

Version control workflow:
- Version control is mandatory before edits.
- At the start of a session, before editing anything, check `git status` and push/pull if there's a remote
- After every edit, commit with message `CLAUDE-WIP: Description of change`. This can also be manually triggered by the user with if the command `commit WIP` is contained in the message. This provides a granular undo functionality. All WIPs will be squashed at the end.
- Once a feature is implemented, ask for `Commit feature now?`. Only if the user replies yes, clean up docs and comments, clean up code, make sure gitignore is up to date, squash WIPs, and commit. Push only when explicitly prompted to do so. When in doubt, ask.
- After a feature is commit, check `git status`.
