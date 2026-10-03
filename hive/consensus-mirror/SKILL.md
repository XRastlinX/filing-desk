---
name: consensus-mirror
description: "Produce a term, a slide treatment, and a two-voice video from a deep-dive. Use when the user wants a music-video style cut, a named handle, a Studio deck, or a shot list that must recover and stop before apply."
type: workflow
lifecycle: active
---

# Consensus Mirror — producer cut

Make the term before the picture. The picture follows the term. Consensus is the only lyric. This package is staged, not loaded.

```
operation_effect: STAGE_ONLY
authority_effect: NONE
automatic_execution: FORBIDDEN
```

## Lens

Work as a producer, not as a narrator. A term is a handle with act, object, and condition. A shot is that handle on screen and one sentence in a voice. If the sentence cannot be turned back into the handle, cut the shot.

## Workflow

1. Read SOURCE only. Charter, validator, hook, and action file are not sources.
2. Cut terms. For each recovered claim, write handle, act, object, condition, standing, and what it must not mean. Hype gets a term only as a refusal.
3. Write the treatment in six beats: status quo, facts, renames, refusals, shelves, stop. One handle per beat-slide.
4. Cast two voices. Witness, lower, says the sentence. Check, higher, says standing or refusal. Same words on title and status quo. Disagreement is a clash card, no winner.
5. Write the shot list in treatment order. Each shot: handle, duration, voice, line, what is not shown. Total under twelve minutes.
6. Run `scripts/consensus_mirror.py` on the treatment and the shot list. Forbidden token or missing stop line refuses.
7. Stop. Do not render audio, install a hook, or archive sources.

## Picture rules

Dark ground, bone type, one shelf color. No glow, no stock brains, no gears-as-primes, no dodecahedron. No sealed room shown as a modulus. No port shown as alive. No gendered figure as the authority.

## Non-claims

A landed check is not a finished video. A coined term is not a theorem. This skill does not close an open act.
