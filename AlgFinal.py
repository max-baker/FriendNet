import friendNetwork
import sys

def main(filename):
	file_stream = open(filename, 'r')
	myNet = friendNetwork.Network(file_stream)
	prompt = raw_input('What do you want to do? (1:"user exists" / 2:"connection" / 3:"quit") : ')
	while(prompt != "3"):
		if prompt == "1":
			user = raw_input("What User: ")
			myNet.checkName(user)
		elif prompt == "2":
			name1 = raw_input("First Name: ")
			name2 = raw_input("Second Name: ")
			myNet.checkConnection(name1, name2)
		else:
			print "Please enter a command"
		prompt = raw_input('What do you want to do? (1:"user exists" / 2:"connection" / 3:"quit") : ')
	print "Thanks!"
main(sys.argv[1])