filepath = 'emails.txt'
emailList = []

#puts all emails into array
with open(filepath) as fp:
    line = fp.readline()
    while line:
        entry = line.split(', ')
        emailList.append(entry)
        line = fp.readline()

#reduce list to remove duplicates
mylist = []
for i in emailList:
    if i not in mylist:
        mylist.append(i)

#rewrites new data to file
with open('nodupe.txt', 'w') as f:
    for item in mylist:
        entry = item[0]+","+item[1]
        f.write("%s" % entry)