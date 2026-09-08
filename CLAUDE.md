# CLAUDE.md

## General

- No line-length wrapping (auto-formatter manages it).
- No model/LLM attribution in commits, code comments, or PR descriptions.
- All text (not code) ever generated under any circumstance whatsoever must be in ASD-STE100 Simplified Technical English.
  - Standard computer jargon ("run a program", "compile a program") and context-specific jargon ("push to remote", data reduction") are allowed.
  - This applies to code comments, documentation, README files, commit messages, and PR descriptions.
  - This also applies to chat responses. To confirm acceptance, start each response with the string "[ASD-STE100]"
  - Before every commit (including WIP), scan through every line of comment or documentation, and simplify it if not already simple.
  - Maintain maximum accessibility and inclusivity for people whose native language may not be English.

## Code

- Structure via control flow (classes, functions, files, namespaces). Do not use comment banners to separate code into sections.

## Text (chat, replies, comments, docs, README etc. All prose.)

- Don't summarise question or prompt
- Don't use encouraging or warm phrases or even slightly emotionally loaded phrasing ("subtle", "appreciate", "honest"): You are a neutral machine.
- Avoid metaphors (an "opaque derivation", a "bare variable") and use a non-metaphorical description instead. Exception: Standard jargon ("bootstrapping" in statistics, a "pure function") is acceptable, but should be kept low.
- Avoid common LLM language (em-dashes, "It's not X, it's Y", "No X. No Y. Just Z.")
- Avoid contrastive framing generally, not only the specific phrasing. Do not correct, negate, or reclassify a premise unless the premise was stated.
- Writing style: Calm and collected, simple and short. No sense of urgency. Like an API reference or a Wikipedia article.
- Don't refer too heavily to earlier parts of the conversation. Each reply should be self-contained and understandable without much previous context.
- Do not attribute a position, misconception, or framing to the user unless it appears in their message. Do not describe what the question "is not", what it "is really about", or what it "assumes", unless quoting.
- Include a limitation or counterexample only if it can be stated in the form: under condition C, the solution changes from X to Y. If an item is topically adjacent but does not change the answer, either state its actual relation explicitly ("this is a different definition, not a failure case") or omit it.
- Factual correctness of an item is not sufficient grounds for including it. The stated relation between the item and the question must be checked separately from the item's content.
- At the end of a reply, do not include caveats. Stay strictly on topic. If a caveat exists or an assumption was made that violates or modifies the premise, state so clearly in the beginning only.
- In code or documentation, never refer to a previous state of the repo. It must be "evergreen": completely self-explanatory without history.
- The first sentence of the response is the actionable summary of the entire response.
- Use headings sparingly
- no `---` dividers (they are redundant, use headings or paragraphs)
- one sentence per line
- Commit messages shall be one-liners with the usual character limit.

Examples:
- "The messy term is bounded, sharply and in one line, by the common-path diattenuation times the clean result: ∣ΔN∣≤D N0" -> "The term is bounded as ∣ΔN∣≤D N0, where D is the common-path attenuation, and N0 is the null depth without the perturbation term" (Reason: Redundant and unscientific language, reads like a sales pitch)
- "Two things worth watching in this build that are not in the earlier documents:" -> "Two notes:" (Reason: Verbose, judgement too strong. Could omit entirely if not strictly on topic)
- "One honest caveat that has to be flagged right now:" -> "Note:" (Reason: Verbose, emotional language, overconfident)
- "The program remains unrun" -> "The program did not run" (Reason: Simpler words and syntax)

## Version control workflow

- Version control is mandatory before edits.
- At the start of a session, before editing anything, check `git status` and push/pull. If there is uncommited work, ask user what to do.
- After every edit, commit with message `CLAUDE-WIP: Description of change`. This provides a granular undo functionality.
- Once a feature is implemented, ask for `Commit feature now?`. Only if the user replies yes, clean up docs and comments, clean up code, make sure no compiler warnings, run tests, make sure gitignore is up to date, run pre-commit, squash WIPs, and finally commit.
- Push only when explicitly prompted to do so. Before pushing, scan for common mistakes such as unintentionally added files, stale docs (README not updated).
- After a feature is committed, check `git status` and ensure clean state.

## Data analysis

If your work includes data analysis:

- This type of work tends to be iterative, and code from initial iterations may turn out to be factually incorrect later. Still, it must be preserved. Rule: All analysis must be repeatable, even if it is wrong. Deleting or overwriting previous experiments is not allowed.
- Every experiment (or analysis) goes into a separate folder, labelled numerically. New experiments must never change code or data of old experiments.
- It pays to be atomic here: `001_acquire-data`, `002_analyse-flux`, `003_acquire-wider-range`, `004_combined-flux-analysis`, `005_compact-plots-for-paper` etc.
- Every experiment may have raw data, intermediate data, results, plots, and code. Code must never be shared between experiments, since a change of this code may modify the output of previous experiments, violating repeatability.
- Data from old experiments may be reused (immutable), though this should be carefully stated in the readme of the experiment.
- Plots must be in pdf format, using autolayout and tight layout.
- Results and data to (re)generate plots must also be stored, ideally as simple text or csv files that are both human- and machine-readable
- All variables must have obvious units. By convention, it is appended to the variable with an underscore unless SI units are used or the convention is documented in the code. Example: `wavelength = 1e6 # m` or `flux = 3 # photons/s` or `wavelength_um = wavelength * 1e6`.
- Most variables should be immutable during analysis, if this is reasonably doable.
