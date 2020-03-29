---
title: "Relax PP"
reference_version: 857b60c378a463c68431822860a6c18f
---
**Ripple now has support for Relax PP!** We have divided all leaderboards (global, country and per-beatmap) in two sections: **Classic and Relax**.

- **Classic** is the normal leaderboard system, where Relax and Autopilot are not ranked
- **Relax** has support for Relax and Autopilot PP on osu!standard, osu!taiko and osu!catch, with a tweaked PP system.

In other words, all PP you gain in Relax mode will not affect your Classic mode stats, so if you don't like this feature, you can ignore it entirely and it won't affect your rank.

## How to switch between Classic and Relax in-game
By default, all in-game leaderboards will display classic mode scores. Relax scores have their own leaderboard, separate from the classic one.

If you submit a score with Relax or Autopilot, it'll be submitted but it'll be visible **only on the relax leaderboard**. You can switch between classic and relax by **sending a message containing `!relax` or `!rx` anywhere in the chat.** Don't worry about spamming, these messages are visible only to you. If you're not multiplaying or being spectated, you'll immediately see your leaderboard reloaded, otherwise click on "Global leaderboard" to reload it. Your in-game stats will regard relax mode as well.

**Typing `!relax` again will switch you back to classic mode.** You can also use `!relax on` and `!relax off`/`!classic` if you want to explicitly switch to Relax or Classic respectively.

## How to view Relax leaderboards & profiles on the website
If you want to see the global or country leaderboards in Relax mode, go to our [leaderboard](/leaderboard) page and click the "Relax" button. Click to "Classic" to switch back to classic mode.

The same thing applies for user profiles and beatmap pages, click the "Classic" or "Relax" button under the game modes to switch between the two submodes. All stats and scores displayed on the profile will be relative to the currently selected mode.

## PP System
The osu!standard relax PP system was developed by [Lithium](/u/1955) by tweaking the values from the classic PP system, which is the same one osu! uses. This was needed to avoid gaining too many performance points by playing stream maps with relax or jump maps with autopilot. The PP system on osu!taiko and osu!catch is the same as the classic one.

You can see how many PP a map is worth by sending `/np` to [FokaBot](/u/999), and then `!with RX`. If you want to add additional mods, you can append them at the end, for example `!with RXDTHD`.

The Relax PP system may be subject to future changes, if you have any suggestions, please let us know in our [Discord server](https://discord.ripple.moe).
