class Hash_Table:
    def __init__(self):
        self.MAX = 15;
        self.arr = [None for i in range(self.MAX)]


    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX -1
    
    # def add(self,key,value):
    #     h = self.get_hash(key)
    #     self.arr[h] = value
    
    # def get(self,key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        del self.arr[h]


    
t = Hash_Table();
# t.add('march 3','demo')
# t.get('march 3')

t['march 3'] = 'demo'
t['jul 2'] = 'birthday'
t['apr 2'] = 'fool'
print(t.arr)
del t['jul 2']
print(t.arr)
print(t['apr 2'])