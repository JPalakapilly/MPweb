class MPnode(object):
    """docstring for MPNode."""

    def __init__(self, name, governingRelations=[]):
        #super(MPNode, self).__init__()
        self.name = name
        self.relations = set()
        for relation in governingRelations:
            self.connect(relation)

    @property
    def numRelations(self):
        return len(relations)

    def connect(self, relation):
        if (not isinstance(relation,MPrelation)):
            print("Node must be connected to a relation")
        elif (relation not in self.relations):
            self.relations.add(relation)
            relation.connect(self)

    def getPath(self):
        for relation in self.relations:
            print(self.name + " can be found using " + relation.name)
            relation.getReqs(self)



class MPrelation(object):
    """docstring for MPrelation."""


    def __init__(self, name, relatedNodes=[]):
        #super(MPnode, self).__init__()
        self.name = name;
        self.nodes = set()
        for node in relatedNodes:
            self.connect(node)

    @property
    def numNodes(self):
        return len(relations)

    def connect(self, node):
        if (not isinstance(node,MPnode)):
            print("node must be connected to a relation")
        elif (node not in self.nodes):
            self.nodes.add(node)
            node.connect(self)

    def getReqs(self,rootNode):
        needed = []
        for node in self.nodes:
            if not node.name == rootNode.name:
                needed.append(node.name)
        print("Needed variables:")
        print(needed)
        print("")

class MPweb(object):
    """docstring for MPweb."""
    def __init__(self, arg):
        super(MPweb, self).__init__()
        self.arg = arg






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
