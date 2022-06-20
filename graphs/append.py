import pandas as pd


class Append:
    def __init__(self):
        return None

    def column_dictionary(self,alist):
        d = {}
        for a,b in enumerate(alist):
            d[a] = list(b.columns)
        return d

    def column_picker(self,alist,blist):
        index = 0 
        while index < len(alist):
            index2 = 0 
            found = False
            while index2 < len(blist) and not found:
                if alist[index] == blist[index2]:
                    found = True 
                else: 
                    index2 += 1
            if found:
                blist[index2] = None 
            index +=1
        for a in blist:
            if a is not None:
                alist.append(a)
        return alist  
    
    def column_create(self, alist):
        x = self.column_dictionary(alist)
        for a in range(len(x)-1):
            xx = self.column_picker(x[0], x[a+1])
        return xx
    
    def data_create(self,alist, file_name):
        columns = self.column_create(alist)
        empty = pd.DataFrame(columns=columns)
        for items in alist:
            empty = empty.append(items)
            empty.to_csv(file_name, index=False)
            
        return empty