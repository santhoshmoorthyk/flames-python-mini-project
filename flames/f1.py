class t:
    def __init__(self):
        j=input('enter first name:').strip().replace(" ","").lower()
        self.x=list(j)
        c=input('enter second name:').strip().replace(" ","").lower()
        self.y=list(c)
    def s(self):
        h=self.x.copy()
        f=self.y.copy()
        q=0
        while q<len(h):
            if h[q] in f:
                f.remove(h[q])
                h.pop(q)
               
                #h=h.replace(self.x[q],'')
            else:
                q+=1
        return h+f  