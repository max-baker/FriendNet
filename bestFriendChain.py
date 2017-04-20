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

        def Dijkstra(self, source_n, goal_n):
                source = self.names[source_n]
                goal = self.names[goal_n]
                visited = dict()
                minPriorityQueue = dict()
                predecessors = dict()
                minPriorityQueue[source] = 0
                while goal not in visited.keys():
                        currNode = self.shortestNode(minPriorityQueue)

        def shortestNode(self, myDict):
                currSmallest = myDict[myDict.keys()[0]]
                for i in myDict:
                        if currSmallest[1] < i[1]:
                                currSmallest = i


                
