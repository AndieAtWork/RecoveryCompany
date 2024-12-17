import random
import math


class Frame:
	def __init__(self, units, x0, y0, width, height, celular_width, celular_height):

		# x0 and y0 are the absolute position where the scene should start
		# x0 + x = where to paste the scene 
		self.x = x0
		self.y = y0

		# How many blocks make up a given frame
		self.cell_units =  units

		# This is for non-square blocks
		# For example, a map made out of corridors, there will be horizontal and vertical
		direction = random.choice(["horizontal", "vertical"])
		# Depending on which is chosen, the widths and heights are switched
		if direction == "horizontal":

			# frame width and height are the max size of the frame
			self.frame_width = width
			self.frame_height = height
			# celular size varies from a minimum to a meximum
			# how many cell blocks there are is set by cell_units above
			self.max_celular_width = celular_width[1]
			self.min_celular_width = celular_width[0]
			self.max_celular_height = celular_height[1]
			self.min_celular_height = celular_height[0]
		else:
			self.frame_height = width
			self.frame_width = height
			self.max_celular_width = celular_height[1]
			self.min_celular_width = celular_height[0]
			self.max_celular_height = celular_width[1]
			self.min_celular_height = celular_width[0]

		print("Total Width: " + str(self.frame_width))
		print("Total Height: " +str(self.frame_height))

		print("Celular Width: " + str(self.min_celular_width) + " - " + str(self.max_celular_width))
		print("Celular Height: " + str(self.min_celular_height) + " - " + str(self.max_celular_height))

		self.frame_array = []
		# frame array starts with rows, which are column arrays.
		# each position is a cell. It is set to the max size of the frame: frame height and width
		for y in range(self.frame_height):
			row = []
			for x in  range(self.frame_width):
				# The cell is created empty of information
				cell = Cell();
				row.append(cell)
			self.frame_array.append(row)
		
		# Adds a block to the cells. Starts as the first one
		self.add_celular_unit()
		self.add_celular_unit(False)



	def save_in_file(self):
		pass

	def load_from_file():
		pass

	def print(self):
		print("-" * self.frame_width + "--")
		for row in range(self.frame_height):
			printed_row = "|"
			for column in range(self.frame_width):
				cell = self.frame_array[row][column]
				printed_row = printed_row + str(cell)
			printed_row = printed_row + "|"
			print(printed_row)
		print("-" * self.frame_width + "--")

	def add_celular_unit(self, first=True):
		# Size of a unit in the frame
		width = random.randint(self.min_celular_width, self.max_celular_width)
		height = random.randint(self.min_celular_height, self.min_celular_height)

		xprint("Cell width: " + str(width))
		xprint("Cell height: " + str(height))

		if (first): # First block

			# Middle point of the frame (int)
			middle_point_width = self.frame_width//2
			middle_point_height = self.frame_height//2

			# Where the block starts (upper left corner)
			# The middle point of the frame minus hald of  the size of the block
			start_point_width = middle_point_width - width//2
			start_point_height = middle_point_height - height//2

		else: 
			used_cells = self.get_all_cells()
			start_cell = random.choice(used_cells)
			
			direction = random.choice(["top-left", "top-right", "bottom-right", "bottom-left"])
			if direction == "top-left":
				start_point_height = start_cell.array_y - height
				start_point_width = start_cell.array_x - width
			elif direction == "top-right":
				start_point_height = start_cell.array_y - height
				start_point_width = start_cell.array_x + width
			elif direction == "bottom-right":
				start_point_height = start_cell.array_y + height
				start_point_width = start_cell.array_x + width
			elif direction == "bottom-left":
				start_point_height = start_cell.array_y + height
				start_point_width = start_cell.array_x - width

			print("DIRECTION")
			print(direction)
			print("CELL STARTING POINT")
			print(start_cell.array_y)
			print(start_cell.array_x)
			print("UNIT PROPERTIES")
			print(height)
			print(width)
			print("RESULT")
			print(start_point_height)
			print(start_point_width)


		# Fill in the cell square
		# go from start_point to height-width
		for y in range(start_point_height, start_point_height + height):

			for x in range(start_point_width, start_point_width + width):

				# Positions not allowed:
				# Less than 0
				# Outoside of frame
				# Leaving a margin for the walls
				if y <= 0 or x <= 0:
					continue
				if y >= self.frame_height - 1 or x >= self.frame_width - 1:
					continue
				else:
					# x,y are the position in the array
					# self.x, self.y are the position in the Scene
					cell = self.frame_array[y][x]
					cell.fill(x + self.x, y + self.y, x, y)


	def get_all_cells(self):
		array = []
		frame_height = len(self.frame_array) - 1
		frame_width = len(self.frame_array[0]) - 1
		for y in range(0, frame_height):
			for x in range(0, frame_width):
				if not self.frame_array[y][x].empty:
					array.append(self.frame_array[y][x])
		return array


class Cell:
	def __init__(self, empty=True):
		self.empty = empty

	def fill(self, x, y, array_x, array_y):
		self.empty = False
		self.x_position = x
		self.y_position = y
		self.array_x = array_x
		self.array_y = array_y

	def __str__(self):
		if self.empty == False:
			return "0"
		else:
			return " "

def xprint(txt):
	if False:
		print(txt)

while (True):

	character = input("Enter for new frame: ")

	print("\n\n\n\n")
	
	#units, x0, y0, width, height, celular_width, celular_height)
	frame =  Frame(1, 0, 0, 20, 20, [5, 10], [5, 10])
	frame.print()
	print("\n\n\n\n")


