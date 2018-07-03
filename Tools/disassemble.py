#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from capstone import *

# http://shell-storm.org/shellcode/files/shellcode-806.php
shellcode = (
    b"\x31\xc0\x48\xbb\xd1\x9d\x96"
    b"\x91\xd0\x8c\x97\xff\x48\xf7"
    b"\xdb\x53\x54\x5f\x99\x52\x57"
    b"\x54\x5e\xb0\x3b\x0f\x05"
)

ARCH = {
    'arm': CS_ARCH_ARM,
    'arm64': CS_ARCH_ARM64,
    'mips': CS_ARCH_MIPS,
    'ppc': CS_ARCH_PPC,
    'x86': CS_ARCH_X86,
    'xcore': CS_ARCH_XCORE
}

MODE = {
    '16': CS_MODE_16,
    '32': CS_MODE_32,
    '64': CS_MODE_64,
    'arm': CS_MODE_ARM,
    'be': CS_MODE_BIG_ENDIAN,
    'le': CS_MODE_LITTLE_ENDIAN,
    'micro': CS_MODE_MICRO,
    'thumb': CS_MODE_THUMB
}

if __name__ == "__main__":
    print("len = %d" % len(shellcode))
    md = Cs(ARCH[argv[1]], MODE[argv[2]])
    for i in md.disasm(shellcode, 0x1000):
        print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
