"""Create optional Nginx precompressed files from a verified complete Demo."""
import argparse
import gzip
import os
import shutil
from pathlib import Path
from verify_demo import ROOT, verify

def prepare(directory):
    manifest = verify(directory)
    for name in manifest['files']:
        if Path(name).suffix not in {'.js', '.wasm', '.pck'}:
            continue
        source = directory / name
        target = directory / (name + '.gz')
        temp = directory / (name + '.gz.part')
        try:
            with source.open('rb') as src, temp.open('wb') as dest:
                with gzip.GzipFile(filename='', fileobj=dest, mode='wb', mtime=0, compresslevel=6) as compressed:
                    shutil.copyfileobj(src, compressed, 1024 * 1024)
            os.utime(temp, (source.stat().st_atime, source.stat().st_mtime))
            temp.replace(target)
        finally:
            temp.unlink(missing_ok=True)
        print(f'{name}: {source.stat().st_size:,} -> {target.stat().st_size:,} bytes')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=ROOT / 'web')
    args = parser.parse_args()
    try:
        prepare(args.directory.resolve())
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')
