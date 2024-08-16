import networkx as nx 
import matplotlib.pyplot as plt

def BFS(graph,src,des):
    q=[]
    q.append(src)
    vis=set()
    order=[]
    vis.add(src)
    while q:
        v=q.pop(0)
        if v==des:
            order.append(des)
            break
        order.append(v)
        for n in graph[v]:
            if n not in vis:
                vis.add(n)
                q.append(n)
    return order





def DFS(graph,s):
    vis=set()
    stk=[s]
    d=[]
    while stk:
        v=stk.pop()
        if v not in vis:
            d.append(v)
            for n in graph[v]:
                if n not in vis:
                    stk.append(n)
    return d



# Load the dataset
# Assuming the dataset is in a file called 'facebook_combined.txt'
# The file contains edges in the format: node1 node2

G = nx.read_edgelist('facebook_combined.txt')

# Basic info about the graph
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Is the graph directed: {G.is_directed()}")
print(f"Graph density: {nx.density(G)}")

# Define start and goal nodes
start_node = '0'  # Example start node
goal_node = '100'  # Example goal node

# Ensure start_node and goal_node are in the graph
if start_node not in G or goal_node not in G:
    raise ValueError("Start or goal node not in graph")
    
#nx.draw(G)
#plt.show()
l=[]
ll=[]
graph={}
nodes=[]
edges=[]

f=open('facebook_combined.txt','r')
for x in f:
    l=x.split(" ")
    e1=int(l[0])
    e2=int(l[1].rstrip('\n'))
    if e1 not in nodes:
        nodes.append(e1)
    if e2 not in nodes:
        nodes.append(e2)
    ll.append(int(l[0]))
    if int(l[0]) not in graph:
        graph[int(l[0])]=[]
    if int(l[1].rstrip('\n')) not in graph:
        graph[int(l[1].rstrip('\n'))]=[]
    graph[int(l[0])].append(int(l[1].rstrip('\n')))
    graph[int(l[1].rstrip('\n'))].append(int(l[0]))
    edges.append([e1,e2])
f.close()
print("BFS")
src=int(input("Source:"))
des=int(input("Destination"))
bfs=BFS(graph,src,des)
print("DFS")
src1=int(input("enter source"))
dfs=DFS(graph,src1)

Grraph=nx.Graph()
col=[]


for e in edges:
    Grraph.add_edge(e[0],e[1])
    
ch=int(input("enter 1 for bfs or 2 for dfs"))
if ch==1:
    for n in nodes:
        if n not in bfs:
            Grraph.add_node(n)
            col.append('blue')

    for b in bfs:
        Grraph.add_node(b)
        col.append('red')
else:
    for n in nodes:
        if n not in dfs:
            Grraph.add_node(n)
            col.append('blue')

    for d in dfs:
        Grraph.add_node(b)
        col.append('red')
nx.draw(Grraph,node_color=col,with_labels=True)
plt.show()
