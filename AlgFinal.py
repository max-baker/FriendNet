import friendNetwork
import bestFriendChain
import sys

def main(filename):
	file_stream = open(filename, 'r')
	myNet = friendNetwork.Network(file_stream)
	chainFinder = bestFriendChain.BestFriendChain(myNet)
	prompt = raw_input('What do you want to do? (1:"user exists" / 2:"connection" / 3: "Best Friend Chain" / 4:"quit") : ')
	while(prompt != "4"):
		if prompt == "1":
			user = raw_input("What User: ")
			myNet.checkName(user)
		elif prompt == "2":
			name1 = raw_input("First Name: ")
			name2 = raw_input("Second Name: ")
			myNet.checkConnection(name1, name2)
		elif prompt == "3":
			chainFinder.Dijkstra("Wang", "Zhang")
			name1 = raw_input("First Name: ")
			name2 = raw_input("Second Name: ")
			chainFinder.Dijkstra(name1, name2)
		else:
			print "Please enter a command"
		prompt = raw_input('What do you want to do? (1:"user exists" / 2:"connection" / 3: "Best Friend Chain" / 4:"quit") : ')
	print "Thanks!"
main(sys.argv[1])