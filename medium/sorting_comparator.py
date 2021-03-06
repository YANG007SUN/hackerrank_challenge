# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def comparator(a, b):
        if a.score<b.score:
            return 1
        elif a.score>b.score:
            return -1
        elif a.score==b.score:
            if a.name<b.name:
                return -1
            elif a.name>b.name:
                return 1
            else:
                return 0
        else:
            return 0

n = int(input())
data =[]
for i in range(n):
    name, score = input().split()
    data.append(Player(name,score))

sorted_data = sorted(data, key=cmp_to_key(Player.comparator))
for i in sorted_data:
    print(i.name, i.score)