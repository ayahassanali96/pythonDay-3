readmode = "r"
writemode = "w"

def readtofile(path):
    try:
        f = open(path,"r")
        if(f.readable()):
            return f.read()
        f.close()
    except FileNotFoundError:
        print("This file not found")