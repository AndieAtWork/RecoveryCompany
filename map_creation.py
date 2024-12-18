import random
import math


class Frame:
	def __init__(self, units, x0, y0, width, height, celular_width, celular_height, safety_margin):

		# x0 and y0 are the absolute position where the scene should start
		# x0 + x = where to paste the scene 
		self.x = x0
		self.y = y0

		# minimum closeness between units, the larger, the most likely to look like a square
		self.safety_margin = safety_margin

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

		xprint("Total Width: " + str(self.frame_width))
		xprint("Total Height: " +str(self.frame_height))

		xprint("Celular Width: " + str(self.min_celular_width) + " - " + str(self.max_celular_width))
		xprint("Celular Height: " + str(self.min_celular_height) + " - " + str(self.max_celular_height))

		self.frame_array = []
		# frame array starts with rows, which are column arrays.
		# each position is a cell. It is set to the max size of the frame: frame height and width
		for y in range(self.frame_height):
			row = []
			for x in  range(self.frame_width):
				# The cell is created empty of information
				cell = Cell(self.frame_array);
				row.append(cell)
			self.frame_array.append(row)
		
		# Adds a block to the cells. Starts as the first one
		self.add_celular_unit()
		for i in range(0, self.cell_units - 1):
			self.add_celular_unit(False)



	def save_in_file(self):
		pass

	def load_from_file():
		pass

	# Prints the scene
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

	# Adds another unit. Can be the first
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
			
			# the direction in which the unit will be written
			# safety margin is how close the can be minimum
			direction = random.choice(["top-left", "top-right", "bottom-right", "bottom-left"])
			if direction == "top-left":
				start_point_height = start_cell.array_y - height + self.safety_margin
				start_point_width = start_cell.array_x - width + self.safety_margin
			elif direction == "top-right":
				start_point_height = start_cell.array_y - height + self.safety_margin
				start_point_width = start_cell.array_x - self.safety_margin
			elif direction == "bottom-right":
				start_point_height = start_cell.array_y - self.safety_margin
				start_point_width = start_cell.array_x - self.safety_margin
			elif direction == "bottom-left":
				start_point_height = start_cell.array_y - self.safety_margin
				start_point_width = start_cell.array_x - width +  self.safety_margin

			xprint("DIRECTION")
			xprint(direction)
			xprint("CELL STARTING POINT")
			xprint(start_cell.array_y)
			xprint(start_cell.array_x)
			xprint("UNIT PROPERTIES")
			xprint(height)
			xprint(width)
			xprint("RESULT")
			xprint(start_point_height)
			xprint(start_point_width)


		# Fill in the cell square
		# go from start_point to height-width
		for y in range(start_point_height, start_point_height + height):

			for x in range(start_point_width, start_point_width + width):

				# Positions not allowed:
				# Less than 0
				# Outside of frame
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


	# To chose where to start the new unit, all ocupied cells SO FAR
	def get_all_cells(self):
		array = []
		frame_height = len(self.frame_array) - 1
		frame_width = len(self.frame_array[0]) - 1
		for y in range(0, frame_height):
			for x in range(0, frame_width):
				if not self.frame_array[y][x].empty:
					array.append(self.frame_array[y][x])
		return array

	def add_entrance(direction):
		array = []
		frame_height = len(self.frame_array) - 1
		frame_width = len(self.frame_array[0]) - 1
		for y in range(0, frame_height):
			for x in range(0, frame_width):
				cell = self.frame_array[y][x]
				if cell.empty:
					continue

				if direction == "up":
					pass
				elif direction == "down":
					pass
				elif direction == "right":
					pass
				elif direction == "left":
					pass


class Cell:
	def __init__(self, frame, empty=True):
		self.frame_array = frame
		self.empty = empty

	def fill(self, x, y, array_x, array_y):
		# When filled, empty is False
		self.empty = False
		self.x_position = x # position in the game interface
		self.y_position = y
		self.array_x = array_x # position in the array
		self.array_y = array_y

	def get_positioning(self, direction):
		if direction == "up":

			#neighbour1 = 
			#neighbour2 = 
		elif direction == "down":
			pass
		elif direction == "right":
			pass
		elif direction == "left":
			pass

	def __str__(self):
		if self.empty == False:
			return "0"
		else:
			return " "

# testing
def xprint(txt):
	if False:
		print(txt)

while (True):

	character = input("Enter for new frame: ")

	print("\n\n\n\n")
	
	#units, x0, y0, width, height, celular_width, celular_height, safety_margin)
	frame =  Frame(3, 0, 0, 35, 35, [10, 20], [10, 20], 3)
	frame.print()
	print("\n\n\n\n")


