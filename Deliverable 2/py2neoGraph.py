from py2neo import Graph, Node, Relationship
#Setup
graph = Graph('bolt://localhost:7687', password="root")
filepath = 'finalData.txt'
nodeList = []
pairList = []

#get pairList from finalData.txt
with open(filepath) as fp:
    line = fp.readline()
    while line:
        entry = line.split(':')
        #make sure there is no \n in the string
        entry[0] = entry[0].rstrip()
        entry[1] = entry[1].rstrip()
        pairList.append(entry)
        line = fp.readline()

#reusable function to see if a node already exists
def hasNode(list, nodeIn):
    for j in list:
        if j['email'] == nodeIn['email']:
            return True
    return False

#reusable function to find existing node
def findNode(list, nodeIn):
    for j in list:
        if j['email'] == nodeIn['email']:
            return j
    return nodeIn


#Create nodes and relationships
for i in pairList:
    a = Node("Email", email=i[0])
    if not hasNode(nodeList, a):
        nodeList.append(a)
    b = Node("Email", email=i[1])
    if not hasNode(nodeList, b):
        nodeList.append(b)
    a_works_with_b = Relationship(findNode(nodeList, a), "WORKS_WITH", findNode(nodeList, b))
    graph.create(a_works_with_b)

