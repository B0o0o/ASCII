import random
import os
i = random.randrange(9) + 1 
website="https://raw.githubusercontent.com/B0o0o/ASCII/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"
os.system("curl " +  website)
