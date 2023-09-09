def coding(arr):

    if(len(arr) < 2):
        return arr+"1"

    st = ""
    i= 0
    while(i < len(arr)):

        count = 1

        while(i < len(arr) - 1 and arr[i] == arr[i+1]):
            count += 1
            i += 1
        st+=arr[i]

        for val in str(count):
            st+=val
        i+=1

    return st

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = input()
        print(coding(arr))
