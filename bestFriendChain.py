import friendNetwork

class BestFriendChain(object):
        def __init__(self, network):
                self.network = network
                self.names = network.names
                self.friendNet = list(network.friendNet)
                self.enemyNet = []
                for person in self.friendNet:
                        personConnections =[]
                        for connection in person:
                                personConnections.append((connection[0], 11 - int(connection[1])))
                        self.enemyNet.append(personConnections)

        def bellmanFord(self, source_n, goal_n):
                source = self.names[source_n]
                goal = self.names[goal_n]
                belFordCost = dict()
                belFordPred = dict()
                j = 0
                while j < len(self.names):
                        belFordCost[j] = float("inf")
                        belFordPred[j] = []
                        j = j+1
                itters = len(self.names)-1
                belFordCost[source] = 0
                while itters > 0:
                        for vertex in belFordCost.keys():
                                if belFordCost[vertex] != float("inf"):
                                        for connection in self.enemyNet[vertex]:
                                                if belFordCost[vertex] + connection[1] < belFordCost[connection[0]]:
                                                        belFordCost[connection[0]] = belFordCost[vertex] + connection[1]
                                                        belFordPred[connection[0]] = belFordPred[vertex]+[vertex]
                                                
                        itters -= 1
                return belFordPred[goal] + [goal]
                
        def printChain(self, chain):
                print "The chain is"
                for i in chain:
                        for k,v in self.names.iteritems():
                                if v == i:
                                        print k