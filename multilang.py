#!/usr/bin/env python3
# Convert input markdown to single-language output.

import re
import sys
import fileinput

# Supported langs. xx is for comments.
LANGS = ("en", "ja", "xx")

def clean_line(line):
    """Remove Notebook formatting if present."""
    # notebook lines look like: "text\n", for non-block-finals, or
    # like "text" for block finals
    sline = line.strip(' ",')
    if sline[-2:] == r"\n":
        return sline[:-2]
    return sline

try: 
    #TODO proper arg / help
    lang = sys.argv[1] 
    infile = sys.argv[2]
except:
    print("usage:")
    print(f"    {sys.argv[0]} [lang] [fname]")
    sys.exit(1)

# this is the symbol we look for
sigil = f":{lang}"
ignore_sigils = [f":{ll}" for ll in LANGS if ll != lang]

KEEP = False # for blocks
for line in fileinput.input([infile]):
    # Note we can't strip the left due to markdown code indent
    line = line.rstrip()

    # if in a block, keep everything until blank line if lang is right
    cline = clean_line(line)
    if KEEP:
        if cline == ":end":
            KEEP = False

        if KEEP == sigil:
            print(line)

        continue

    # if the line is just a sigil, we entered a block
    if sigil == cline or cline in ignore_sigils:
        KEEP = cline 
        print()
        continue

    # If flagged with another lang, discard
    ignore = False
    for ss in ignore_sigils:
        if ss in line:
            ignore = True
    if ignore:
        continue

    # if line is marked, remove the sigil
    # (extra spaces should be filtered out)
    if sigil in line:
        line = line.replace(sigil, "")

    # remove unnecessary section meta data
    line = re.sub(r"{#.+}", "", line)

    # finally print the kept line, which may have been marked or unmarked
    print(line)

