count = {}
with open("poem.txt","r") as f:
    for lines in f:
        tokens = lines.split(" ")

        #print(tokens)
        length = len(tokens)
        for i in tokens:
            i = i.replace("\n",""
                               "")
            if i in count:
                #print("yes")
                count[i] += 1
            else:
                #print("No")
                count[i] = 1
            """if i in count.values():
                count[i] += 1
            else:
                count[i] = 1"""
        #print(lines)
"""length = len(lines)
print(length)"""
print(count)
"""print(count["diverged"])
print(count["in"])
print(count["I"])"""
#for i in r
