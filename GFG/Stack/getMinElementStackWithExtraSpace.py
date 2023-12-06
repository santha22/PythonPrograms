class stack:
    def __init__(self):
        self.s=[]
        self.temp = []
        self.minEle=None

    def push(self,x):
        #CODE HERE
        if not self.temp or x <= self.temp[-1]:
            self.temp.append(x)
            
        self.s.append(x)
        
        

    def pop(self):
        #CODE HERE
        if not self.s:
            return -1
            
        val = self.s.pop()
        if val == self.temp[-1]:
            self.temp.pop()
            
        return val
        

    def getMin(self):
        #CODE HERE
        if not self.temp:
            return -1
            
        return self.temp[-1]
