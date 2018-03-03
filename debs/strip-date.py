#!/usr/bin/env python3

from os import rename
from pathlib import Path

TARGET_DIR=Path("debs/")

debs = [file for file in TARGET_DIR.iterdir() if file.is_file()]

for deb in debs:
	deb_name = deb.name
	try:
		first_underscore = deb_name.index("_")
		second_underscore = deb_name.index("_", first_underscore + 1)
		deb.rename(TARGET_DIR / Path("%s%s" % (
			deb_name[:first_underscore],
			deb_name[second_underscore:])))
	except ValueError:
		print("Could not rename '%s', skipping..." % deb_name)