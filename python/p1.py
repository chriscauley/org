f = open("p1.txt",'r')
lines = f.read().split("\n")
f.close()
lines.pop()
wins = 0
ties = 0
for l in lines:
    l = l.replace("a","d").replace("k","c").replace("q","b").replace("j","a")
    hands = l.split(",")
    if hands[0]>hands[1]:
        wins += 1
    if hands[0]==hands[1]:
        ties += 1
print wins
print ties
