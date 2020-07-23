import sys

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.team = ''
        self.visited = False
        self.distance = 10000000

    def addNeighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)

file = open(sys.argv[1], 'r')

lines = file.read().splitlines()

numTeams = int(lines.pop(0))
teams = []
for i in range(numTeams):
    teams.append(lines.pop(0));

numRivalries = int(lines.pop(0))
rivalries = []
for i in range(numRivalries):
    rivalries.append(lines.pop(0).split(' '))

graph = {}

for i in range(len(teams)):
    graph[teams[i]] = Vertex(teams[i])

for i in range(len(rivalries)):
    graph[rivalries[i][0]].addNeighbor(graph[rivalries[i][1]])
    graph[rivalries[i][1]].addNeighbor(graph[rivalries[i][0]])

# BFS i=on graph of teams
q = []
graph[teams[0]].visited = True
graph[teams[0]].team = 'beaver'
graph[teams[0]].distance = 0

for v in graph[teams[0]].neighbors:
    graph[v.name].team = 'duck'
    graph[v.name].distance = 1
    q.append(v)
while len(q) > 0:
    u = q.pop(0)
    u.visited = True
    for v in u.neighbors:
        if not v.visited:
            # if haven't marked distance yet, mark
            if v.distance > u.distance + 1:
                v.distance = u.distance + 1
            if v.distance % 2 == 0:
                v.team = 'beaver'
            elif v.distance % 2 == 1:
                v.team = 'duck'
            if v.team == u.team:
                print('No, impossible')
                sys.exit()
            q.append(v)

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