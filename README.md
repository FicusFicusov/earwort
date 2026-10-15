# Earwort

Earwort trains your ear, for free, in your browser. It has two trainers: one for mixing engineers, one for
musicians. You need no account. Nothing tracks you, and nothing leaves your device: the page makes every sound
itself.

**Try it:** <https://ficusficusov.github.io/earwort/>

| Frequencies · EQ | Intervals & scales |
| --- | --- |
| ![The EQ trainer: grass grows into a hill where the band was boosted](docs/frequencies.jpg) | ![The intervals trainer: each note grows as a bamboo stalk](docs/intervals.jpg) |

## Frequencies · EQ

[`index.html`](index.html) teaches you to hear EQ: which band changed, and how. It works like SoundGym,
Quiztones or TrainYourEars, and costs nothing.

- **Frequency.** A band is boosted on pink noise. Pick it. Hold **Bypass** to hear the sound without the EQ.
- **Boost / cut.** Was the band boosted or cut, and where?
- **A / B.** You get two versions. Which one has the EQ?
- **Match.** Turn a knob until your band sounds like the reference.
- **Width (Q).** How wide is the boosted band?
- **Free sweep.** Turn the EQ yourself. Nothing is scored.

Easy has 6 octave bands at ±15 dB. Medium has 9 octave bands at ±10 dB. Hard has 26 third-octave bands at ±6 dB.
You can train on pink noise, white noise, a sine tone or your own track.

Each band has a sound of speech to remember it by. 250 Hz sounds like "oo" in *boot*, 1 kHz like "ah" in
*father*, 4 kHz like "ee" in *see*. The reference card lists them all.

**The screen is a night meadow, laid out like an EQ:** low frequencies on the left, high on the right. When you
answer, the grass grows into the filter you heard. A boost raises a hill; a cut mows a hollow. The width of the
hill is the width of the band. A stake marks your guess. Each correct answer in a row lights a firefly, and a miss
sends them all away.

## Intervals & scales

[`intervals.html`](intervals.html) trains your ear for music. It works like Functional Ear Trainer or EarMaster,
and costs nothing.

- **Degrees.** A cadence sets the key, then one note sounds. Name its scale degree. This is the main exercise.
- **Melodic.** Two notes, one after the other. Name the interval.
- **Harmonic.** Two notes at once. Name the interval.
- **Wider?** Which of two intervals is wider? You need no theory for this one.
- **Scales.** From major and minor up to fourteen scales and modes, Phrygian dominant included.
- **Chords.** From major and minor up to twelve chords with sevenths.
- **Dictation.** A short tune plays. Write it down in scale degrees.
- **Free play.** Play a keyboard over a tonic drone, in any key and scale.

Name the notes with letters, scale degrees (1 ♭3 5) or movable-do solfège. Letter names follow the key: the 4th of
A♭ major is D♭, not C♯. After a correct answer the note can resolve to the tonic, so your ear learns the pull of
each degree. The trainer brings back the items you miss most, and the **Ear map** shows your accuracy on each one.

**The screen is a bamboo grove in the mist.** Each note grows as a stalk. Each joint of a stalk is one semitone,
so you can count an interval in joints. The golden stalk is the tonic, or the root. A run of correct answers
thickens the grove behind.

## Keyboard

| Key | Frequencies | Intervals & scales |
| --- | --- | --- |
| Space | play or stop | play |
| K | | the second play button: note only, slower, one by one |
| 1–9 | answer | answer |
| → or N | next | next |
| A, B | play A or B | first or second (Wider?) |
| Enter, Backspace | | check, erase (Dictation) |

## Run it yourself

Each trainer is one HTML file, with its pixel font inside. Open `index.html` or `intervals.html` in a browser, or
serve the folder from any static server. On a phone, open the file in Safari or Chrome: a file preview can't run
the buttons.

A page remembers one thing, in your browser only: the light or dark theme.

## For developers

- Both pages share their look and their common code: icons, theme, knobs, the pixel screen, the support dialog.
  Edit the shared parts in `index.html`, between the `=== shared ===` and `=== this page ===` banners. Then run
  `python3 tools/sync_shared.py` to copy them into `intervals.html`.
- `tools/build_font.py` builds `fonts/earwort-mono.woff2`. It takes Departure Mono, draws the music signs the font
  lacks (♯ ♭ ♮ ✓ ✗) on its pixel grid, and keeps only the characters the pages use. It needs `fonttools` and
  `brotli`.
- `tools/embed.py` puts that font into both pages as base64.

## Credits

- Font: [Departure Mono](https://departuremono.com) by Helena Zhang, under the SIL Open Font License 1.1
  ([`fonts/OFL-DepartureMono.txt`](fonts/OFL-DepartureMono.txt)). Earwort uses a modified copy, Earwort Mono.

## Support

Earwort is free and will stay free. If it helps you, press **Support** on either page.
Contact: [Telegram channel](https://t.me/ficusficusov) · iambemoli@gmail.com

## License

Earwort is free software under the GNU General Public License, version 3 only ([`LICENSE`](LICENSE)).
You may use, study, share and change it. If you share a changed version, share its source under the same license.
The font keeps its own license, the SIL Open Font License 1.1.
