"""Validate the frozen runtime files without importing or executing the game."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def verify(directory):
    directory = Path(directory).resolve()
    manifest = json.loads((ROOT / 'release-manifest.json').read_text(encoding='utf-8'))
    for name, info in manifest['files'].items():
        path = (directory / name).resolve()
        if not path.is_relative_to(directory):
            raise ValueError('Invalid manifest path')
        if not path.is_file():
            raise ValueError(f'Missing {name}. Download the complete Demo ZIP from GitHub Releases.')
        if path.stat().st_size != info['bytes']:
            raise ValueError(f'File size mismatch: {name}')
        hasher = hashlib.sha256()
        with path.open('rb') as source:
            for block in iter(lambda: source.read(1024 * 1024), b''):
                hasher.update(block)
        digest = hasher.hexdigest()
        if digest != info['sha256']:
            raise ValueError(f'SHA-256 mismatch: {name}')
    return manifest

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=ROOT / 'web')
    args = parser.parse_args()
    try:
        manifest = verify(args.directory)
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')
    print(f"DEMO INTEGRITY: {len(manifest['files'])} frozen files; PASS")
