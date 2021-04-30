import search
import random

class BoardState:
    """
    Implement 8x8 Board for 8 queens
    """
    def __init__(self, size=8):
        self.size = size
        self.queens = set() # store sets of tuples of coordinates of queens
    
    def __str__(self):
        s = []
        for i in range(self.size):
            line = '|'
            line += '|'.join('X' if (i, j) in self.queens else ' ' for j in range(self.size))
            line += '|'
            s.append('-' * (self.size * 2 + 1))
            s.append(line)
        s.append('-' * (self.size * 2 + 1))
        return '\n'.join(s)
    
    def __eq__(self, other):
        return self.size == other.size and self.queens == other.queens

    def __hash__(self):
        return hash(str(self.queens))
    
    def isGoal(self):
        return len(self.queens) == self.size
    
    def addQueen(self, queen_pos):
        x, y = queen_pos
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            raise Exception("Queen out of board")
        if self.isSafe(queen_pos):
            self.queens.add(queen_pos)
            return True

    def result(self, position):
        new_board = BoardState(self.size)
        queens = self.queens.copy()
        [new_board.addQueen(queen) for queen in self.queens]
        new_board.addQueen(position)
        return new_board

    def addRandomQueens(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            pos = (x,y)
            if self.addQueen(pos):
                return

    def isSafe(self, queen_pos):
        x, y = queen_pos
        for queen in self.queens:
            if x == queen[0] or y == queen[1] or abs(x - queen[0]) == abs(y - queen[1]):
                return False
        return True
    
    def legalMoves(self):
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.isSafe((i, j)):
                    moves.append((i, j))
        return moves

class EightQueensProblem(search.SearchProblem):
    def __init__(self, board):
        self.board = board

    def getStartState(self):
        return self.board

    def isGoalState(self, state):
        return state.isGoal()

    def getSuccessors(self, state):
        succ = []
        for move in state.legalMoves():
            succ.append((state.result(move), move, 1))
        return succ

    def getNextState(self, state, action):
        return state.result(action)

    def getCostOfActions(self, actions):
        return len(actions)

if __name__ == "__main__":
    board = BoardState()
    board.addRandomQueens()
    print('Add a random queen:')
    print(board)
    
    problem = EightQueensProblem(board)
    path = search.dfs(problem)
    print('DFS found a path of %d moves: %s' % (len(path), str(path)))
    curr = board
    for a in path:
        curr = curr.result(a)
        print(curr)
        input("Press return for the next state...")
