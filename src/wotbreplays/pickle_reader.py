#!/usr/bin/env python3

from pickle import load
from sys import argv
from asyncio import run



async def main() -> int:
	fn : str = argv[1]
	with open(fn, 'rb') as fi, open(f'{fn}.bin', 'wb') as fo:
		pickled = load(fi, encoding='bytes')
		print(f'unique_arena_id: {pickled[0]} ({type(pickled[0])})')
		fo.write(pickled[1])
	return 0


if __name__ == "__main__":
	run(main())