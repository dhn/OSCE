#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sys
import string
import argparse
from subprocess import check_output

__version__ = "# $Id: bin2op.py,v 1.3 2018/07/07 23:23:30 dhn Exp $"
__license__ = "BSD"


# thanks zerosum0x0
def parse(obj, formats):
	objdump = ['objdump', '-D', '-M', "intel", obj]

	lines = check_output(objdump)
	lines = lines.split(b'Disassembly of section')[1]
	lines = lines.split(b'\n')[3:]

	shellcode = ""
	code = []

	for line in lines:
		line = line.strip()

		tabs = line.split(b'\t')
		if (len(tabs) < 2):
			continue
		bytes = tabs[1].strip()

		instruction = "."
		if (len(tabs) == 3):
			instruction = tabs[2].strip().decode("utf-8")

		bytes = bytes.split(b' ')
		shellcodeline = ""
		for byte in bytes:
			shellcodeline += "\\x" + byte.decode("utf-8")

		shellcode += shellcodeline
		if formats is not None:
			c = '\t%-*s# %s' % (32, '"'+shellcodeline+'"', instruction)
		else:
			c = '%-*s/* %s */' % (32, '"'+shellcodeline+'"', instruction)
		code.append(c)

	return shellcode, code


def main(args):
	if os.path.exists(args.file):
		objfile = args.file

		if args.python:
			formats = "python"
		else:
			formats = None

		shellcode, code = parse(objfile, formats)
		format_code = ""
		for line in code:
			format_code += line + "\n"

		if args.syntax == "short" and args.python:
			shellcode = re.sub(
				"(.{32})", "\t\"\\1\"\n",
				shellcode, 0, re.DOTALL)
			print("shellcode = (\n%s\n)" % shellcode[:-1])
		elif args.syntax == "short":
			shellcode = re.sub(
				"(.{32})", "\\1\n",
				shellcode, 0, re.DOTALL)
			print(shellcode)

		if args.syntax == "large" and args.python:
			print("shellcode = (\n%s\n)" % format_code[:-1])
		elif args.syntax == "large":
			print(format_code[:-1])
	else:
		print("[!] file does not exist")
		sys.exit(1)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="Extract the opcode from the objdump of a binary",
		epilog="Example: %s -f bindshell/build/bindshell.o -s large\n" \
				"\t %s -f bindshell/build/bindshell.o -s large -p\n" \
				"\t %s -f bindshell/build/bindshell.o -p"
					% (__file__, __file__, __file__),
				formatter_class=argparse.RawDescriptionHelpFormatter
	)
	parser.add_argument("-f", "--file",
			help="The assembly code filename",
			required=True)
	parser.add_argument("-s", "--syntax",
			help="Show [less|verbose] version of opcode",
			choices = ["short", "large"],
			default="short")
	parser.add_argument("-p", "--python",
			help="Format output to python syntax",
			default=False, action="store_true")
	args = parser.parse_args()

	main(args)
