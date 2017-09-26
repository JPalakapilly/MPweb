class MPnode(object):
    """docstring for MPNode."""

    def __init__(self, name, relations=[]):
        #super(MPNode, self).__init__()
        self.name = name
        self.relationList = []
        self.numRelations = 0
        for relation in relations:
            self.connect(relation)


    def connect(self, relation):
        if (not isinstance(relation,MPrelation)):
            print("Node must be connected to a relation")
        elif (relation not in self.relationList):
            self.relationList.append(relation)
            self.numRelations += 1
            relation.connect(self)

    def getPath(self):
        for relation in self.relationList:
            print(self.name + " can be found using " + relation.name)
            relation.getReqs(self)



class MPrelation(object):
    """docstring for MPrelation."""


    def __init__(self, name, nodes=[]):
        #super(MPnode, self).__init__()
        self.name = name;
        self.nodeList = []
        self.numNodes = 0
        for node in nodes:
            self.connect(node)


    def connect(self, node):
        if (not isinstance(node,MPnode)):
            print("node must be connected to a relation")
        elif (node not in self.nodeList):
            self.nodeList.append(node)
            self.numNodes += 1
            node.connect(self)

    def getReqs(self,rootNode):
        needed = []
        for node in self.nodeList:
            if not node.name == rootNode.name:
                needed.append(node.name)
        print("Needed variables:")
        print(needed)
        print("")

if __name__ == "__main__":
    P = MPnode("Pressure")
    V = MPnode("Volume")
    T = MPnode("Temperature")
    n = MPnode("Num Moles")
    IGL = MPrelation("Ideal Gas Law",nodes=[P,V,n,T])
    P.connect(IGL)
    IGL.connect(V)
    T.connect(IGL)
    Eint = MPrelation("Equation to find internal energy")
    U = MPnode("Internal Energy", [Eint])
    n.connect(Eint)
    Eint.connect(T)
    print(P.numRelations)
    print(V.numRelations)
    print(IGL.numNodes)
    T.getPath()
