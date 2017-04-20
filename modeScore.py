import friendNetwork

class ModeScore(object):
        def __init__(self, person_i, network):
                self.person_i = person_i
                self.network = network
                self.mode_score = self.get_scores(self.person_i, self.network)
                print(self.mode_score)

        def get_scores(self, person_i, network):
                self.person_i = person_i
                self.network = network
                self.scores = []

                for people in network:
                        for connections in people:
                                if connections[0] == self.person_i:
                                        self.scores.append(connections[1])
                self.scores = self.merge_sort(self.scores)

                self.mode_score = self.scores[0]
                self.mode_score_count = 1
                self.curr_count = 1

                for i in range(1, len(self.scores)):
                        if self.scores[i] == self.scores[i-1]:
                                self.curr_count += 1
                        else:
                                self.curr_count = 0
                        if self.mode_score == self.scores[i]:
                                self.mode_score_count += 1
                        elif self.mode_score_count <= self.curr_count:
                                self.mode_score = self.scores_i
                                self.mode_score_count = self.curr_count
                return self.mode_score


        def merge_sort(self, scores):
          #base case
                if len(scores) == 1:
                        return scores
                left = self.merge_sort(scores[:(len(scores)//2)])
                right = self.merge_sort(scores[(len(scores)//2):])

                return self.merge(left, right)

        def merge(self, left, right):
                new_arr = []

                #while left and right still have elements to compare
                while len(left) > 0 and len(right) > 0:
                        #compare the first elem of left and right
                        if left[0] < right[0]:
                                new_arr.append(left[0])
                                del left[0]
                        else:
                                new_arr.append(right[0])
                                del right[0]

                #add the remaining elements from either left or right
                for index in range(len(left)):
                        new_arr.append(left[index])
                for index in range(len(right)):
                        new_arr.append(right[index])

                return new_arr

                
