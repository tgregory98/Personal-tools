import numpy as np

n = 5
x = np.random.rand(n,n)
y = np.where(x > 0.3, 1, 0)
y = y.astype(str)
a1, a2, b1, b2 = np.random.randint(0, n, size=4)
y[a1][a2] = 'a'
y[b1][b2] = 'b'
grid = y

def find_pos(grid, x):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == x:
                return [i, j]

current_activenodes = [find_pos(grid, 'a')]
current_routes = [[find_pos(grid, 'a')]]
new_activenodes = []
new_routes = []
shortest_route = []
pass_number = 1

s1, s2 = grid.shape
smax = max([s1, s2])

while shortest_route == []:
    print('pass_number: ' + str(pass_number))
    pass_number = pass_number + 1
    if pass_number > 2 * smax:
        print('stopped here due to too many iterations \n')
        break

    new_activenodes = None
    new_activenodes = []
    new_routes = None
    new_routes = []
    node_enumeration = 0
    for node in current_activenodes:
        print('node: ' + str(node))
        i = node[0]
        j = node[1]
        if i - 1 >= 0:
            if grid[i - 1][j] == '1':
                new_activenodes.append([i - 1, j])
                N = current_routes[node_enumeration] + [[i - 1, j]]
                print('    N: ' + str(N))
                new_routes.append(N)
                grid[i][j] == '0'
            elif grid[i - 1][j] == 'b':
                N = current_routes[node_enumeration] + [[i - 1, j]]
                shortest_route = N
                break
        if j + 1 < grid.shape[1]:
            if grid[i][j + 1] == '1':
                new_activenodes.append([i, j + 1])
                E = current_routes[node_enumeration] + [[i, j + 1]]
                print('    E: ' + str(E))
                new_routes.append(E)
                grid[i][j] == '0'
            elif grid[i][j + 1] == 'b':
                E = current_routes[node_enumeration] + [[i, j + 1]]
                shortest_route = E
                break
        if i + 1 < grid.shape[0]:
            if grid[i + 1][j] == '1':
                new_activenodes.append([i + 1, j])
                S = current_routes[node_enumeration] + [[i + 1, j]]
                print('    S: ' + str(S))
                new_routes.append(S)
                grid[i][j] == '0'
            elif grid[i + 1][j] == 'b':
                S = current_routes[node_enumeration] + [[i + 1, j]]
                shortest_route = S
                break
        if j - 1 >= 0:
            if grid[i][j - 1] == '1':
                new_activenodes.append([i, j - 1])
                W = current_routes[node_enumeration] + [[i, j - 1]]
                print('    W: ' + str(W))
                new_routes.append(W)
                grid[i][j] == '0'
            elif grid[i][j - 1] == 'b':
                W = current_routes[node_enumeration] + [[i, j - 1]]
                shortest_route = W
                break
        print('    cummulative new_activenodes up to node ' + str(node) + ': ' + str(new_activenodes))
        print('    cummulative new_routes up to node ' + str(node) + ': ' + str(new_routes))
        node_enumeration = node_enumeration + 1
    print('new_activenodes at end of pass: ' + str(new_activenodes))
    print('new_routes at end of pass: ' + str(new_routes))
    current_activenodes = new_activenodes
    current_routes = new_routes
    print('\n')
print(grid)
print('shortest_route: ' + str(shortest_route))
print('which has length ' + str(len(shortest_route)))
