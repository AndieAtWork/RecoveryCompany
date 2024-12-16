import random
import math


class Frame:
	def __init__(self, units, x, y, width, height, celular_width, celular_height):

		self.x = x
		self.y = y

		self.cell_units =  units
		direction = random.choice(["horizontal", "vertical"])
		if direction == "horizontal":
			self.frame_width = width
			self.frame_height = height
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
		for y in range(self.frame_height):
			row = []
			for x in  range(self.frame_width):
				cell = Cell();
				row.append(cell)
			self.frame_array.append(row)
		
		self.add_celular_unit()

		self.prioritize()

		for i in range(self.cell_units - 1):
			xprint("Add range")

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

	def add_celular_unit(self, first=True, x_position=0, y_position=0):
		width = random.randint(self.min_celular_width, self.max_celular_width)
		height = random.randint(self.min_celular_height, self.min_celular_height)

		xprint("Cell width: " + str(width))
		xprint("Cell height: " + str(height))

		if (first):
			space_left_width = self.frame_width - width
			if (space_left_width <= 1):
				x_position = 0
			else:
				x_position = math.floor(space_left_width/2)

			xprint("x_position: " + str(x_position))

			space_left_height = self.frame_height - height
			if (space_left_height <= 1):
				y_position = 0
			else:
				y_position = math.floor(space_left_height/2)

			xprint("y_position: " + str(y_position))

			for y in range(y_position, y_position + height):
				for x in range(x_position, x_position + width):
					if y < 0 or x < 0 or y == self.frame_height or x == self.frame_width:
						continue
					else:
						cell = self.frame_array[y][x]
						cell.fill(x + self.x, y + self.y)


		else:
			direction = random.choice(["top-left", "top-right", "bottom-right", "bottom-left"])
			if (direction == "top-left"):
				pass
			elif (direction == "top-right"):
				pass
			elif (direction == "bottom-right"):
				pass
			elif (direction == "bottom-left"):
				pass

	def prioritize(self):
		priority = -1
		labeled = 0

		while (labeled < self.frame_width * self.frame_height):
			for y in range(self.frame_height):
				for x in range(self.frame_height):
					cell = self.frame_array[y][x]

					if cell.empty:
						xprint(str(x) + "," + str(y))
					else:
						xprint(str(x) + "," + str(y) + " -> USED")

					if (cell.empty == False and cell.priority == -1):
						print("Filled and not set")
						if (y-1 >= 0):
							top_cell = self.frame_array[y-1][x]
							if (top_cell.priority == priority):
								cell.set_priority(priority + 1)
								labeled += 1
								xprint("set")
								continue

						if (x+1 < self.frame_width):
							right_cell = self.frame_array[y][x+1]
							if (right_cell.priority == priority):
								cell.set_priority(priority + 1)
								labeled += 1
								xprint("set")
								continue

						if (y+1 < self.frame_height):
							bottom_cell = self.frame_array[y+1][x]
							if (bottom_cell.priority == priority):
								cell.set_priority(priority + 1)
								labeled += 1
								xprint("set")
								continue

						if (x-1 >= 0):
							left_cell = self.frame_array[y][x-1]
							if (left_cell.priority == priority):
								cell.set_priority(priority + 1)
								labeled += 1
								xprint("set")
								continue
					elif (cell.priority == -1):
						xprint("Not filled and not set")
						cell.set_priority(0)
						labeled += 1
						continue

			xprint("Up the priority: " + str(priority))
			priority += 1





class Cell:
	def __init__(self, empty=True, x=None, y=None):
		self.empty = empty
		self.x_position = x
		self.y_position = y
		self.category = []
		self.img =  None
		self.priority = -1
		self.cell_code = "NULL" 

	def fill(self, x, y):
		self.empty = False
		self.x_position = x
		self.y_position = y
		self.priority = 0

	def set_priority(self, priority):
		self.priority = priority

	def __str__(self):
		if self.empty == False:
			if (self.priority == -1):
				return " "
			return str(self.priority)
		else:
			return " "

def xprint(txt):
	if False:
		print(txt)

while (True):

	character = input("Enter for new frame: ")

	print("\n\n\n\n")
	#frame =  Frame(1, 0, 0, 30, 30, [10, 20], [10, 20], True)
	frame =  Frame(1, 0, 0, 8, 8, [5, 5], [5, 5], True)
	frame.print()
	print("\n\n\n\n")


