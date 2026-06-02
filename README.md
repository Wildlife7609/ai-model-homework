# ai-model-homework
Goal: Implement and compare multiple graph search algorithms to find optimal routes on a map of Romania (and optionally Atlanta).

Search Algorithms Implemented
Algorithm	Description
BFS	Breadth-First Search — finds path by fewest edges
UCS	Uniform Cost Search — finds lowest-cost path
A* Search — uses a heuristic (null or Euclidean distance) to guide search
Bidirectional UCS	Searches from both start and goal simultaneously
Bidirectional A*	Same, but heuristic-guided
Tridirectional UCS	Searches from 3 goal nodes simultaneously to find the best connecting path
Tridirectional Upgraded	Heuristic-enhanced version of tri-search
