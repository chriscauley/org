import random
p1 = open("p1.txt","w")
cards = range(1,10)+["J","Q","K","A"]
suits = ["H","S","C","D"]
def rand_card():
    return str(random.choice(cards))+random.choice(suits)
for i in range(1000):
    p1.write("%s,%s\n"%(rand_card(),rand_card()))
p1.close()

p2 = open("p2.txt",'w')
names = ["bill","jane","tom","davis","samantha","johnathan","mona","angela","tony"]
aves = [92,95,60,72,54,88,80,77,91]
drift = range(-20,20)
def rand_score():
    i = random.choice(range(len(names)))
    return names[i]+" "+str(aves[i]+random.choice(drift))+"\n"
for i in range(1000):
    p2.write(rand_score())
p2.close()
