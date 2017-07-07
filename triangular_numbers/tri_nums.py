# Mary Karroqe
# 07.04.17
# Triangular Numbers

# returns value of n-th triangular number
def nth_tri_num(n):
	return .5 * n * (n + 1)

# prints first n triangular numbers
def tri_num_series(n):
	for i in range(1, n + 1):
		val = .5 * i * (i + 1)
		print(int(val))

# prints out visual of triangular number, centered
def print_tri_num_centered(n):
	for i in range(n):
		padding = n - i
		num_nodes = i + 1
		row = (" " * padding) + ("* " * num_nodes)
		print(row)

	print("\nTriangular number", n, "is", str(int(nth_tri_num(n))) + ".\n")

# prints out visual of triangular number, left-aligned, with filled in negative space
def print_tri_num_left_a(n):
	for i in range(n):
		padding = n - i
		num_nodes = i + 1
		row = ("* " * num_nodes) + ("` " * padding)
		print(row)

	print("\nTriangular number", n, "is", str(int(nth_tri_num(n))) + ".\n")

# prints out visual of triangular number, right-aligned, with filled in negative space
def print_tri_num_right_a(n):
	for i in range(n):
		padding = n - i
		num_nodes = i + 1
		row = ("` " * padding) + ("* " * num_nodes)
		print(row)

	print("\nTriangular number", n, "is", str(int(nth_tri_num(n))) + ".\n")

print_tri_num_right_a(6)
print_tri_num_centered(6)

