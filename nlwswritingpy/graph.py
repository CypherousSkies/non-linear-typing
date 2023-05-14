# This Python file uses the following encoding: utf-8


class Graph():
    graph = None
    data = None
    def __init__(self,graph=None,data=None):
        """
        Graph(graph=None,data=None) creates a new Graph object with optional
        node-connection dictionary, graph, and node-value dictionary, data.
        graph :: Hashable -> [Hashable]
        nodes :: Hashable -> *
        Note that the domain of graph and of data should be the same,
        e.g. if graph = {"A": {"B","C"},"B": {"C"},"C": "C"}, then
        data["A"], data["B"], and data["C"] should all return something (even if that something is null)
        additionally any other input to data shouldn't return anything
        """
        if graph.keys != data.keys:
            raise ValueError("graph and data keys don't match up!")
        self.graph = graph
        self.data = data
    def add(self,node,data,*predecessors):
        """
        add(node,data,*predecessors) adds a node to the graph with
        id `node` and data `data` connected to other nodes *predecessors
        """
        self.graph[node] = predecessors
        self.data[node] = data
    def pop(self,node):
        """
        pop(node) removes node from the graph
        """
        self.graph.pop(node)
        self.data.pop(node)
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
    def __init__(self,graph=None,data=None):
        """
        StaticGraph(graph=None,data=None) creates a graph with the connections
        of `graph` and the node's appearance `data`
        for each node, data[node] = disp
        where `disp` is a Glyph
        """
        super().__init__(graph,data)
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
    def __init__(self,graph=None,data=None):
        """
        DisplayGraph(graph=None,data=None) creates a graph with the connections
        of `graph` and the display/location/spline data `data`
        for each node, data[node] should be formatted like (disp,pos,connection_data)
        where
          `disp` is a Glyph
          `pos` = np.array(x,y) is the position of the node
          `connection_data` is a dictionary with keys graph[node] and values
            of 4-vectors np.array(x,y,dx,dy) which form a one-sided spline anchor
            where (x,y) is relative to the glyph
        """
        super().__init__(graph,data)
        for k in graph.keys():
            (_,_,_,dict) = data[k]
            if graph[k] != dict.keys:
                raise ValueError("Data keys don't match connections!")
