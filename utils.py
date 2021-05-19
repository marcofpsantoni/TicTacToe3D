# Utilities for matrices

def print_matrices(d3):
	for q in range(len(d3)):
		print_matrix(d3[q])
		print("")

def print_matrix(mat):
	for r in range(len(mat)):
		print(mat[r]);

def checker(line):
	return (line[0]!=0) and line.count(line[0])==len(line)