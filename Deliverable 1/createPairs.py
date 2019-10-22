filepath = 'nodupe.txt'
emailList = []

#puts all emails into array
with open(filepath) as fp:
    line = fp.readline()
    while line:
        entry = line.split(',')
        emailList.append(entry)
        line = fp.readline()

#create pairs and add to list
pairlist = []
for i in emailList:
    for j in emailList:
        if i[0] == j[0] and i[1] != j[1]:
            pairlist.append(i[1].rstrip()+":"+j[1])

#remove duplicates and reverse duplicates
finallist = []
for i in pairlist:
    if i not in finallist:
        temp = i.split(":")
        newi = (temp[1]+":"+temp[0]).rstrip()+"\n"
        if newi not in finallist:
            finallist.append(i)

#writes data to file
with open('finalData.txt', 'w') as f:
    for item in finallist:
        f.write("%s" % item)
