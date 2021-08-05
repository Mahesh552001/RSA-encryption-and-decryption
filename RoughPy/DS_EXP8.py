class Hash:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.hashtable=[[]for _ in range(self.maxsize)]
    
    def hashFunc(self,key):
        a=ord(str(key)[0])
        hash_key=a%self.maxsize
        return hash_key
    
    def insert(self,key,value):
        hash_key=self.hashFunc(key)
        bucket=self.hashtable[hash_key]
        key_exits=False
        for i,kv in enumerate(bucket):
            k,v=kv
            if key==k:
                key_exits=True
                break
        if key_exits:
            bucket[i]=((key,value))
        else:
            bucket.append((key,value))
    
    def delete(self,key):
        hash_key=self.hashFunc(key)
        bucket=self.hashtable[hash_key]
        key_exits=False
        for i,kv in enumerate(bucket):
            k,v=kv
            if key==k:
                key_exits=True
                break
        if key_exits:
            del bucket[i]
        else:
            return 'Key {} not found'.format(key)
            
    def search(self,key):
        hash_key=self.hashFunc(key)
        bucket=self.hashtable[hash_key]
        for i,kv in enumerate(bucket):
            k,v=kv
            if key==k:
                return v
        return "Not found"
    
    def printTable(self):
        for i in self.hashtable:
            print (i)
        
class Hash2:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.hashtable=[None for _ in range(self.maxsize)]
        
# =============================================================================
#     def hashFunc(self,key):
#         a=ord(str(key)[0])
#         hash_key=a%self.maxsize
#         return hash_key
# =============================================================================

    def hashFunc(self,key):
        return key%self.maxsize
    
    def insert(self,key,value):
        hash_key=self.hashFunc(key)
        key_exits=False
        for i in range(self.maxsize):
            if self.hashtable[i]==None:
                pass
            else:
                k,v=self.hashtable[i]
                if key==k:
                    key_exits=True
                    self.hashtable[i]=((key,value))
                    break
        if key_exits:
            pass
        else:
            if self.hashtable[hash_key]==None:
                self.hashtable[hash_key]=((key,value))
            else:
                inc=1
                while True:
                    if self.hashtable[(hash_key+inc)%self.maxsize]==None:
                        self.hashtable[(hash_key+inc)%self.maxsize]=((key,value))
                        break
                    inc+=1
                    
    def delete(self,key):
        key_exits=False
        for i in range(self.maxsize):
            if self.hashtable[i]==None:
                pass
            else:
                k,v=self.hashtable[i]
                if key==k:
                    key_exits=True
                    self.hashtable[i]=None
        if not key_exits:
            return 'Key {} not found'.format(key)
        
    def search(self,key):
        hash_key=self.hashFunc(key)
        if self.hashtable[hash_key]!=None:
            k,v=self.hashtable[hash_key]
            if k==key:
                return v
        for i in range(self.maxsize):
            if self.hashtable[i]==None:
                pass
            else:
                k,v=self.hashtable[i]
                if key==k:
                    return v
        return 'Key {} not found'.format(key)
    
    def printTable(self):
        for i in self.hashtable:
            print (i)
        

 