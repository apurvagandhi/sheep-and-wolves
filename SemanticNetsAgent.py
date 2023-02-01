# Apurva Gandhi
# Mini-Project 1: Sheep & Wolves (Spring 2023)
# KBAI - Georgia Tech
# 01/29/2023

from collections import deque

class SemanticNetsAgent:

    def __init__(self):
        pass

    def solve(self, initial_sheep, initial_wolves):
        # Add your code here! Your solve method should receive
        # the initial number of missionaries and cannibals as integers,
        # and return a list of 2-tuples that represent the moves
        # required to get all missionaries and cannibals from the left
        # side of the river to the right.
        #
        # If it is impossible to move the animals over according
        # to the rules of the problem, return an empty list of
        # moves.

        class State:
            # constructor. 
            # It is called when an object of the class is created, and it is used to initialize the attributes of the object.
            def __init__(self, left_sheep, left_wolves, right_sheep, right_wolves, boat_position):
                self.left_sheep = left_sheep
                self.left_wolves = left_wolves
                self.right_sheep = right_sheep
                self.right_wolves = right_wolves
                self.boat_position = boat_position
                self.parent = None

            #It is checking if two instances of the class are equal or not based on these attributes.
            def __eq__(self, other):
                return (self.left_sheep == other.left_sheep and self.left_wolves == other.left_wolves and
                        self.right_sheep == other.right_sheep and self.right_wolves == other.right_wolves and
                        self.boat_position == other.boat_position)
                
            # This method is checking if the current state of the object is a goal state.
            # A goal state is defined as having all the sheep and wolves on the right bank of the river, 
            # with the boat also on the right bank
            def goal_state(self):
                if (self.left_sheep == 0 and self.left_wolves == 0 and self.right_sheep == initial_sheep 
                        and self.right_wolves == initial_wolves and self.boat_position == "right"):
                    return True
                else:
                    return False
                
            # This method is used to check if the current state of the game is valid or not.
            def is_valid_state(self):
                # If there are sheep on the left bank and the number of wolves is greater than the number of sheep, it returns False.
                # If there are sheep on the right bank and the number of wolves is greater than the number of sheep, it returns False.
                # If the number of left or right sheep is less than 0, it returns False.
                # If the number of left or right wolves is less than 0, it returns False.
                if ((self.left_sheep != 0 and self.left_wolves > self.left_sheep) 
                    or (self.right_sheep != 0 and self.right_wolves > self.right_sheep) 
                    or self.left_sheep < 0 or self.left_wolves < 0 or self.right_sheep < 0 or self.right_wolves < 0):
                    return False
                else:
                    return True
                
        # successors that takes in a current state object
        # This function generates a list of possible next states ('successor') that can be reached from the current state.
        def successors(current_state):
            successor = []
            # Five possible moves: Move 2 sheeps, or 2 wolves, or 1 sheep + 1 wolve or 1 wolve only, or 1 sheep only
            possible_moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
            # If the boat is on the left side, it loops through the possible moves, 
            # and for each move, it creates a new state object, by subtracting the values of the move from the left side sheep and wolves, 
            # and adding the values of the move to the right side sheep and wolves, and sets the boat position to the right side
            if current_state.boat_position == "left":
                for move in possible_moves:
                    new_state = State(current_state.left_sheep - move[0], current_state.left_wolves - move[1],
                                       current_state.right_sheep + move[0], current_state.right_wolves + move[1], "right")
                    # If the new state is valid, it is added to the 'successor' list and 
                    # the 'parent' attribute of the new state object is set to the current state.
                    if new_state.is_valid_state():
                        successor.append(new_state)
                        new_state.parent = current_state
            # If the boat is on the right side, the loop is the same but 
            # this time it subtracts values from the right side sheep and wolves and adds them to the left side sheep and wolves, 
            # and sets the boat position to the left side.
            else:  
                for move in possible_moves:
                    new_state = State(current_state.left_sheep + move[0], current_state.left_wolves + move[1],
                                       current_state.right_sheep - move[0], current_state.right_wolves - move[1], "left")
                    if new_state.is_valid_state():
                        successor.append(new_state)
                        new_state.parent = current_state
            return successor
        
        # Implementation of the Breadth-First Search (BFS) algorithm.
        # The bfs algorithm is an algorithm used for traversing and searching a graph in a breadthward motion. 
        # It starts at the tree root, and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
        def bfs():  
            # It first creates an initial state object with a given number of sheeps, wolves, and the boat is on left side. This will be the root node
            initial_state = State(initial_sheep, initial_wolves, 0, 0, "left")
            # if initial state is the goal state it return the initial state
            if initial_state.goal_state():
                return initial_state
            # It creates an empty queue
            queue = deque([])
            #  An empty list for visited states
            visited = []
            # append the initial state to the queue
            queue.append(initial_state)
            # The while loop will continue until the queue is empty.
            while queue:
                # In each iteration, it removes the leftmost state from the queue (node) and checks 
                # if it's the goal state, if it is, it returns the node
                node = queue.popleft()
                if node.goal_state():
                    return node
                # it adds the node to the visited list 
                visited.append(node)
                # Gets the children of the node (possible next states) by calling the successors function on the node.
                node_children = successors(node)
                # For each child in the children, it checks if the child is already in the visited list or the queue, 
                # if not, it appends the child to the queue.
                for child in node_children:
                    if (child not in visited) and (child not in queue):
                        queue.append(child)
            # If the loop completes and the queue is empty, the function returns None, meaning that no solution was found.
            return None

        # find the moves that were made to reach the final goal state, starting from the final goal state, solution 
        def find_moves(result):
            path = []
            final_path = []
            result_parent = result.parent
            #  Traversing the parent pointers of the result object and the objects it points to, and 
            # For each traversal, calculates the difference in the number of sheep and wolves between the current state and its parent.         
            while result_parent:
                move = (abs(result.left_sheep - result_parent.left_sheep),
                        abs(result.left_wolves - result_parent.left_wolves))
                # These differences are then appended to the path list, which represents the moves made
                path.append(move)
                result = result_parent
                result_parent = result.parent
            # The final path is  constructed by reversing the order of the path list and storing it in final_path
            for i in range(len(path)):
                final_result = path[len(path) - 1 - i]
                final_path.append(final_result)
            return final_path

        # Checking if a solution exists for the problem using the bfs() function.
        solution = bfs()
        #  If a solution is found, it calls the find_moves() function to retrace the steps taken to reach the solution and returns the list of moves as the final output. 
        if solution:
            return find_moves(solution)
        # If no solution is found, it returns an empty list.
        else:
            return []