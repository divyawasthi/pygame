class Sudoku(object):
	def __init__(self,grid) : 
		self.grid = grid 
		self.solved = False
		self.ans = [] 
	
	# def empty(self):
	# 	ans = list()
	# 	for i in range(9) : 
	# 		for j in range()

	def check_all(self,num,row,col) : 
		for i in range(9):
			if self.grid[row][i] == num : return False 
		# return True
		for i in range(9) : 
			if self.grid[i][col] == num : return False 
		
		start_row,start_col = (row//3)*3,(col//3)*3
		for start in range(3) : 
			for end in range(3) : 
				if self.grid[start_row+start][start_col+end] == num : return False 
		return True 

	def reload(self):
		for pair in self.ans : 
			self.grid[pair[0]][pair[1]] = 0


	def solve(self,row,col):
		if row == 8 and col == 9 : return True 
		if col == 9 : 
			row += 1 ; col = 0
		if self.grid[row][col] > 0 : return self.solve(row,col+1)
		self.ans.append((row,col))
		for num in range(1,10) : 
			if self.check_all(num,row,col) : 
				self.grid[row][col] = num 
				if self.solve(row,col+1) : return True 
			self.grid[row][col] = 0 

		return False 
