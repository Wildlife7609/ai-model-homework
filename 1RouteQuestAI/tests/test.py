import heapq
import math

class PriorityQueue(object):
    """
    A queue structure where each element is served in order of priority.

    Elements in the queue are popped based on the priority with higher priority
    elements being served before lower priority elements.  If two elements have
    the same priority, they will be served in the order they were added to the
    queue.

    Traditionally priority queues are implemented with heaps, but there are any
    number of implementation options.

    (Hint: take a look at the module heapq)

    Attributes:
        queue (list): Nodes added to the priority queue.
    """

    def __init__(self):
        """Initialize a new Priority Queue."""

        self.queue = []
    

    def pop(self):
        """
        Pop top priority node from queue.

        Returns:
            The node with the highest priority.
        """

        # TODO: finish this function!͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
        #raise NotImplementedError
        node = sorted(self.queue)[0]
        for i, j in self.queue:
            if i == node[0]:
                removed_node = (i, j)
                self.queue.remove(removed_node)
                return removed_node
#         return heapq.heappop(self.queue)
                
    def is_empty(self):
        return len(self.queue) == 0

    def remove(self, node):
        """
        Remove a node from the queue.

        Hint: You might require this in ucs. However, you may
        choose not to use it or to define your own method.

        Args:
            node (tuple): The node to remove from the queue.
        """

        return self.queue.remove(node)

    def __iter__(self):
        """Queue iterator."""

        return iter(sorted(self.queue))

    def __str__(self):
        """Priority Queue to string."""

        return 'PQ:%s' % self.queue

    def append(self, node):
        """
        Append a node to the queue.

        Args:
            node: Comparable Object to be added to the priority queue.
        """

        # TODO: finish this function!͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
        #raise NotImplementedError
        return self.queue.append(node)
#         heapq.heapify(self.queue)
#         new_node = (node[0], self.count, node[1])
#         result = heapq.heappush(self.queue, new_node)
#         self.count += 1
#         return result
    
    def __contains__(self, key):
        """
        Containment Check operator for 'in'

        Args:
            key: The key to check for in the queue.

        Returns:
            True if key is found in queue, False otherwise.
        """

        return key in [n[-1] for n in self.queue]

    def __eq__(self, other):
        """
        Compare this Priority Queue with another Priority Queue.

        Args:
            other (PriorityQueue): Priority Queue to compare against.

        Returns:
            True if the two priority queues are equivalent.
        """

        return self.queue == other.queue

    def size(self):
        """
        Get the current size of the queue.

        Returns:
            Integer of number of items in queue.
        """

        return len(self.queue)

    def clear(self):
        """Reset queue to empty (no nodes)."""

        self.queue = []

    def top(self):
        """
        Get the top item in the queue.

        Returns:
            The first item stored in the queue.
        """

        return self.queue[0]


# class PriorityQueue(object):

#     def __init__(self):
        
#         self.queue = []
#         self.counter = 0

#     def pop(self):
         
#         # top = heapq.heappop(self.queue)
#         # print(top, len(top))
#         # return [top[x] for x in range(len(top)) if x != len(top) - 2]
#         node = sorted(self.queue)[0]
#         for i, j in self.queue:
#             if i == node[0]:
#                 removed_node = (i, j)
#                 self.queue.remove(removed_node)
#                 return removed_node

#     def remove(self, node):
        
#         # nodes_need_append = []
#         # for i in range(len(self.queue)):
#         #     poped = heapq.heappop(self.queue)
#         #     if poped[-1] == node:
#         #         break
#         #     else:
#         #         nodes_need_append.append(poped)
#         # for node in nodes_need_append:
#         #     heapq.heappush(self.queue, node)
#         m = self.queue.remove(node)
#         return m
    
#     def remove_node(self, x):
#         for i, j in self.queue:
#             if j == x:
#                 self.queue.remove((i, j))
#         return (i, j)
    

#     def __iter__(self):
         
#         return iter(sorted(self.queue))

#     def __str__(self):
         
#         return 'PQ:%s' % self.queue

#     def append(self, node):
         
#         # anc = [item for item in node]
#         # print("anc :" , anc, anc[-1], self.counter)
#         # temp = anc[-1]
#         # anc[-1] = self.counter
#         # anc.append(temp)
#         # heapq.heappush(self.queue, anc)
#         # self.counter += 1
#         return self.queue.append(node)

#     def __contains__(self, key):
         
#         return key in [n[-1] for n in self.queue]

#     def __eq__(self, other):
         
#         return self.queue == other.queue

#     def size(self):
         

#         return len(self.queue)

#     def clear(self):
         
#         self.queue = []

#     def top(self):

#         return self.queue[0]

    


class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, node, neighbors_with_weights):
        self.graph[node] = neighbors_with_weights
    
    def neighbors(self, node):
        return [neighbor for neighbor, _ in self.graph[node]]
    
    def get_edge_weight(self, u, v):
        for neighbor, weight in self.graph[u]:
            if neighbor == v:
                return weight
        return math.inf
    



#export

# def tridirectional_search(graph, goals):
#     """
#     Exercise 3: Tridirectional UCS Search

#     See README.MD for exercise description.

#     Args:
#         graph (ExplorableGraph): Undirected graph to search.
#         goals (list): Key values for the 3 goals

#     Returns:
#         The best path as a list from one of the goal nodes (including both of
#         the other goal nodes).
#     """
#     # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
# #     raise NotImplementedError

#     #these for init queue
#     goal0, goal1, goal2 = goals
    
#     goal0_queue = PriorityQueue()
#     goal0_path_cost = {goal0:0}
#     goal0_prev = {goal0: None}
#     goal0_queue.append((0, goal0))
#     goal0_pop = set()
    
#     goal1_queue = PriorityQueue()
#     goal1_path_cost = {goal1:0}
#     goal1_prev = {goal1: None}
#     goal1_queue.append((0, goal1))
#     goal1_pop = set()
    
#     goal2_queue = PriorityQueue()
#     goal2_path_cost = {goal2:0}
#     goal2_prev = {goal2: None}
#     goal2_queue.append((0, goal2))
#     goal2_pop = set()
    
#     #make sure each node explored once
#     total_pop = set()
#     #these for found best common node and path
#     best_node01 = None
#     best_node02 = None
#     best_node12 = None

#     mu01 = 1e9
#     mu02 = 1e9
#     mu12 = 1e9
#     found01 = False
#     found02 = False
#     found12 = False
 
#     if len(set(goals)) == 1:
#         return []
    
#     while not goal0_queue.is_empty() and not goal1_queue.is_empty() and not goal2_queue.is_empty():
#         cost0, goal0_front = goal0_queue.pop()
#         if goal0_front not in goal0_pop and goal0_front not in goal1_pop and goal0_front not in goal2_pop:
#             if goal0_front not in 
#             goal0_neighbors = sorted(graph.neighbors(goal0_front))
#             goal0_pop.add(goal0_front)
#             for goal0_neighbor in goal0_neighbors:
#                 goal0_cost = goal0_path_cost[goal0_front] + graph.get_edge_weight(goal0_front, goal0_neighbor)
#                 if goal0_neighbor not in goal0_path_cost or goal0_cost < goal0_path_cost[goal0_neighbor]:
#                     goal0_path_cost[goal0_neighbor] = goal0_cost
#                     goal0_queue.append((goal0_cost, goal0_neighbor))
#                     goal0_prev[goal0_neighbor] = goal0_front   



        
#         goal1_front = goal1_queue.pop()[-1]    
#         if goal1_front not in goal1_pop and goal1_front not in goal0_pop and goal1_front not in goal2_pop:
#             goal1_neighbors = sorted(graph.neighbors(goal1_front))
#             goal1_pop.add(goal1_front)
#             for goal1_neighbor in goal1_neighbors:
#                 goal1_cost = goal1_path_cost[goal1_front] + graph.get_edge_weight(goal1_front, goal1_neighbor)
#                 if goal1_neighbor not in goal1_path_cost or goal1_cost < goal1_path_cost[goal1_neighbor]:
#                     goal1_path_cost[goal1_neighbor] = goal1_cost
#                     goal1_queue.append((goal1_cost, goal1_neighbor))
#                     goal1_prev[goal1_neighbor] = goal1_front 
                    
        
#         goal2_front = goal2_queue.pop()[-1]
#         if goal2_front not in goal2_pop and goal2_front not in goal0_pop and goal2_front not in goal1_pop:
#             goal2_neighbors = sorted(graph.neighbors(goal2_front))
#             goal2_pop.add(goal2_front)
#             for goal2_neighbor in goal2_neighbors:
#                 goal2_cost = goal2_path_cost[goal2_front] + graph.get_edge_weight(goal2_front, goal2_neighbor)
#                 if goal2_neighbor not in goal2_path_cost or goal2_cost < goal2_path_cost[goal2_neighbor]:
#                     goal2_path_cost[goal2_neighbor] = goal2_cost
#                     goal2_queue.append((goal2_cost, goal2_neighbor))
#                     goal2_prev[goal2_neighbor] = goal2_front 
#         if goal0_front in goal2_pop or goal2_front in goal0_pop:
#             if goal0_front in goal2_pop: cost = goal0_path_cost[goal0_front] + goal2_path_cost[goal0_front]
#             else: cost = goal2_path_cost[goal2_front] + goal0_path_cost[goal2_front]
#             if cost < mu02:
#                 if goal0_front in goal2_pop: best_node02 = goal0_front
#                 else: best_node02 = goal2_front
#                 mu02 = cost
#             else:
#                 found02 = True
#                 if found01 and found02 and found12:
#                     break;
#         if goal0_front in goal1_pop or goal1_front in goal0_pop: 
#             if goal0_front in goal1_pop: cost = goal0_path_cost[goal0_front] + goal1_path_cost[goal0_front]
#             else: cost = goal1_path_cost[goal1_front] + goal0_path_cost[goal1_front]
#             # print('goal0_front: ', goal0_front)
#             # print('cost: ', cost)
#             # print('mu01: ', mu01)
#             # print(goal1_pop)
#             # print(goal0_pop)
#             if cost < mu01:
#                 if goal0_front in goal1_pop: best_node01 = goal0_front
#                 else: best_node01 = goal1_front
#                 mu01 = cost
#             else:
#                 found01 = True
#                 if found01 and found02 and found12:
#                     break;
#         if goal1_front in goal2_pop or goal2_front in goal1_pop:
#                 if goal1_front in goal2_pop: cost = goal1_path_cost[goal1_front] + goal2_path_cost[goal1_front]
#                 else: cost = goal2_path_cost[goal2_front] + goal1_path_cost[goal2_front]
#                 if cost < mu12:
#                     if goal1_front in goal2_pop: best_node12 = goal1_front
#                     else: best_node12 = goal2_front
#                     mu12 = cost
#                 else: 
#                     found12 = True   
#                     if found01 and found02 and found12:
#                         break;
        
#     # print(best_node01, best_node02, best_node12)
#     # print(mu01, mu02, mu12)
#     # print(goal0_path_cost, goal0_prev)
#     # print(goal1_path_cost, goal1_prev)
    
#     path01 = []
#     path02 = []
#     path12 = []
#     if mu01 <= mu02 <= mu12 or mu02 <= mu01 <= mu12:
#         best_point = best_node01
#         while best_point:
#             path01.insert(0, best_point)
#             best_point = goal1_prev[best_point]
#         if path01:
#             path01.pop()
#         best_point = best_node01
#         while best_point:
#             path01.append(best_point)
#             best_point = goal0_prev[best_point]
#         best_point = best_node02
#         while best_point:
#             path02.insert(0, best_point)
#             best_point = goal0_prev[best_point]
#         if path02:
#             path02.pop()
#         best_point = best_node02
#         while best_point:
#             path02.append(best_point)
#             best_point = goal2_prev[best_point]
#         if path01:
#             path01.pop()
#         return path01 + path02
    
#     if mu01<= mu12 <= mu02 or mu12 <= mu01 <= mu02:
#         best_point = best_node01
#         while best_point:
#             path01.insert(0, best_point)
#             best_point = goal0_prev[best_point]
#         if path01:
#             path01.pop()
#         best_point = best_node01
#         while best_point:
#             path01.append(best_point)
#             best_point = goal1_prev[best_point]
#         best_point = best_node12
#         while best_point:
#             path12.insert(0, best_point)
#             best_point = goal1_prev[best_point]
#         if path12:
#             path12.pop()
#         best_point = best_node12
#         while best_point:
#             path12.append(best_point)
#             best_point = goal2_prev[best_point]
#         if path01:
#             path01.pop()
#         return path01 + path12
    
    
#     if mu02<= mu12 <= mu01 or mu12 <= mu02 <= mu01:
#         best_point = best_node02
#         while best_point:
#             path02.insert(0, best_point)
#             best_point = goal0_prev[best_point]
#         if path02:
#             path02.pop()
#         best_point = best_node02
#         while best_point:
#             path02.append(best_point)
#             best_point = goal2_prev[best_point]
#         best_point = best_node12
#         while best_point:
#             path12.insert(0, best_point)
#             best_point = goal2_prev[best_point]
#         if path12:
#             path12.pop()
#         best_point = best_node12
#         while best_point:
#             path12.append(best_point)
#             best_point = goal1_prev[best_point]
#         if path02:
#             path02.pop()
#         return path02 + path12
    

# def tridirectional_search(graph, goals):
     
#     res = []
#     if goals[0] == goals[1] == goals[2]:
#         return res

#     q1 = PriorityQueue()
#     q2 = PriorityQueue()
#     q3 = PriorityQueue()
#     explored1 = set()
#     explored2 = set()
#     explored3 = set()
#     edge1 = {}
#     edge2 = {}
#     edge3 = {}
#     init1 = (0, goals[0])
#     init2 = (0, goals[1])
#     init3 = (0, goals[2])
#     q1.append(init1)
#     q2.append(init2)
#     q3.append(init3)
#     path1 = {}
#     path2 = {}
#     path3 = {}
#     path1[goals[0]] = 0
#     path2[goals[1]] = 0
#     path3[goals[2]] = 0
#     mu12 = float('inf')
#     mu23 = float('inf')
#     mu31 = float('inf')
#     frontier12 = None
#     frontier23 = None
#     frontier31 = None
#     res12 = []
#     res23 = []
#     res31 = []
#     while q1 and q2 and q3:
#         print(q1, q2, q3)
#         w1, n1 = q1.top()
#         w2, n2 = q2.top()
#         w3, n3 = q3.top()
#         if w1 + w2 >= mu12 and w2 + w3 >= mu23 and w3 + w1 >= mu31:
#             break

#         w1, n1 = q1.pop()
#         w2, n2 = q2.pop()
#         w3, n3 = q3.pop()
#         explored1.add(n1)
#         explored2.add(n2)
#         explored3.add(n3)

#         for x in sorted(graph.neighbors(n1)):
#             we1 = w1 + graph.get_edge_weight(n1, x)
#             if x not in explored1 and x not in q1:
#                 path1[x] = we1
#                 q1.append((we1, x))
#                 edge1[x] = n1
#             elif x in q1:
#                 print("is it possible?       1")
#                 if path1[x] > we1:
#                     path1[x] = we1
#                     print("here is x :", x)
#                     q1.remove_node(x)
#                     q1.append((we1, x))
#                     edge1[x] = n1

#             if x in explored2:
#                 if path1[x] + path2[x] < mu12:
#                     mu12 = path1[x] + path2[x]
#                     frontier12 = x

#             if x in explored3:
#                 if path1[x] + path3[x] < mu31:
#                     mu31 = path1[x] + path3[x]
#                     frontier31 = x

#         for x in sorted(graph.neighbors(n2)):
#             we2 = w2 + graph.get_edge_weight(n2, x)
#             if x not in explored2 and x not in q2:
#                 path2[x] = we2
#                 q2.append((we2, x))
#                 edge2[x] = n2
#             elif x in q2:
#                 print("is it possible?       1")
#                 if path2[x] > we2:
#                     path2[x] = we2
#                     q2.remove_node(x)
#                     q2.append((we2, x))
#                     edge2[x] = n2

#             if x in explored1:
#                 if path1[x] + path2[x] < mu12:
#                     mu12 = path1[x] + path2[x]
#                     frontier12 = x

#             if x in explored3:
#                 if path2[x] + path3[x] < mu23:
#                     mu23 = path2[x] + path3[x]
#                     frontier23 = x

#         for x in sorted(graph.neighbors(n3)):
#             we3 = w3 + graph.get_edge_weight(n3, x)
#             if x not in explored3 and x not in q3:
#                 path3[x] = we3
#                 q3.append((we3, x))
#                 edge3[x] = n3
#             elif x in q3:
#                 print("is it possible?       1")
#                 if path3[x] > we3:
#                     path3[x] = we3
#                     q3.remove_node(x)
#                     q3.append((we3, x))
#                     edge3[x] = n3

#             if x in explored2:
#                 if path3[x] + path2[x] < mu23:
#                     mu23 = path3[x] + path2[x]
#                     frontier23 = x

#             if x in explored1:
#                 if path1[x] + path3[x] < mu31:
#                     mu31 = path1[x] + path3[x]
#                     frontier31 = x

#     def constructPath(re,frontier,edgea,edgeb,a,b):
#         r1 = []
#         r2 = []
#         r1.append(frontier)
#         cur1 = frontier
#         while cur1 != a:
#             prev1 = edgea[cur1]
#             r1.append(prev1)
#             cur1 = prev1
#         r1 = r1[::-1]

#         cur2 = frontier
#         while cur2 != b:
#             prev2 = edgeb[cur2]
#             r2.append(prev2)
#             cur2 = prev2

#         re += r1 + r2

#     constructPath(res12, frontier12, edge1, edge2, goals[0], goals[1])
#     constructPath(res23, frontier23, edge2, edge3, goals[1], goals[2])
#     constructPath(res31, frontier31, edge3, edge1, goals[2], goals[0])

#     if mu12 >= mu23 and mu12 >= mu31:
#         res = res23[:-1] + res31

#     if mu23 >= mu31 and mu23 >= mu12:
#         res = res31[:-1] + res12

#     if mu31 >= mu23 and mu31 >= mu12:
#         res = res12[:-1] + res23

#     return res
    
#export

#export

def tridirectional_search(graph, goals):
    """
    Exercise 3: Tridirectional UCS Search

    See README.MD for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        goals (list): Key values for the 3 goals

    Returns:
        The best path as a list from one of the goal nodes (including both of
        the other goal nodes).
    """
    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
#     raise NotImplementedError

    #these for init queue
    goal0, goal1, goal2 = goals
    
    goal0_queue = PriorityQueue()
    goal0_path_cost = {goal0:0}
    goal0_prev = {goal0: None}
    goal0_queue.append((0, goal0))
    goal0_pop = set()
    
    goal1_queue = PriorityQueue()
    goal1_path_cost = {goal1:0}
    goal1_prev = {goal1: None}
    goal1_queue.append((0, goal1))
    goal1_pop = set()
    
    goal2_queue = PriorityQueue()
    goal2_path_cost = {goal2:0}
    goal2_prev = {goal2: None}
    goal2_queue.append((0, goal2))
    goal2_pop = set()
    
    #make sure each node explored once
    total_pop = set()
    #these for found best common node and path
    best_node01 = None
    best_node02 = None
    best_node12 = None

    mu01 = 1e9
    mu02 = 1e9
    mu12 = 1e9
    

    
    def find_best_node(start_explored, goal_frontier, goal_explored, start_cost, goal_cost):
        mu = 1e9
        best_node = None
        for p in start_explored:
            if p in goal_frontier or p in goal_explored:
                cost = start_cost[p] + goal_cost[p]
                if cost < mu:
                    mu = cost
                    best_node = p
        return best_node, mu
    
    def abort(queue, goal_pop, path_cost, prev):
#         print("abort", queue)
        while not queue.is_empty():
            cost, front = queue.pop()
            # if front not in goal_pop:
            #     goal_pop.add(front)
            #     for p in sorted(graph.neighbors(front)):
            #         new_cost = cost + graph.get_edge_weight(front, p)
            #         if p not in path_cost or new_cost < path_cost[p]:
            #             path_cost[p] = new_cost
            #             queue.append((new_cost, p))
            #             prev[p] = front
        goal_pop.clear()
            
        
    
    if len(set(goals)) == 1:
        return []
    
    while not goal0_queue.is_empty() or not goal1_queue.is_empty() or not goal2_queue.is_empty():
        if not goal0_queue.is_empty():  
            _, goal0_front = goal0_queue.pop()
            if goal0_front not in goal0_pop:
                goal0_pop.add(goal0_front)
                if goal0_front in goal1_pop:
                    best_node01, mu01 = \
                        find_best_node(goal0_pop, goal1_path_cost, goal1_pop, goal0_path_cost, goal1_path_cost)
    #                 best_node01_, mu01_ = \
    #                     find_best_node(goal0_pop, goal1_path_cost, goal1_pop, goal0_path_cost, goal1_path_cost)
    #                 if mu01_ < mu01:
    #                     best_node01, mu01 = best_node01_, mu01_
                    if goal0_path_cost[goal0_front] < goal1_path_cost[goal0_front]:
                        abort(goal1_queue, goal1_pop, goal1_path_cost, goal1_prev)
                    else:
                        abort(goal0_queue, goal0_pop, goal0_path_cost, goal0_prev)

                if goal0_front in goal2_pop:
                    best_node02, mu02 = \
                        find_best_node(goal0_pop, goal2_path_cost, goal2_pop, goal0_path_cost, goal2_path_cost)
    #                 best_node02_, mu02_ = \
    #                     find_best_node(goal0_pop, goal2_path_cost, goal2_pop, goal0_path_cost, goal2_path_cost)
    #                 if mu02_ < mu02:
    #                     best_node02, mu02 = best_node02_, mu02_
                    if goal0_path_cost[goal0_front] < goal2_path_cost[goal0_front]:
                        abort(goal2_queue, goal2_pop, goal2_path_cost, goal2_prev)
                    else:
                        abort(goal0_queue, goal0_pop, goal0_path_cost, goal0_prev)
                goal0_neighbors = sorted(graph.neighbors(goal0_front))
                for goal0_neighbor in goal0_neighbors:
                    goal0_cost = goal0_path_cost[goal0_front] + graph.get_edge_weight(goal0_front, goal0_neighbor)
                    if goal0_neighbor not in goal0_path_cost or goal0_cost < goal0_path_cost[goal0_neighbor]:
                        goal0_path_cost[goal0_neighbor] = goal0_cost
                        goal0_queue.append((goal0_cost, goal0_neighbor))
                        goal0_prev[goal0_neighbor] = goal0_front   

        if not goal1_queue.is_empty():
            _, goal1_front = goal1_queue.pop()
#             print(".....", goal1_front)
            if goal1_front not in goal1_pop:
                goal1_pop.add(goal1_front)
                if goal1_front in goal0_pop:
                    best_node01, mu01 = \
                        find_best_node(goal1_pop, goal0_path_cost, goal0_pop, goal1_path_cost, goal0_path_cost)
    #                 best_node01_, mu01_ = \
    #                     find_best_node(goal1_pop, goal0_path_cost, goal0_pop, goal1_path_cost, goal0_path_cost)
    #                 if mu01_ < mu01:
    #                     best_node01, mu01 = best_node01_, mu01_
                    if goal1_path_cost[goal1_front] < goal0_path_cost[goal1_front]:
                        abort(goal0_queue, goal0_pop, goal0_path_cost, goal0_prev)
                    else:
                        abort(goal1_queue, goal1_pop, goal1_path_cost, goal1_prev)
                if goal1_front in goal2_pop:
                    best_node12, mu12 = \
                        find_best_node(goal1_pop, goal2_path_cost, goal2_pop, goal1_path_cost, goal2_path_cost)
    #                 best_node12_, mu12_ = \
    #                     find_best_node(goal1_pop, goal2_path_cost, goal2_pop, goal1_path_cost, goal2_path_cost)
    #                 if mu12_ < mu12:
    #                     best_node12, mu12 = best_node12_, mu12_
                    if goal1_path_cost[goal1_front] < goal2_path_cost[goal1_front]:
                        abort(goal2_queue, goal2_pop, goal2_path_cost, goal2_prev)
                    else:
                        abort(goal1_queue, goal1_pop, goal1_path_cost, goal1_prev)

                goal1_neighbors = sorted(graph.neighbors(goal1_front))
                for goal1_neighbor in goal1_neighbors:
                    goal1_cost = goal1_path_cost[goal1_front] + graph.get_edge_weight(goal1_front, goal1_neighbor)
                    if goal1_neighbor not in goal1_path_cost or goal1_cost < goal1_path_cost[goal1_neighbor]:
#                         print(goal1_front, goal1_neighbor, goal1_path_cost[goal1_front], goal1_cost, goal1_path_cost, goal1_queue)
                        goal1_path_cost[goal1_neighbor] = goal1_cost
                        goal1_queue.append((goal1_cost, goal1_neighbor))
                        goal1_prev[goal1_neighbor] = goal1_front 
                    
        if not goal2_queue.is_empty():
            _, goal2_front = goal2_queue.pop()
            if goal2_front not in goal2_pop:
                goal2_pop.add(goal2_front)
                if goal2_front in goal0_pop:
                    best_node02, mu02 = \
                        find_best_node(goal2_pop, goal0_path_cost, goal0_pop, goal2_path_cost, goal0_path_cost)
    #                 best_node02_, mu02_ = \
    #                     find_best_node(goal2_pop, goal0_path_cost, goal0_pop, goal2_path_cost, goal0_path_cost)
    #                 if mu02_ < mu02:
    #                     best_node02, mu02 = best_node02_, mu02_
                    if goal2_path_cost[goal2_front] < goal0_path_cost[goal2_front]:
                        abort(goal0_queue, goal0_pop, goal0_path_cost, goal0_prev)
                    else:
                        abort(goal2_queue, goal2_pop, goal2_path_cost, goal2_prev)
                if goal2_front in goal1_pop:
                    goal2_pop.add(goal2_front)
                    best_node12, mu12 = \
                        find_best_node(goal2_pop, goal1_path_cost, goal1_pop, goal2_path_cost, goal1_path_cost)
    #                 best_node12_, mu12_ = \
    #                     find_best_node(goal2_pop, goal1_path_cost, goal1_pop, goal2_path_cost, goal1_path_cost)
    #                 if mu12_ < mu12:
    #                     best_node12, mu12 = best_node12_, mu12_
                    if goal2_path_cost[goal2_front] < goal1_path_cost[goal2_front]:
                        abort(goal1_queue, goal1_pop, goal1_path_cost, goal1_prev)
                    else:
                        abort(goal2_queue, goal2_pop, goal2_path_cost, goal2_prev)
                
                goal2_neighbors = sorted(graph.neighbors(goal2_front))
                for goal2_neighbor in goal2_neighbors:
                    goal2_cost = goal2_path_cost[goal2_front] + graph.get_edge_weight(goal2_front, goal2_neighbor)
                    if goal2_neighbor not in goal2_path_cost or goal2_cost < goal2_path_cost[goal2_neighbor]:
                        goal2_path_cost[goal2_neighbor] = goal2_cost
                        goal2_queue.append((goal2_cost, goal2_neighbor))
                        goal2_prev[goal2_neighbor] = goal2_front 
                    
#         if goal0_front in goal2_path_cost or goal2_front in goal0_path_cost:
#             if goal0_front in goal2_path_cost: cost = goal0_path_cost[goal0_front] + goal2_path_cost[goal0_front]
#             else: cost = goal2_path_cost[goal2_front] + goal0_path_cost[goal2_front]
#             if cost < mu02:
#                 if goal0_front in goal2_path_cost: best_node02 = goal0_front
#                 else: best_node02 = goal2_front
#                 mu02 = cost
#                 count += 1
                    
#         if goal0_front in goal1_path_cost or goal1_front in goal0_path_cost: 
#             if goal0_front in goal1_path_cost: cost = goal0_path_cost[goal0_front] + goal1_path_cost[goal0_front]
#             else: cost = goal1_path_cost[goal1_front] + goal0_path_cost[goal1_front]
#             # print('goal0_front: ', goal0_front)
#             # print('cost: ', cost)
#             # print('mu01: ', mu01)
#             # print(goal1_pop)
#             # print(goal0_pop)
#             if cost < mu01:
#                 if goal0_front in goal1_path_cost: best_node01 = goal0_front
#                 else: best_node01 = goal1_front
#                 mu01 = cost
#                 count += 1
                    
#         if goal1_front in goal2_path_cost or goal2_front in goal1_path_cost:
#                 if goal1_front in goal2_path_cost: cost = goal1_path_cost[goal1_front] + goal2_path_cost[goal1_front]
#                 else: cost = goal2_path_cost[goal2_front] + goal1_path_cost[goal2_front]
#                 if cost < mu12:
#                     if goal1_front in goal2_path_cost: best_node12 = goal1_front
#                     else: best_node12 = goal2_front
#                     mu12 = cost
#                     count += 1
       
        
    print(best_node01, best_node02, best_node12)
    print(mu01, mu02, mu12)
    print(goal0_path_cost, goal0_prev)
    print(goal1_path_cost, goal1_prev)
    
    def path(p1, p2):
        print(p1, p2)
        if p1[-1] == p2[-1]:
            return p1 + p2[:-1]
        if p1[0] in p2:
            return p2
        if p1[-1] in p2:
            return p2.insert(p2.find(p1[-1]) + 1, p1[0])
        return p1 + p2
    
    path01 = []
    path02 = []
    path12 = []
    if mu01 <= mu02 <= mu12 or mu02 <= mu01 <= mu12:
        best_point = best_node01
        while best_point:
            path01.insert(0, best_point)
            best_point = goal1_prev[best_point]
        if path01:
            path01.pop()
        best_point = best_node01
        while best_point:
            path01.append(best_point)
            best_point = goal0_prev[best_point]
        best_point = best_node02
        while best_point:
            path02.insert(0, best_point)
            best_point = goal0_prev[best_point]
        if path02:
            path02.pop()
        best_point = best_node02
        while best_point:
            path02.append(best_point)
            best_point = goal2_prev[best_point]
        if path01:
            path01.pop()
        return path(path01, path02)
    
    if mu01<= mu12 <= mu02 or mu12 <= mu01 <= mu02:
        best_point = best_node01
        while best_point:
            path01.insert(0, best_point)
            best_point = goal0_prev[best_point]
        if path01:
            path01.pop()
        best_point = best_node01
        while best_point:
            path01.append(best_point)
            best_point = goal1_prev[best_point]
        best_point = best_node12
        while best_point:
            path12.insert(0, best_point)
            best_point = goal1_prev[best_point]
        if path12:
            path12.pop()
        best_point = best_node12
        while best_point:
            path12.append(best_point)
            best_point = goal2_prev[best_point]
        if path01:
            path01.pop()
        return path(path01, path12)
    
    
    if mu02<= mu12 <= mu01 or mu12 <= mu02 <= mu01:
        best_point = best_node02
        while best_point:
            path02.insert(0, best_point)
            best_point = goal0_prev[best_point]
        if path02:
            path02.pop()
        best_point = best_node02
        while best_point:
            path02.append(best_point)
            best_point = goal2_prev[best_point]
        best_point = best_node12
        while best_point:
            path12.insert(0, best_point)
            best_point = goal2_prev[best_point]
        if path12:
            path12.pop()
        best_point = best_node12
        while best_point:
            path12.append(best_point)
            best_point = goal1_prev[best_point]
        if path02:
            path02.pop()
        return path(path02, path12)

    

    


# Example usage:
graph = Graph()
graph.add_edge('o', [('z', 71), ('s', 151)])
graph.add_edge('z', [('o', 71), ('a', 75)])
graph.add_edge('a', [('z', 75), ('s', 140), ('t', 118)])
graph.add_edge('t', [('a', 118), ('l', 111)])
graph.add_edge('l', [('t', 111), ('m', 70)])
graph.add_edge('m', [('l', 70), ('d', 75)])
graph.add_edge('d', [('m', 75), ('c', 120)])
graph.add_edge('c', [('d', 120), ('r', 146), ('p', 138)])
graph.add_edge('r', [('s', 80), ('p', 97), ('c', 146)])
graph.add_edge('p', [('r', 97), ('c', 138), ('b', 101)])
graph.add_edge('s', [('a', 140), ('o', 151), ('r', 80), ('f', 99)])
graph.add_edge('f', [('s', 99), ('b', 211)])
graph.add_edge('b', [('p', 101), ('f', 211), ('g', 90), ('u', 85)])
graph.add_edge('g', [('b', 90)])
graph.add_edge('u', [('b', 85), ('h', 98), ('v', 142)])
graph.add_edge('h', [('u', 98), ('e', 86)])
graph.add_edge('e', [('h', 86)])
graph.add_edge('v', [('u', 142), ('i', 92)])
graph.add_edge('i', [('v', 92), ('n', 87)])
graph.add_edge('n', [('i', 87)])

start_node = 'h'
goal_node = 's'
result = tridirectional_search(graph, ['a', 'v', 'n'])
print(result)