class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,m,ths):
        self.size = size
        self.pre = []
        self.table = [None for i in range(size)]
        self.maxCollision = m
        self.ths = ths
        self.prime = [2]
    
    def rehash(self):
        self.size=self.addPrime(2*self.size,self.prime[-1]+1)
        self.table = [None for i in range(self.size)]
        
        for i in self.pre:
            index = i%self.size
            realIndex  = index
            col = 0
            while self.table[index] != None:
                col+=1
                print("collision number",col,"at",index)
                if col == self.maxCollision:break
                index = (realIndex+col**2)%self.size
            if self.table[index] == None:self.table[index] = i
    
    def addPrime(self,data,p):
        if data < self.prime[-1]:return self.prime[-1]
        isPrime = True
        for i in self.prime:
            if i >= int(data)/2:break
            if p%i==0:
                isPrime = False
                break
        if isPrime:self.prime.append(p)
        return self.addPrime(data,p+1)

    def insert(self,data):
        print("Add :",data)
        index = data%self.size
        realIndex  = index
        col = 0
        while self.table[index] != None:
            col+=1
            print("collision number",col,"at",index)
            if col == self.maxCollision:
                print("****** Max collision - Rehash !!! ******")
                self.rehash()
                index = data%self.size
                break
            index = (realIndex+col**2)%self.size
        self.pre.append(data)
        if len(self.pre)*100/self.size >= self.ths:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
            index = data%self.size
        else:self.table[index] = data
        
    def printTable(self):
        for i in range(self.size):
            print("#"+str(i+1)+"	",end="")
            if self.table[i] == None:print(None)
            else:print(self.table[i])
        print("----------------------------------------")

print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")
h = hash(int(inp[0].split()[0]),int(inp[0].split()[1]),int(inp[0].split()[2]))
print("Initial Table :")
h.printTable()
for i in inp[1].split():
    h.insert(int(i))
    h.printTable()