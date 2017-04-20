import friendNetwork

class BestFriendChain(object):
        def __init__(self, network):
                self.network = network
                for names in self.network.names:
                        for lists in names:
                                lists[1] = 10 - lists[1]
                Dijkstra(self.network, 1, 2)

        def Dijkstra(self, network, source_n, goal_n):
                self.network = network
                self.source_n = source_n
                self.goal_n = goal_n

                
