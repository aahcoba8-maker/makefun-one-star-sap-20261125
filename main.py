"""One Star, Written in Sap — a one-line 1-star review by a houseplant.

The plant's grievance is the centre: its human waters it on a schedule
found online, for a plant he has never actually met — then the turn:
it is a fern, not a cactus. Plant's-eye detail (watering schedule,
species mix-up), a genuine review shape, and no stock wilting/drama
phrases, per the judge brief.
"""

import os

TEXT = "★☆☆☆☆ My human waters me on a schedule he found online, for a plant he has never actually met. I am a fern, not a cactus, Greg."


def main():
    # Self-gate mirroring the kit's sealed scorer: 1-279 UTF-8 chars, not
    # only white space.
    assert 1 <= len(TEXT) <= 279, "entry must be 1-279 characters"
    assert TEXT.strip(), "entry must not be only white space"
    assert "\n" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)
    print("chars:", len(TEXT))


if __name__ == "__main__":
    main()
