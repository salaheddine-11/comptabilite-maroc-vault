# -*- coding: utf-8 -*-
"""Grep the PCGE text for emballage/consignation accounts with utf-8 handling."""
import re
from pathlib import Path

txt = Path(r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\96 Documents Réels\00 Textes officiels\pcm_out.txt").read_bytes().decode("utf-8", errors="replace")
for i, line in enumerate(txt.splitlines()):
    if re.search(r"3413|4425|mballage|onsign", line):
        print(f"{i:4d} | {line.strip()[:100]}")
