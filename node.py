class MPNode(object):
    """docstring for MPNode."""

    def __init__(self, name, relations=[]):
        #super(MPNode, self).__init__()
        self.name = name
        self.relationList = relations
        self.numRelations = len(self.relationList)

    def connect(self, relation):
        if (not isinstance(relation,MPrelation)):
            print("Node must be connected to a relation")
        else:
        self.relationList.append(relation)
        self.numRelations += 1

    def getPath(self):
        for relation in self.relationList:
            print(self.name + " can be found using " + relation.name)
            relation.getNodes()



class MPrelation(object):
    """docstring for MPrelation."""


    def __init__(self, name, nodes=[]):
        #super(MPnode, self).__init__()
        self.nodeList = nodes
        self.name = name;
        self.numNodes = len(self.nodeList)

    def connect(self, node):
        if (not isinstance(node,MPnode)):
            print("node must be connected to a relation")
            raise TypeError
        if (node not in self.nodeList):
            self.nodeList.append(node)
            self.numNodes += 1

    def getReqs(rootNode):
        for node in self.nodeList:
            if not node.name == rootNode.name:
                print node.name

if __name__ == "__main__":
    a = MPnode("Pressure")
    b = MPnode("Volume")
    c = MPrelation("Ideal Gas Law",nodes=[a,b])
    a.connect(c)
    c.connect(a)
    c.connect(b)
    print(a.numRelations)
    print(b.numRelations)
    print(c.numNodes)
    a.getPath()

class MPnode(object):
    """docstring for MPnode."""


    def getPath(self):
        for relation in self.relationList:
            print(self.name + " can be found using " + relation.name)
            relation.getReqs(self.name)
