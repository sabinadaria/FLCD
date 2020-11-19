class FA:
    def __init__(self):
        self.Q = [] #finite state
        self.E = [] #finite alphabet
        self.q0 = "" #initial state
        self.F = "" #set of final state
        self.S = {}  # transition function
        self.readFile()



    def readFile(self):
        filename="file.txt"
        file = open(filename,"r")
        self.Q = file.readline().split(" ")
        self.Q[-1] = self.Q[-1].strip("\n")

        self.E = file.readline().split(" ")
        self.E[-1] = self.E[-1].strip("\n")

        self.q0 = file.readline()

        self.F = file.readline()

        for line in file:
            elem=line[:-1].split(" ")
            if(len(elem)>2):
                self.S[elem[0],elem[1]]=elem[2]



    def isDFA(self):
        for i in self.S.keys():
            for j in self.S.keys():
                if self.S[i] == self.S[j]:
                    if i[0] == j[0] and i[1] != j[1]:
                        return False
        return True



    def printMeniu(self):
        print()
        print("1. Display states")
        print("2. Display the alphabet")
        print("3. Display initial state")
        print("4. Display final states")
        print("5. Display transitions")
        print("6. Verify DFA")


    def start(self):
        c=-1
        while c!="0":
            self.printMeniu()
            c=input(" ")
            if c=="1":
                for q in self.Q:
                    print(q)
            elif c=="2":
                for e in self.E:
                    print(e)
            elif c=="3":
                print(self.q0)
            elif c=="4":
                print(self.F)
            elif c=="5":
                for k in self.S:
                    print(k[0]+"->"+k[1]+":"+self.S[k[0],k[1]])
            elif c == "6":
                if self.isDFA() is True:
                    print("It is DFA")
                else:
                    print("It is not DFA")


fa=FA()
fa.start()



