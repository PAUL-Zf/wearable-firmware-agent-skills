#!/usr/bin/env python3
"""Copy selected skill packages with provenance and licenses; never overwrite."""
from pathlib import Path
import argparse
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skills', nargs='*')
    parser.add_argument('--dest', type=Path)
    parser.add_argument('--group', action='append', default=[])
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()
    records = json.loads((ROOT / 'sources.lock.json').read_text())['skills']
    by_name = {s['name']: s for s in records}
    groups = {s['group'] for s in records}
    if args.list:
        for s in records:
            print(f"{s['name']}\t{s['group']}\t{s['license']}")
        return 0
    if not args.dest or not (args.skills or args.group):
        parser.error('provide --dest and skill names and/or --group')
    if set(args.skills) - set(by_name):
        parser.error('unknown skills: ' + ', '.join(sorted(set(args.skills) - set(by_name))))
    if set(args.group) - groups:
        parser.error('unknown groups: ' + ', '.join(sorted(set(args.group) - groups)))
    names = set(args.skills) | {s['name'] for s in records if s['group'] in args.group}
    # These integration skills refer to companion knowledge and project skills by name.
    cmsis_groups = {'CMSIS 与 bring-up', 'CMSIS MCP 集成'}
    if any(by_name[n]['group'] in cmsis_groups for n in names):
        names |= {s['name'] for s in records if s['group'] in cmsis_groups}
    # Selected local Markdown cross-links are hard package dependencies when copied standalone.
    import re
    while True:
        needed = set(names)
        for n in names:
            folder = ROOT / 'skills' / n
            for p in folder.rglob('*.md'):
                for link in re.findall(r'(?<!!)\[[^\]]+\]\(([^\s)]+)\)', p.read_text()):
                    if link.startswith(('http:', 'https:', '#', 'mailto:')):
                        continue
                    target = (p.parent / link.split('#')[0]).resolve()
                    try:
                        rel = target.relative_to(ROOT / 'skills')
                    except ValueError:
                        continue
                    if rel.parts and rel.parts[0] in by_name:
                        needed.add(rel.parts[0])
        if needed == names:
            break
        names = needed
    dest = args.dest.expanduser().resolve()
    collisions = [n for n in sorted(names) if (dest / n).exists() or (dest / n).is_symlink()]
    if collisions:
        parser.error('refusing to overwrite: ' + ', '.join(collisions))
    if dest == ROOT / 'skills' or ROOT / 'skills' in dest.parents:
        parser.error('destination must be outside repository skills')
    for name in sorted(names):
        shutil.copytree(ROOT / 'skills' / name, dest / name)
        print(name)
    print(f'Installed {len(names)} skills into {dest}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
