import search

class WaterJug:
    def __init__(self, capacity, water):
        self.water = water
        self.capacity = capacity
    
    def __str__(self):
        return f"({self.water}/{self.capacity})"

    def __hash__(self):
        return hash(self.water + 13 * self.capacity)

    def __eq__(self, other):
        return self.water == other.water and self.capacity == other.capacity

    def isEmpty(self):
        return self.water == 0

    def isFull(self):
        return self.water == self.capacity
    
    def pour_in(self, water):
        remainder = max(self.water + water - self.capacity, 0)
        self.water = min(self.water + water, self.capacity)

        # Return water's remainder
        return remainder
    
    def pour_to(self, other_jug):
        self.water = other_jug.pour_in(self.water)
    
    def copy(self):
        return WaterJug(self.capacity, self.water)

class WaterJugsState:
    def __init__(self, jug_list):
        jug1, jug2, jug3 = jug_list
        self.jugs = [jug1, jug2, jug3]
    
    def __str__(self):
        return ' | '.join(str(jug) for jug in self.jugs)
    
    def __eq__(self, other):
        return self.jugs == other.jugs
    
    def __hash__(self):
        return sum(hash(jug) for jug in self.jugs)
    
    def isGoal(self, goal_state):
        return self == goal_state
    
    def legalMoves(self):
        moves = []
        for i in range(3):
            if self.jugs[i].isEmpty(): continue
            for j in range(3):
                if i == j or self.jugs[j].isFull(): continue
                moves.append((i, j))
        return moves
    
    def result(self, action):
        initial_jug, destination_jug = action
        new_state = WaterJugsState([jug.copy() for jug in self.jugs])
        new_state.jugs[initial_jug].pour_to(new_state.jugs[destination_jug])
        return new_state
    
class WaterJugsProblem(search.SearchProblem):
    def __init__(self, initial_state, goal_state):
        self.current_state = initial_state
        self.goal_state = goal_state
    
    def getStartState(self):
        return self.current_state

    def isGoalState(self, state):
        return state.isGoal(goal_state)

    def getSuccessors(self, state):
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActionSequence(self, actions):
        return len(actions)
        
if __name__ == '__main__':
    inital_state = WaterJugsState([WaterJug(12,12),WaterJug(8,0),WaterJug(5,0)])
    goal_state = WaterJugsState([WaterJug(12,6),WaterJug(8,1),WaterJug(5,5)])

    problem = WaterJugsProblem(inital_state, goal_state)
    actions = search.brfs(problem)
    print('Found a path of %d moves: %s' % (len(actions), str(actions)))
    print('Initial:')
    print(f"{inital_state}")
    temp = inital_state 
    for action in actions:
        temp = temp.result(action)
        print(f"\nPour from cup {action[0] + 1} to cup {action[1] + 1}:")
        print(f'{temp}')