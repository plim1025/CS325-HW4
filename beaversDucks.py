import sys

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.team = ''
        self.distance = 10000000

    def addNeighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)

# open file in read mode
file = open(sys.argv[1], 'r')

# split file into lines
lines = file.read().splitlines()

# get num teams and store team names in array
numTeams = int(lines.pop(0))
teams = []
for i in range(numTeams):
    teams.append(lines.pop(0));

# get num rivalries and store rivalries in array
numRivalries = int(lines.pop(0))
rivalries = []
for i in range(numRivalries):
    rivalries.append(lines.pop(0).split(' '))

# contains all vertices
graph = {}
unvisited = set()

# add vertices to graph
for i in range(len(teams)):
    graph[teams[i]] = Vertex(teams[i])
    unvisited.add(teams[i])

# add edges to vertices with rivalries
for i in range(len(rivalries)):
    graph[rivalries[i][0]].addNeighbor(graph[rivalries[i][1]])
    graph[rivalries[i][1]].addNeighbor(graph[rivalries[i][0]])

# BFS on graph of teams
q = []

while len(unvisited) > 0:
    # visit starting vertex
    graph[list(unvisited)[0]].team = 'beaver'
    graph[list(unvisited)[0]].distance = 0
    q.append(graph[list(unvisited)[0]])

    while len(q) > 0:
        u = q.pop(0)
        if u.name in unvisited:
            unvisited.remove(u.name)
        for v in u.neighbors:
            # only need to handle vertices that haven't visited yet since we know the relationships between u and visited are correct
            if v.name in unvisited:
                # if haven't marked distance yet, mark
                if v.distance > u.distance + 1:
                    v.distance = u.distance + 1
                # if even distance from starting vertex
                if v.distance % 2 == 0:
                    v.team = 'beaver'
                # if odd distance from starting vertex
                elif v.distance % 2 == 1:
                    v.team = 'duck'
                # if current vertex is same team as adjacent vertex, impossible to match all teams properly
                if v.team == u.team:
                    print('No, impossible')
                    sys.exit()
                q.append(v)

# print out Beavers and Ducks if possible
beavers = 'Beavers:\n'
ducks = 'Ducks: \n'
for v in graph:
    if graph[v].team == 'beaver':
        beavers += '\t' + v + '\n'
    elif graph[v].team == 'duck':
        ducks += '\t' + v  + '\n'
print('Yes, possible')
print(beavers)
print(ducks)