from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

# Connect to Neptune
graph = Graph()
remoteConn = DriverRemoteConnection('wss://your-neptune-endpoint:8182/gremlin', 'g')
g = graph.traversal().withRemote(remoteConn)

# Add vertices
names = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank', 'Grace', 'Helen', 'Ivan', 'Judy']
vertices = {}
for name in names:
    vertex = g.addV('person').property('name', name).next()
    vertices[name] = vertex

# Add edges (connections)
connections = [
    ('Alice', 'Bob'), ('Alice', 'Carol'), ('Alice', 'Dave'),
    ('Bob', 'Carol'), ('Bob', 'Eve'),
    ('Carol', 'Dave'), ('Carol', 'Eve'),
    ('Dave', 'Eve'),
    # less connected individuals
    ('Frank', 'Grace'), ('Helen', 'Ivan')
]

for (from_name, to_name) in connections:
    g.V(vertices[from_name]).addE('knows').to(g.V(vertices[to_name])).next()

# Close the connection
remoteConn.close()

