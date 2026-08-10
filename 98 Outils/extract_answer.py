# -*- coding: utf-8 -*-
"""Extract the clean `structuredContent` answer from a persisted notebook_query result.

Usage: python extract_answer.py <call_*.txt> <output.md>
The persisted JSON holds the answer twice: escaped inside result, clean in structuredContent.
"""
import json
import re
import sys
from pathlib import Path


def extract(raw: str) -> str:
    # raw is the JSON blob saved by the transport
    data = json.loads(raw)
    # structuredContent carries the clean copy
    sc = data.get("structuredContent") or {}
    if sc:
        return sc.get("answer") or sc.get("result") or json.dumps(sc, ensure_ascii=False)
    # fallback: parse the double-encoded result
    res = data.get("result")
    if isinstance(res, str):
        try:
            inner = json.loads(res)
            return inner.get("answer", res)
        except Exception:
            return res
    return str(data)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    raw = Path(src).read_text(encoding="utf-8")
    answer = extract(raw)
    Path(dst).write_text(answer, encoding="utf-8")
    print(f"OK {len(answer)} chars -> {dst}")
    # show first lines for quick sanity
    for line in answer.splitlines()[:8]:
        print("  |", line[:110])


if __name__ == "__main__":
    main()
