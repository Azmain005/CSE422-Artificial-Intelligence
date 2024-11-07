import heapq

def extract(data):
    heu = {}
    adj = {}
    for i in data:
        city = i.split()
        heu[city[0]] = city[1]
        adj[city[0]] = {}
        for j in range(2, len(city), 2):
            adj[city[0]][city[j]] = city[j + 1]
    return heu, adj

def AStar(source, dest, heuristic, adj):
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (0, source))
    parent = {}
    parent[source] = None
    dist = {}
    dist[source] = 0
    while fringe:
        curr = heapq.heappop(fringe)[1]
        if curr == dest:
            break
        for city in adj[curr]:
            temp = dist[curr] + int(adj[curr][city])
            if city not in dist or temp < dist[city]:
                dist[city] = temp
                tot_dist = int(heuristic[city]) + temp
                heapq.heappush(fringe, (tot_dist, city))
                parent[city] = curr
    return parent, dist

data = open('input.txt', 'r')
heuristic, adj = extract(data)
source = input("Start Node: ")
dest = input("Destination: ")
if (source and dest in heuristic):
    path, distance = AStar(source, dest, heuristic, adj)    
    actual_path = [dest]
    child = dest
    while child != source:
        parent = path[child]
        actual_path.append(parent)
        child = parent
    if len(actual_path) == 0:
        print('NO PATH FOUND')
    else:
        actual_path.reverse()
        ans = ' --> '.join(actual_path)
        print(f'''Path: {ans}
Total distance: {distance[dest]} km''')
else:
    print('NO PATH FOUND')
