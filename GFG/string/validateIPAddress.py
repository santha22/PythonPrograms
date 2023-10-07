def isValid(s):
    # code here
    parts = s.split(".")
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return 0
    # Check each part for validity
    for part in parts:

        # Check if the part is empty or has leading zeros
        if not part or (len(part) > 1 and part[0] == "0"):
            return 0

        # Check if the part is an integer in the range [0, 255]
        if not part.isdigit():
            return 0

        num = int(part)
        if num < 0 or num > 255:
            return 0

    return 1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
