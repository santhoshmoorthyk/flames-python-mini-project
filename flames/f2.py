import f1
class main:
    def __init__(self):
        y=rough1.t()
        self.s=len(y.s())
        print(self.s)
    def flames(self):
        d=['Friends','Lovers','Affection','Marriage','Enemies','Siblings']
        i=0
        while len(d)>1:
            for _ in range(self.s-1):
                i+=1
                if i>=len(d):
                    i=0
            d.pop(i)
            if i>=len(d):
                i=0
        print(d[0])
                   
u=main()
u.flames()    
    