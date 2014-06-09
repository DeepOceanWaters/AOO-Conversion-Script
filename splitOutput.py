import sys
import os.path
findStr = "Building module "
outDir = "AllOutput"

filePath = sys.argv[1]
f = open(filePath,"r")
data = f.read()
it = 0
while(True):
        it = data.find(findStr,it)
        if (it == -1):
                break
        it += len(findStr)
        end_it = data.find("\n",it)
        if (end_it == -1):
                print "Error, no newline found"
        fileName = data[it:end_it]
        fileName = fileName.strip()
        end_it = data.find(findStr,it)
        outStr = data[it:end_it]
        try:
                out = open(os.path.join(fileName,fileName+".txt"),"w")
                out.write(outStr)
                out.close()
        except IOError as e:
                print "Unable to open/write to file " + fileName
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
