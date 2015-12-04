
ag = "kuty"

def add_a(string):
    return string + "a"

ag = add_a(ag)
print(ag)




ag2 = ["rep", "macsk", "cic", "kacs"]

for i in range(len(ag2)):
    ag2[i] = add_a(ag2[i])

print(ag2)
