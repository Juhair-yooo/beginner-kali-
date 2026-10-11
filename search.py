#!/usr/bin/env python3
"""
kali-cmd-finder — type what you want to do, get the command for it.

Usage:
    python3 search.py                 # interactive mode
    python3 search.py "scan ports"    # one-shot query
"""

import json
import os
import sys

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commands.json")


def load_entries():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def score_entry(entry, query_words):
    """Simple relevance score: count query-word hits across tool/category/
    description/keywords, weighted a bit so tool-name / keyword hits count
    more than incidental description hits."""
    haystacks = {
        "tool": entry.get("tool", "").lower(),
        "category": entry.get("category", "").lower(),
        "description": entry.get("description", "").lower(),
        "keywords": " ".join(entry.get("keywords", [])).lower(),
    }
    score = 0
    for word in query_words:
        if word in haystacks["tool"]:
            score += 3
        if word in haystacks["keywords"]:
            score += 3
        if word in haystacks["category"]:
            score += 2
        if word in haystacks["description"]:
            score += 1
    return score


def search(entries, query):
    query = query.strip().lower()
    if not query:
        return []
    query_words = [w for w in query.replace("-", " ").split() if w]
    scored = []
    for entry in entries:
        s = score_entry(entry, query_words)
        if s > 0:
            scored.append((s, entry))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [entry for _, entry in scored]


def print_entry(entry):
    print(f"\n=== {entry['tool']}  [{entry['category']}] ===")
    print(entry["description"])
    for c in entry["commands"]:
        print(f"  $ {c['cmd']}")
        print(f"    -> {c['desc']}")


def print_results(results, query):
    if not results:
        print(f'\nNo matches for "{query}". Try a different word (e.g. "scan", "crack", "wifi", "sniff").')
        return
    for entry in results[:8]:
        print_entry(entry)
    if len(results) > 8:
        print(f"\n...and {len(results) - 8} more matches. Try a more specific query to narrow it down.")


def list_categories(entries):
    cats = sorted(set(e["category"] for e in entries))
    print("\nCategories:")
    for c in cats:
        print(f"  - {c}")


def main():
    entries = load_entries()

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print_results(search(entries, query), query)
        return

    print("Kali Command Finder — type what you want to do (e.g. 'scan a network', 'crack a hash', 'sniff traffic').")
    print("Commands: 'categories' to list categories, 'quit' to exit.\n")
    while True:
        try:
            query = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not query:
            continue
        if query.lower() in ("quit", "exit", "q"):
            break
        if query.lower() in ("categories", "category", "list"):
            list_categories(entries)
            continue
        print_results(search(entries, query), query)


if __name__ == "__main__":
    main()
