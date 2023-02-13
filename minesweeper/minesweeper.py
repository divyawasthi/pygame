import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count : 
            return self.cells 
        return set()

        # raise NotImplementedError

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        ans = set()
        if self.count == 0 : return self.cells 
        return set()

        # for i,j in list(self.cells) : 
            # if 
        # raise NotImplementedError

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # raise NotImplementedError
        if cell  in self.cells : 
            self.count -= 1 
            self.cells.remove(cell)


    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells : self.cells.remove(cell)

        # raise NotImplementedError


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def neighbours(self,cell) : 
        i,j = cell
        neighbours = set()
        for row in range(i-1,i+2) : 
            for col in range(j+1,j-2) : 
                if (row <= self.height and col <= self.width) : 
                    if (row,col) not in self.moves_made : neighbours.add((row,col))
        return neighbours

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)
        if cell not in self.safes : self.safes.add(cell)

        neighbours = self.neighbours(cell)
        neighbours -= self.safes 
        neighbours -= self.moves_made 
        sentence = Sentence(neighbours,count)
        self.knowledge.append(sentence)

        for sen in self.knowledge : 
            if sen.count == 0 : self.knowledge.remove(sen)
            safes = list(sen.known_safes())
            mines = list(sen.known_mines())
            for safe in safes : 
                self.mark_safe(safe)
            for mine in mines : 
                self.mark_mine(mine)
            
        news = sentence 
        new_knowledge = []
        for s in self.knowledge : 
            if len(s.cells) == 0  : self.knowledge.remove(s)
            elif s == news : break 
            elif s.count >= news.count : 
                ss = s.cells - news.cells 
                cc = s.count - news.count 
                new_knowledge.append(Sentence(ss,cc))
            news = s 
        self.knowledge.extend(new_knowledge)



        # raise NotImplementedError

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for move in self.safes :
            if move not in self.moves_made : 
                self.moves_made.add(move)
                return move 
        # raise NotImplementedError

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # moves = dict()
        spaces_left = (self.height*self.width) - (len(self.moves_made) + len(self.mines)) 
        if spaces_left == 0 : return None 
        basic_prob = (8-len(self.mines))/spaces_left 

        moves = {(i,j):basic_prob for i in range(self.height) for j in range(self.width) if (i,j) not in self.moves_made and (i,j) not in self.mines}

        if moves and not self.knowledge : 
            return random.choice(list(moves.keys()))
        elif moves  : 
            for sen in self.knowledge : 
                m_prob = sen.count/len(sen.cells)
                for cell in sen.cells : 
                    if moves[cell] < m_prob : moves[cell] = m_prob 
            ans = sorted([[x,moves[x]] for x in moves],key = lambda x : x[1])
            bprob = ans[0][1]
            return random.choice([item[0] for item in ans if item[1] == bprob])
            
        # raise NotImplementedError


