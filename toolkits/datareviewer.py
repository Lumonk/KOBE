#
# This is to review and process the datasets
#

fileloc = './aikucun_data/alldata_unique.txt'
outputF = open(fileloc, encoding='utf8')
f= open("processed.str","w+")
print('Processing ...')

#linecount=0
#totallen=0
#maxlen=-1
#minlen=1000
#averlen=0.0
#
#longcount=0
#shortcount=0
#midcount=0

#while True:
#    line = outputF.readline()
#
#    if line == "":
#        break
#    else: 
#        line = line.replace(' ','')
#        line = line.replace('，','')
#        linecount += 1
#        totallen += len(line)
#        averlen = totallen / linecount
#        if len(line)>maxlen:
#            maxlen=len(line)
#        if len(line)<minlen:
#            minlen=len(line)
#        if len(line)>110:
#            longcount += 1
#        elif len(line)>60   :
#            midcount += 1
#        else:
#            shortcount += 1
#print("#lines:",linecount,"averlen:",averlen,sep=" ")

while True:
    line = outputF.readline()
    line = line.split('\t', 1)[0]
    if line == "":
        break
#    else: 
#        line = line.replace(' ','')
#        line = line.replace('，','')
#        line=line[6:]
#        if(line[0]=='>'):
#            line = line[1:]
#    print(str(line)+' ')
    f.write(str(line)+' ')
        
f.close()
        
    