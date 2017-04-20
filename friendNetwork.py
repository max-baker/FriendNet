class Network(object):
	def __init__(self, input_stream):
		self.input_stream = input_stream
		self.names = dict()
		name = self.getNext()
		i = 0 

		#Name Dictionary
		while name != 'end':
			self.names[name]= i
			i = i +1
			name = self.getNext()

		#Initialize Adjacency List
		j = len(self.names)
		self.friendNet = []
		while j > 0:
			self.friendNet.append([])
			j = j-1


		#Adjacency list
		name1 = self.getNext()
		while name1 != 'end':
			name2 = self.getNext()
			strength = self.getNext()
			self.friendNet[self.names[name1]].append((self.names[name2],strength) )
			name1 = self.getNext()

	def checkName(self, user):
		if user in self.names:
			print ("Exists")
		else:
			print ("Does not Exist")

	def checkConnection(self, name1, name2):
		user1 = self.names[name1]
		user2 = self.names[name2]
		for p in self.friendNet[user1]:
			for q in p:
				if p[0]==user2:
					print (p[1])
					return
		print ("No connection")
		
	def getModeScore(self, name):
		person = self.names[name]
        theModeScore = ModeScore(self.person, self.friendNet)


	#helper functions:
	def getNext(self):
		name = ''
		while self.peek(1) != ' ' and self.peek(1) != '\n' and self.peek(1) != '':
			name = name + self.read(1)
		self.read(1)
		return name

	def read(self, i):
		return self.input_stream.read(i)

	def peek(self, i):
		pos = self.input_stream.tell()
		symbol = self.input_stream.read(i)
		self.input_stream.seek(pos)
		return symbol


