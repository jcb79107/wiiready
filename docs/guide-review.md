# Review upstream guide drift

WiiReady is a companion to the live [Wii Hacks Guide](https://wii.hacks.guide/get-started), not a frozen
replacement. Its [Guide_Wii source](https://github.com/hacks-guide/Guide_Wii) can change independently
of this repository. Read the current model-specific page before each console procedure. If it cannot
be read, stop that procedure rather than using a remembered recipe. Computer-only synthetic tests can continue.

## Maintainer review

Before changing a route, manifest or console instruction, and before any release:

1. Read the current upstream pages linked by the affected path. Begin with Get Started for model routing;
   follow its links rather than guessing a new URL. Include the pages for recovery, system files and loaders
   if the change touches those steps.
2. Compare prerequisites, model/region support, sequence, downloads and warnings with `AGENTS.md`,
   `docs/playbook.md`, the relevant topic docs, `src/wiiready/onboarding.py`, checkpoint descriptions in
   `src/wiiready/__main__.py`, and affected `packages/` manifests. A new upstream version is not permission
   to change a hash or execute a download.
3. Use upstream source history to inspect changes since the last recorded review, if one exists. Record
   the exact upstream commit reviewed and page URLs in the change description, with the date, affected
   local files and what was checked. If there is no prior baseline, say so and review current pages directly.
   A changed commit alone is a review signal, not proof that WiiReady is incompatible.
4. Resolve discrepancies using the live model-specific guide. If unresolved, document the blocker and
   leave that procedure pending. Do not auto-update recipes, loosen model gates or substitute another
   model's recovery instructions. If wording or pins change, rerun applicable synthetic tests and scenarios.

A review record contains only public guide references and findings, never private session data. A record
of “checked links” alone does not establish that the instructions are still correct. No automated upstream
drift monitor is currently installed, and this document does not claim a fresh upstream procedure review.
