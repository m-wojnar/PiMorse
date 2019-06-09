import RPi.GPIO as io
from time import *

#dictionary with chars
chars = {'a' : "sl",
         'b' : "lsss",
         'c' : "lsls",
         'd' : "lss",
         'e' : "s",
         'f' : "ssls",
         'g' : "lls",
         'h' : "ssss",
         'i' : "ss",
         'j' : "slll",
         'k' : "lsl",
         'l' : "slss",
         'm' : "ll",
         'n' : "ls",
         'o' : "lll",
         'p' : "slls",
         'q' : "llsl",
         'r' : "sls",
         's' : "sss",
         't' : "l",
         'u' : "ssl",
         'v' : "sssl",
         'w' : "sll",
         'x' : "lssl",
         'y' : "lsll",
         'z' : "llss",
         '0' : "lllll",
         '1' : "sllll",
         '2' : "sslll",
         '3' : "sssll",
         '4' : "ssssl",
         '5' : "sssss",
         '6' : "lssss",
         '7' : "llsss",
         '8' : "lllss",
         '9' : "lllls",
         '.' : "slslsl",
         ',' : "llssll",
         '\'' : "slllls",
         '"' : "slssls",
         '_' : "ssllsl",
         ':' : "lllsss",
         ';' : "lslsls",
         '?' : "ssllss",
         '!' : "lslsll",
         '-' : "lssssl",
         '+' : "slsls",
         '/' : "lssls",
         '(' : "lslls",
         ')' : "lsllsl",
         '=' : "lsssl",
         '@' : "sllsls"
        }

def short_signal():
    io.output(21, 1)
    sleep(0.15)
    io.output(21, 0)
    sleep(0.15)

def long_signal():
    io.output(21, 1)
    sleep(0.5)
    io.output(21, 0)
    sleep(0.15)


#setup gpio
io.setmode(io.BCM)
io.setup(21, io.OUT)

#read and split message into words
print("Enter the text you want to translate into the Morse code:")
message = input()
message = message.lower()
message = message.split(' ')

for word in message:
    for char in word:
        if not (char in chars):
            print("Character \"" + char + "\" is not supported, skipping this character")
            continue

        for i in chars[char]:
            if i == 's':
                short_signal()
            else:
                long_signal()
        #space between signs
        io.output(21, 0)
        sleep(0.2)

    #space between words
    io.output(21, 0)
    sleep(0.5)
    
print("Translation done, thank you for using this program!")
#gpio cleanup
io.output(21, 0)
io.cleanup()