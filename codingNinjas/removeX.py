def removeX(string):
    if len(string) == 0:
        return ""
    if string[0] == 'x':
        return removeX(string[1:])
    return string[0] + removeX(string[1:])

string = input()
print(removeX(string))
