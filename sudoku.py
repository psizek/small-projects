#sudoku.py - a script for solving sudokus. The class contained here solves a sudoku-like structure, meaning that it will solve for cells that can not share values with cells of the same type until the first solution is attained - not necessarily the only solution. The code at the bottom describes a sudoku and prints results.

#possible future functionality:
#check for more than one solution - which'd mean running brute a few times, which could have some efficiency problems.
#generate sudoku? probably easiest solution is random fill in of values, and then subsequently checking/adding possible values until it's solved. Would need a "random generate" function.
#additional algorithms? Only one fairly simple algorithm right now to demonstrate how we'd do it.

#add a timeout function? for brute and main?

class Sudoku:
	"""
	desc: class that describes a sudoku, with methods for solving one. Cells locations are here given as tuples, although they can really be whatever you'd like.
	attributes:
	cell_list: list of all possible cell locations
	sec_list: list of all sections. A section is a list of cell locations - this would correspond to a single row, column, or box in a 'traditional' sudoku
	cell_dict: dict of actual cell values. This is typically empty or near empty initially.
	p_cell_dict: dict of possible values for a given cell. These possible values decline as the sudoku is solved.
	cell_sec_index: a dictionary which consists of {cell_location:corresponding sections}
	has_error: if the sudoku encounters an error via logical contradiction, this gets set to true and parsing is disabled.

	USAGE:
	initialization instruction:
	1) populate the sec_list. You can add a single section with add_section(section)
	2) put a list of cell locations into cell_list. This can be done with popl_from_sec_list()
	3) populate p_cell_dict. This can be done with popl_p_dict()
	4) run popl_cell_index(), which populates an index based on sec_list.

	running:
	sudokus are calculated automatically whenever a value is set, and completes upon setting enough values. If this is insufficient to solve, use main() to 1) try some other algorithms and 2) do some brute force solving.

	results:
	results are in cell_dict for each cell.
	"""

	sec_list = []
	cell_list = []
	cell_dict = {}
	p_cell_dict = {}
	cell_sec_index = {}
	has_error = False
	what_error = 0
	#METHODS

	#BUILDING

	def add_section(self,section):
		"""
		adds a section to sec_list

		:param section: a list of cell locations
		"""
		self.sec_list.append(section)

	def popl_cell_list(self):
		"""populates cell_list from cells listed in sec_list. If each cell is in at least one section, than this should populate all cells."""
		for sec in self.sec_list:
			for c in sec:
				if c not in self.cell_list:
					self.cell_list.append(c)

	def popl_p_dict(self,val_list):
		"""
		populates p_cell_dict with possibilities for each cell

		:param val_list: list of possible values that any cell can have
		"""
		for c in self.cell_list:
			self.p_cell_dict[c] = val_list

	def popl_cell_index(self):
		"""populates the cell index from the section list"""
		for c in self.cell_list:
			self.cell_sec_index[c] = []
		count = 0
		for sec in self.sec_list:
			for c in sec:
				self.cell_sec_index[c].append(count)
			count += 1


	#PARSING AND SETTING:

	def set_value(self,c,val):
		"""
		sets the value for a particular cell and updates possibilities for other cells that share a section.

		:param c: cell location
		:param val: value to set at cell location
		"""
		if self.has_error or self.is_complete(): #do not parse with errors.
			return
		if val not in self.p_cell_dict[c]:
			self.has_error = True
			self.what_error = c
			return


		self.cell_dict[c] = val
		for sec_num in self.cell_sec_index[c]:
			for rm_c in self.sec_list[sec_num]:
				self.rm_possibl(rm_c,val)
		self.p_cell_dict[c] = [val]

	def rm_possibl(self,c,val):
		"""
		removes possible cell values from the possible cell values list, and then sets value if there is only one possible value.

		:param c: cell location
		:param val: value to be removed
		"""
		if self.has_error or (c in self.cell_dict) or self.is_complete():
			return #do not parse with errors or replicate efforts.

		if val in self.p_cell_dict[c]:
			#self.p_cell_dict[c].remove(val)
			#for reasons that baffle me, the above code will remove the value from all dictionary entries. Not sure why, since testing out similar code will not yield this same problem just using the python shell prompt. Was not worth the CPU cycles vs dev time to optimize here, so replaced this with the code below.
			p_list = []
			for poss in self.p_cell_dict[c]:
				if poss != val:
					p_list.append(poss)
			self.p_cell_dict[c] = p_list

		#set value if there's only one possibility left
		if len(self.p_cell_dict[c]) == 1:
			self.set_value(c,self.p_cell_dict[c][0])
	

	#ALGORITHMS
	def pre_brute(self):
		"""
		algorithms to run to try to solve before brute forcing to a solution.
		:return bool: true if puzzle is complete, false OW
		"""
		for sec in self.sec_list:
			self.checkForSets(sec)
			if self.is_complete(): return True 
		return False


	def checkForSets(self,sec):
		"""if two (or set) of cells in the same sec share the same two (or set) number of values, then remove possible values from the rest of the pcell dict space."""
		for c in sec:
			p_vals = self.p_cell_dict[c]
			count = len(p_vals)
			match_index = []
			count_match = 0
			for c_match in sec:
				p_vals_match = self.p_cell_dict[c_match]
				if p_vals_match == p_vals:
					match_index.append(c_match)
					count_match += 1
					if count_match == count:
						for c_rm in sec:
							if c_rm not in match_index:
								for val in p_vals:
									self.rm_possibl(c_rm,val)
									if self.has_error or self.is_complete(): return

	#BRUTE FORCE

	def is_complete(self):
		"""
		checks if the sudoku is complete.
		:return bool:
		"""
		return (len(self.cell_list) == len(self.cell_dict))

	def set_poss_value(self):
		"""
		sets a possible value, even though it might not be the value.
		:return tuple: tuple of a cell location and it's possible values.
		"""
		for c in self.p_cell_dict:
			if not self.cell_dict[c]:
				self.set_value(c,self.p_cell_dict[c][0])
				return (c,self.p_cell_dict[c][0])

	def brute(self):
		"""
		brute forces until we find a logical contradiction.
		calls: main,set_poss_value,rm_possible

		"""
		new_sudoku = self
		c_and_val = new_sudoku.set_poss_value()
		new_sudoku.main()
		if new_sudoku.has_error:
			self.rm_possibl(c_and_val[1],c_and_val[2])
		else:
			self = new_sudoku

	def main(self):
		"""
		runs Sudoku class methods until sudoku is complete
		calls: brute()
		"""
		while not self.is_complete():
		#	if self.pre_brute(): break
			self.brute()
	

#solve a normal sudoku
mySudoku = Sudoku()

#here we will use tuples of x,y positions of cells as cell location identifiers. Any location identifiers can be used as long as they can key a dictionary (i.e. only immutable data types.)

#add row and column sections
for i in range(1,10):
	r_list = []
	c_list = []
	for j in range(1,10):
		r_list.append((i,j))
		c_list.append((j,i))
	mySudoku.add_section(r_list)
	mySudoku.add_section(c_list)

#add box sections, as writing these in loops is a more or less pointless exercise.
mySudoku.add_section([(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)])
mySudoku.add_section([(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)])
mySudoku.add_section([(1,7),(1,8),(1,9),(2,7),(2,8),(2,9),(3,7),(3,8),(3,9)])
mySudoku.add_section([(4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(6,1),(6,2),(6,3)])
mySudoku.add_section([(4,4),(4,5),(4,6),(5,4),(5,5),(5,6),(6,4),(6,5),(6,6)])
mySudoku.add_section([(4,7),(4,8),(4,9),(5,7),(5,8),(5,9),(6,7),(6,8),(6,9)])
mySudoku.add_section([(7,1),(7,2),(7,3),(8,1),(8,2),(8,3),(9,1),(9,2),(9,3)])
mySudoku.add_section([(7,4),(7,5),(7,6),(8,4),(8,5),(8,6),(9,4),(9,5),(9,6)])
mySudoku.add_section([(7,7),(7,8),(7,9),(8,7),(8,8),(8,9),(9,7),(9,8),(9,9)])

#complete remaining intialization
mySudoku.popl_cell_list()
mySudoku.popl_p_dict(range(1,10))
mySudoku.popl_cell_index()

#***SET SUDOKU VALUES HERE USING set_value(cell_location,value)***
#just type out numbers and :norm ImySudoku.set_value((^[la,^[la),^[A) or similar in vim
mySudoku.set_value((1,3),4)
mySudoku.set_value((1,5),1)
mySudoku.set_value((1,9),5)
mySudoku.set_value((2,1),6)
mySudoku.set_value((2,2),8)
mySudoku.set_value((2,4),4)
mySudoku.set_value((2,5),3)
mySudoku.set_value((2,7),9)
mySudoku.set_value((2,9),2)
mySudoku.set_value((3,1),5)
mySudoku.set_value((3,4),6)
mySudoku.set_value((3,9),7)
mySudoku.set_value((4,1),8)
mySudoku.set_value((4,5),7)
mySudoku.set_value((4,6),6)
mySudoku.set_value((4,7),1)
mySudoku.set_value((5,1),4)
mySudoku.set_value((5,9),3)
mySudoku.set_value((6,3),1)
mySudoku.set_value((6,4),5)
mySudoku.set_value((6,5),4)
mySudoku.set_value((6,9),6)
mySudoku.set_value((7,1),2)
mySudoku.set_value((7,6),3)
mySudoku.set_value((7,9),9)
mySudoku.set_value((8,1),1)
mySudoku.set_value((8,3),6)
mySudoku.set_value((8,5),5)
mySudoku.set_value((8,6),9)
mySudoku.set_value((8,8),2)
mySudoku.set_value((8,9),8)
mySudoku.set_value((9,1),9)
mySudoku.set_value((9,5),8)
mySudoku.set_value((9,7),5)

#***END OF SETTING VALUES***

#run brute in case not complete.
mySudoku.main()
print('Result:')
print(sorted(mySudoku.cell_dict.items()))
if mySudoku.has_error:
	print('Error in parsing Sudoku: check for mistypes in setting cells.')
