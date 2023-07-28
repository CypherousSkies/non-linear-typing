# This Python file uses the following encoding: utf-8


class Graph():
    graph = None
    data = None
    def __init__(self,graph={},data={},update=None):
        """
        Graph(graph=None,data=None,update=None) creates a new Graph object with optional
        node-connection dictionary, graph, node-value dictionary, data, and update function, update.
        graph :: Hashable -> [Hashable]
        data :: Hashable -> *
        All edges of graph should be mutual (e.g. if
        Note that the domain of graph and of data should be the same,
        e.g. if graph = {"A": {"B","C"},"B": {"C"},"C": "C"}, then
        data["A"], data["B"], and data["C"] should all return something (even if that something is None)
        additionally any other input to data shouldn't return anything
        """
        if graph.keys != data.keys:
            raise ValueError("graph and data keys don't match up!")
        self.graph = graph
        self.data = data
        self.update = update
    def add(self,node,data,*predecessors):
        """
        add(node,data,*predecessors) adds a node to the graph with
        id `node` and data `data` connected to other nodes *predecessors
        """
        if node is None:
            node = str(len(self.graph)+1)
        for edge in predecessors:
            self.connect(node,edge)
        self.graph[node] = predecessors
        self.data[node] = data
        if self.update is not None:
            self.update()
    def addAuto(self,data,*predecessors):
        """
        addAuto(self,data,*predecessors) adds a node with automatically assigned id,
        and specified data `data` and connections to *predecessors
        """
        raise NotImplementedError("No automatic ID algorithm defined!")
    def connect(self,nodeA,nodeB):
        self.graph[nodeA] += nodeB
        self.graph[nodeB] += nodeA
    def pop(self,node):
        """
        pop(node) removes node from the graph
        """
        self.graph.pop(node)
        self.data.pop(node)
        if self.update is not None:
            self.update()
    def prune(self):
        """
        prune() removes dangling edges from the graph
        there is almost certianly a faster way of doing this
        """
        for node in self.keys():
            for edge in self.getConnections(node):
                if edge not in self.keys():
                    self.graph[node].pop(edge)
        if self.update is not None:
            self.update()
    def getConnections(self,node):
        """
        getConnections(node) returns graph[node]
        """
        return self.graph[node]
    def getData(self,node):
        """
        getData(node) returns data[node]
        """
        return self.data[node]
    def keys(self):
        """
        keys() returns a list of nodes
        """
        return self.graph.keys()


class StaticGraph(Graph):
    def __init__(self,graph=None,data=None,update=None):
        """
        StaticGraph(graph=None,data=None) creates a graph with the connections
        of `graph` and the node's appearance `data`
        for each node, data[node] = disp
        where `disp` is a Glyph
        """
        super().__init__(graph,data,update)
    def makeDisplayable(self):
        """
        makeDisplayable() returns a DisplayGraph with the same nodes and connections,
        automatically doing embedding checks, crossing resolution, and other
        embedding stuff.
        I don't expect this to be an especially stable process (e.g. adding
        a node might re-arange the display completely) but the idea is that
        this will automatically make the most space-efficient, minimal-crossing
        embedding for display purposes.
        Is this silly? possibly. Do I want it? yes.
        I mostly like the idea of this for "professional" work where the presentation
        isn't as important as the things being represented, so ideally
        this automates much of the difficulty of layout.
        """
        raise NotImplementedError("makeDisplayable not yet implemented!")


class DisplayGraph(Graph):
    def __init__(self,graph=None,data=None,update=None):
        """
        DisplayGraph(graph=None,data=None) creates a graph with the connections
        of `graph` and the display/location/spline data `data`
        for each node, data[node] should be formatted like (disp,pos)
        where
          `disp` is a Glyph
          `pos` = np.array(x,y) is the position of the node
        """
        super().__init__(graph,data,update)
        for k in graph.keys():
            dict = data[k][0].outgoing
            if graph[k] != dict.keys:
                raise ValueError("Data keys don't match connections!")
    def getConnections(self,node):
        return self.data[node][0].outgoing
    def addAuto(self,data,*p):
        return self.add(self,len(self.data),data,*p)
    def add(self,node,data,*predecessors):
        if predecessors is None:
            self.data[node] = data
            self.graph[node] = data[0].outgoing
        elif len(predecessors) == 1:
            pred = predecessors[0]
            bp = pred.addAnchor(node)
            if bp is not None:
                self.addAuto((bp,data[1]),)# ???????? I think i need to get a predecessor here?


