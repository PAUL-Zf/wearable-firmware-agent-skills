#!/usr/bin/env python3
"""Validate skill structure, pinned attribution, license, hashes and local Markdown links."""
from pathlib import Path
import hashlib
import json
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

def main():
    errors = []
    lock = json.loads((ROOT / 'sources.lock.json').read_text())
    names = set()
    for s in lock['skills']:
        name = s['name']
        folder = ROOT / 'skills' / name
        if name in names:
            errors.append(f'duplicate: {name}')
        names.add(name)
        try:
            text = (folder / 'SKILL.md').read_text()
            _, fm, _ = text.split('---', 2)
            meta = yaml.safe_load(fm)
            if set(meta) != {'name', 'description'} or meta['name'] != name:
                errors.append(f'{name}: invalid metadata')
            if not isinstance(meta['description'], str) or not meta['description'].strip() or len(meta['description']) > 1024 or '<' in meta['description'] or '>' in meta['description']:
                errors.append(f'{name}: missing description')
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
                errors.append(f'{name}: invalid name')
            if len(text.splitlines()) > 500:
                errors.append(f'{name}: entrypoint exceeds 500 lines')
            if s['commit'] not in text or s['license'] not in text or s['source_url'] not in text:
                errors.append(f'{name}: incomplete attribution')
            if json.loads((folder / 'SOURCE.json').read_text()) != s:
                errors.append(f'{name}: source record differs from lock')
            if not (folder / 'LICENSE').is_file() or (folder / 'LICENSE').stat().st_size < 500:
                errors.append(f'{name}: missing license text')
            if not re.fullmatch(r'[0-9a-f]{40}', s['commit']):
                errors.append(f'{name}: unpinned commit')
        except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
            errors.append(f'{name}: {exc}')
    actual = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
    if names != actual:
        errors.append('skill directories differ from lock')
    hashed = set()
    for f in lock['files']:
        p = ROOT / f['path']
        hashed.add(f['path'])
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != f['migrated_sha256']:
            errors.append(f"hash mismatch: {f['path']}")
    actual_files = {str(p.relative_to(ROOT)) for p in (ROOT/'skills').rglob('*')
                    if p.is_file() and p.name not in {'LICENSE','NOTICE','SOURCE.json'} and '__pycache__' not in p.parts}
    if actual_files != hashed:
        errors.append(f'untracked/obsolete content hashes: {sorted(actual_files ^ hashed)}')
    for p in ROOT.rglob('*.md'):
        if '.git' in p.parts:
            continue
        for link in re.findall(r'(?<!!)\[[^\]]+\]\(([^\s)]+)\)', p.read_text()):
            if link.startswith(('http:', 'https:', '#', 'mailto:')):
                continue
            path = link.split('#')[0]
            if not path or any(t in path for t in ('<', '{', '$')):
                continue
            if not (p.parent / path).exists():
                errors.append(f'{p.relative_to(ROOT)}: broken link {link}')
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"PASS: {len(names)} skills, {len(hashed)} content hashes, provenance, licenses and local links")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
