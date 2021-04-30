import search

class RiverCrossingState:
    CHARS = ["Farmer", "Wolf", "Goat", "Cabbage"]

    def __init__(self):
        """
        List represents status of 4 characters
        1 and 0 represent two sides of the river
        """
        self.character = [1, 1, 1, 1]      # [Farmer, Wolf, Goat, Cabbage]
    
    def __eq__(self, other):
        return self.character == other.character
    
    def __hash__(self):
        return hash(str(self.character))
    
    def __str__(self):
        result = []
        r1 = '-'.join(char if bit else '-'*len(char) for bit, char in zip(self.character, self.CHARS))
        r2 = '-'.join(char if bit else '-'*len(char) for bit, char in zip(self.otherSide(), self.CHARS))
        result.append('\n')
        result.append(r1)
        result.append(r2)
        result.append('\n')

        return "\n".join(result)
    
    def isGoal(self):
        return self.character == [0, 0, 0, 0]
    
    def otherSide(self):
        return list(map(lambda x: int(not x), self.character))
    
    def isSafe(self):
        # Goat and Cabbage cannot be together without Farmer, Wolf and Goat cannot be together withput Farmer
        if (self.character[2] == self.character[3] and self.character[0] != self.character[2]) or (self.character[1] == self.character[2] and self.character[0] != self.character[1]):
            return False

        return True
    
    def legalMoves(self):
        return [i for i, bit in enumerate(self.character) if self.character[i] == self.character[0] and self.result(i).isSafe()]
    
    def result(self, char_idx):
        new_game = RiverCrossingState()
        new_game.character = self.character.copy()

        if new_game.character[0] == 1:
            new_game.character[0] = 0
            new_game.character[char_idx] = 0
        else:
            new_game.character[0] = 1
            new_game.character[char_idx] = 1

        return new_game

class RiverCrossingProblem(search.SearchProblem):
    def __init__(self, game_state):
        self.start_state = game_state

    def getStartState(self):
        return self.start_state

    def isGoalState(self, state):
        return state.isGoal()

    def getSuccessors(self, state):
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActionSequence(self, actions):
        return len(actions)

if __name__ == "__main__":
    puzzle = RiverCrossingState()
    
    problem = RiverCrossingProblem(puzzle)
    print('A random puzzle:')
    print(puzzle)
    actions = search.bfs(problem)
    print('BFS found a path of %d moves: %s' % (len(actions), str(actions)))
    
    curr = puzzle
    for action in actions:
        input("Press return for the next state...")   # wait for key stroke
        curr = curr.result(action)
        print(curr)