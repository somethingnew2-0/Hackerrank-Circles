class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)
		
	def __eq__(self, other):
        return self.source == other.source && self.sink = other.sink
 
class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
 
    def add_vertex(self, vertex):
        self.adj[vertex] = []
 
    def get_edges(self, v):
        return self.adj[v]
 
    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0
 
    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge,residual) in path:
                result = self.find_path( edge.sink, sink, path + [(edge,residual)] ) 
                if result != None:
                    return result
 
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            flow = min(res for edge,res in path)
            for edge,res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))

class Detector(object):
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
	def get_position(self):
		return (self.x, self.y)
	def distance(p0, p1):
		return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
		
import sys
tests = sys.stdin.readline()
for test in range(0, int(tests)):
	width, height, number = sys.stdin.readline().split()
	detectors = []
	g=FlowNetwork()
	for circle in range(0, int(number)):
		x, y, radius = sys.stdin.readline().split()
		detectors.append(Detector(x, y, radius))
		g.add_vertex(circle)
	
	for idx, detector in enumerate(detectors):
		for idx2, neighbor in enumerate(detectors):
			if detector == neighbor || Edge(idx, idx2, 0) in g.get_edges(idx):
				continue
			if(Detector.distance(detector.get_position(), neighbor.get_position()) <= detector.radius + neighbor.radius):
				g.add_edge(idx, idx2, 1)

	map(g.add_vertex, ['s','o','p','q','r','t'])
	g.add_edge('s','o',3)
	g.add_edge('s','p',3)
	g.add_edge('o','p',2)
	g.add_edge('o','q',3)
	g.add_edge('p','r',2)
	g.add_edge('r','t',3)
	g.add_edge('q','r',4)
	g.add_edge('q','t',2)
	print g.max_flow('s','t')