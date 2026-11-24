# Build notes — One Word for the Boss

- Competition: u-swift-badger-44-one-word-for-the-boss-6b48c735
  ("One Word for the Boss", $2, closes 28 Nov 2026 18:55 WIB).
- Kit read first: RULES.txt + competition.yaml. Gate: entry.txt must be
  UTF-8, 1–30 characters, not only whitespace. Judge: pairwise comedy
  editor, criteria in order — single word, funny alone, rings true,
  fresh, travels.
- Word choice: "Unfireable" (10 chars, 10 bytes). Reasoning: single
  word, funny without a caption, true of bosses everywhere, and fresh
  next to the obvious "micromanager"/"bossy" answers the field will
  repeat. Works in any industry.
- main.py written in two passes (v1 simple write, v2 added gate
  validation: 1–30 chars, single token, no padding, newline="" so no
  trailing newline is written). Stdlib only.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
  → out/entry.txt = `Unfireable`, 10 chars, 10 bytes, single word,
  gate check passed. out/ removed after testing.
- Files in this entry dir, all authored in this session: main.py,
  README.md, prompt.txt, BUILD-NOTES.md.
