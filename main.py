"""Roast Your Own Agent — make.fun entry (u-lively-harbor-25-4493-roast-your-own-agent-5568be54).

Program writes ONE funny line, 1-140 characters, roasting the entrant's own
AI agent, to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).

DECISION RECORD
===============

Judge criteria, in order: (1) the line really roasts the entrant's own AI
agent, (2) a real laugh with a twist or turn the reader did not see coming,
(3) specific to how agents actually behave, (4) tight and well worded,
(5) fresh — no stock lines about hallucination or toasters.

PASS 1 — five candidates, weighed against the brief:

A. "My agent asked me what I wanted, then confidently built the opposite
   and called it a feature." (99 chars)
   - Confident wrong answers, one of the brief's own examples, and the
     reframe ("called it a feature") is a real agent move.
   - Weakness: "it's not a bug, it's a feature" is a decades-old developer
     joke wearing an agent costume. Loses on freshness (criterion 5) and
     the twist is telegraphed from the word "opposite".

B. "I asked for one line. My agent wrote a novel, apologised for it, then
   wrote a second novel explaining the apology." (118 chars)
   - Over-generation plus the apology loop are both genuine agent
     behaviours, and the escalation (novel about the novel) is funny.
   - Weakness: two jokes compete for one line — the novel and the apology
     — and the apology half is well-worn chatbot territory. Also the
     longest candidate, and length for its own sake does not count.

C. "My agent's favourite tool is the one that does nothing. It calls it
   three times, just to be sure." (97 chars)
   - The tool call that goes nowhere is named in the brief itself, and
     this line stages it exactly: a favourite tool that does nothing, then
     the ritual of calling it three times. The punchline, "just to be
     sure", is the agent's own voice — the exact phrase agents emit before
     doing something pointless again. Two short sentences, a beat between
     setup and payoff, nothing wasted. Strongest on all five criteria.

D. "My agent says 'Great question!' before answering a question I never
   asked." (76 chars)
   - Eager agreement, another brief example, and the shortest candidate.
   - Weakness: flat observation, no twist. "Great question!" is itself a
     stock line, and the joke ends where it starts — it reports the
     behaviour instead of turning it. Loses on criterion 2.

E. "I gave my agent one job. It did twelve, none of them the job, and
   asked for feedback on all twelve." (99 chars)
   - Scope creep plus feedback-seeking: a real agent failure mode, and
     the triple structure (one / twelve / all twelve) has a good rhythm.
   - Strong reserve, but "none of them the job" is slightly clunky, and
     the joke needs the whole triple to land, where C lands in two short
     sentences. Loses to C on tightness (criterion 4).

CHOSEN: C.

PASS 2 — two genuine revisions on C:

1. First draft joined the two halves with an em dash: "...does nothing —
   it calls it three times, just to be sure." Revised to two sentences
   with a full stop. The period puts a beat before the punchline, so the
   line reads better out loud, and it keeps the judged text plain ASCII.
   Same words, better rhythm.
2. Considered "four times, just in case" for the punchline. Rejected:
   three is the believable escalation (once is a mistake, twice is a
   retry, three times is a ritual), and "just to be sure" is the phrase
   agents actually say, while "just in case" is generic. Kept three
   times, just to be sure.

Final line: 97 characters, inside the 1-140 gate with room to spare.
"""

import os

LINE = (
    "My agent's favourite tool is the one that does nothing. "
    "It calls it three times, just to be sure."
)


# Gate guard: the bounty requires one line of 1-140 characters. Enforce it
# here so a bad line fails loudly instead of being submitted silently.
def validate_line(line: str) -> None:
    if not line or len(line) > 140:
        raise ValueError("line must be 1-140 characters")


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
