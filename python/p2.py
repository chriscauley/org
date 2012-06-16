f = open("p2.txt","r")
text = f.read()
f.close()

lines = text.split("\n")
lines.pop()

d = {}

for l in lines:
    name,score = l.split(' ')
    if not name in d:
        d[name] = 0
    d[name] = d[name]+int(score)

for name in d:
    print name + "\t" + str(d[name])
