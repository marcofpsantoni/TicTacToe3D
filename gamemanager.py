from utils import print_matrices, checker
dim = int(4)


class GameManager:

	def __init__(self):
		self.current_player = None
		self.game = None
		self.inizializza()

	def get_current_player(self):
		return self.current_player

	def inizializza(self):
		self.current_player = 1
		self.game = [[[0 for q in range(dim)] for r in range(dim)] for c in range(dim)]

	# Insert x and o in the spots

	def insert_marker(self, q=0, r=0, c=0):

		if self.game[q][r][c]==1 or self.game[q][r][c]==2:
			print("Posizione Occupata")
			return False

		self.game[q][r][c] = self.current_player
		print("\n","Situazione Attuale")
		print_matrices(self.game)
		return True

	def advance_player(self):
		self.current_player = self.current_player % 2 + 1

	def win_test(self):
		#Vincita in linea parallela a un asse cartesiano
		for i in range(dim):
			for j in range(dim):
				line1=[]
				line2=[]
				line3=[]
				for k in range(dim):
					line1.append(self.game[i][j][k])
					line2.append(self.game[k][i][j])
					line3.append(self.game[j][k][i])
				if checker(line1):
					return line1[0]
				if checker(line2):
					return line2[0]
				if checker(line3):
					return line3[0]

		#Vincita diagonale parallela a un piano cartesiano
		for j in range(dim):
			line1=[]
			line2=[]
			line3=[]
			line4=[]
			line5=[]
			line6=[]
			for i in range(dim):
				line1.append(self.game[i][i][j])
				line2.append(self.game[i][-i][j])
				line3.append(self.game[i][j][i])
				line4.append(self.game[i][j][-i])
				line5.append(self.game[j][i][i])
				line6.append(self.game[j][i][-i])
			if checker(line1):
				return line1[0]
			if checker(line2):
				return line2[0]
			if checker(line3):
				return line3[0]
			if checker(line4):
				return line4[0]
			if checker(line5):
				return line5[0]
			if checker(line6):
				return line6[0]


		#Vincita diagonale interna
			line1=[]
			line2=[]
			line3=[]
			line4=[]
			line5=[]
			line6=[]
			line7=[]
			line8=[]
			for i in range(dim):
				line1.append(self.game[i][i][i]);
				line2.append(self.game[i][i][-i]);
				line3.append(self.game[i][-i][i]);
				line4.append(self.game[i][-i][-i]);
				line5.append(self.game[-i][i][i]);
				line6.append(self.game[-i][i][-i]);
				line7.append(self.game[-i][-i][i]);
				line8.append(self.game[-i][-i][-i]);
			if checker(line1):
				return line1[0]
			if checker(line2):
				return line2[0]
			if checker(line3):
				return line3[0]
			if checker(line4):
				return line4[0]
			if checker(line5):
				return line5[0]
			if checker(line6):
				return line6[0]
			if checker(line7):
				return line7[0]
			if checker(line8):
				return line8[0]

		return 0

