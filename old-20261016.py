"""Odds and ends."""

def flatten(xs):
    return [y for x in xs for y in x]

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]
