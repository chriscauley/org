f = open("p1.txt","r")
text = f.read()
f.close()

def compare(hand):
    hand = hand.replace("H","").replace("S","")
    hand = hand.replace("C","").replace("D","")
    hand = hand.replace("J","10").replace("Q","11").replace("K","12").replace("A","13")
    cards = hand.split(",")
    if int(cards[0])==int(cards[1]):
        return "tie"
    if int(cards[0])>int(cards[1]):
        return "win"

print len(text)
lines = text.split("\n")
lines.pop()
print len(lines)
print lines[0:10]

wins = 0
ties=1

for line in lines:
    status = compare(line)
    if status=="tie":
        ties +=1
    if status=="win":
        wins += 1
print wins
print ties
print len(lines)-wins -ties
