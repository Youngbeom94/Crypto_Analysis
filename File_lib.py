import os,sys

def ReadFile(in_file):
    if not os.path.exists(in_file):
        print('File %s does not exist' %(in_file))
        sys.exit()
    Infileobj = open(in_file)
    mytext = Infileobj.read()
    return mytext



def WriteFile(filename,msg):
    outfileobj = open(filename,'w')
    outfileobj.write(msg)
    outfileobj.close()
    return
