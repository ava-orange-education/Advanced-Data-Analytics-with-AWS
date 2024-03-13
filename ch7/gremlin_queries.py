# Well-Connected Nodes: Use Gremlin queries to find nodes with a high number of outgoing or incoming edges.
# This query orders the 'person' nodes by the count of their edges, in decreasing order, and limits the result to the top 3.
g.V().hasLabel('person').order().by(__.bothE().count(), decr).limit(3).valueMap()

#Not Well-Connected Nodes: Find nodes with few or no connections.
# This query is similar to the above but orders by increasing edge count, identifying the least connected nodes.
g.V().hasLabel('person').order().by(__.bothE().count(), incr).limit(3).valueMap()

