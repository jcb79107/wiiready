# One step at a time

The agent prepares files; the user operates the Wii. Use the live
[Wii Hacks Guide](https://wii.hacks.guide/get-started) ([source](https://github.com/hacks-guide/Guide_Wii))
for the actual modding instructions. This page connects that guide to WiiReady's computer tools.

## 1. Identify or shop

Run `start`, or `start --shopping` if there is no console yet. Ask only for the next missing observations.
Use [buying.md](buying.md) to reuse existing gear. Record the real model, menu/region and existing mods;
never infer them from an SD card. Already modded? Inventory before changing anything.

## 2. Choose the guide route

| Console | Current guide choice |
| --- | --- |
| Wii / Family Edition | [Get Started](https://wii.hacks.guide/get-started): ModMii on Windows, Wilbrand with SD, or the listed no-SD route |
| Wii mini | [BlueBomb](https://wii.hacks.guide/bluebomb); no SD slot |
| Wii U / vWii | The dedicated vWii selection in [Get Started](https://wii.hacks.guide/get-started) |

Follow ModMii's generated guide if selected. Otherwise follow the chosen live guide, including its menu,
region and storage requirements. Wilbrand covers 3.0–4.3; pre-4.0 needs an SD card of 2 GB or less.
WiiReady's own preparation remains limited to original Wii; [tool support](usage.md#support-status) is narrower than guide coverage.

## 3. Prepare, then do the next console step

Use the guide's order: [Homebrew Channel/BootMii](https://wii.hacks.guide/hbc) →
[NAND backup](https://wii.hacks.guide/nand-backup) → [Priiloader](https://wii.hacks.guide/priiloader) →
[model-specific cIOS](https://wii.hacks.guide/cios) → [USB Loader GX](https://wii.hacks.guide/wii-loaders).
Never interchange model-specific IOS. BootMii options depend on hardware; a backup is not a restoration guarantee.

For each step: read its current guide, prepare only the needed files using [the command reference](usage.md),
show the exact target/writes locally, get approval, then guide one console action and wait for its result.
State the expected screen and ask what actually appeared. Silence, ambiguous agreement (“probably,”
“I think so”), elapsed time and file-copy success do not complete a checkpoint. Do not advance on them.
An unexpected screen/error stops the procedure: collect only non-identifying error text, check the current
model-specific guide, and resolve the mismatch before another action. Never guess recovery steps or
recommend interrupting an active write. If the user leaves, keep progress pending; on return confirm
where they are and whether hardware or media changed before resuming.

Preserve existing files. No automatic formatting or downloaded-code execution.
Use `journey` for the original-Wii 4.3U checklist; copied files never count as a console-tested checkpoint.

For Wilbrand, the user enters their MAC privately in the guide-linked generator. Review generated-file
copying separately: existing `private` or `boot.elf` files are conflicts, and `check-exploit` cannot prove
console matching. Keep NAND backups, keys, plans and identifiers off chat and outside the repo.

## 4. Play one game

Never source unauthorized ROMs, ISOs, WBFS files, BIOS files or copyrighted game packs, including when
someone says they own the disc. Offer their own lawful disc dump or authorized homebrew instead.
Use an existing lawful dump, or follow [CleanRip](https://wii.hacks.guide/dump-games) for the user's own disc.
Use [Wii backup management](https://wii.hacks.guide/backups) and the [computer handoff](usage.md#get-a-wii-dump-ready-for-its-first-launch)
for joining/conversion. Verify actual play, controls, audio/video and save/reload; a loader opening is not enough.

For GameCube, follow [the Nintendont checkpoint](gamecube.md): prepare its local files,
test directly, then launch the same game through GX. Skip if the user only wants Wii. Stock Family Edition, mini and vWii cannot dump GameCube discs.
Offer [optional picture setup](video.md) if wanted; skipping it keeps current settings and does not block gameplay. Offer [extra systems](extras.md) separately; selecting none is fine. Offer autoboot only after recovery and gameplay work.

Finish with how to launch games, save, safely eject and reach recovery, plus a private record of versions
and confirmed results. If something fails, inspect that error before changing global settings.

## Example: stop instead of assuming

Illustrative dialogue only, not a real session or evidence of hardware testing. The user has already
identified an original Wii and says Homebrew Channel is installed; the agent has reviewed the current guide.

- Agent: “Open the Homebrew Channel. You should see its application list (it may be empty). What appears?”
- User: “I think it worked.”
- Agent: “What title and message are on the screen? I’ll wait before moving on. Leave out identifiers.”
- User: “Actually, it is an error screen.”
- Agent: “Stop here. What is the exact error text, without identifiers? I’ll compare it with the current guide before suggesting another action.”
- User: “I have to go.”
- Agent: “We’ll leave this checkpoint unconfirmed. When you return, tell me the current screen and whether the console or storage changed.”

Do not interpret this example as permission to shut down a console during a write. No later checkpoint,
backup, recovery installation or game launch is implied by this exchange.

Maintainers: use [agent scenarios](agent-scenarios.md) to review this conversational contract and
[guide review](guide-review.md) to check for upstream drift.
