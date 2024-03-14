class Trienode:
    def __init__(self):
        self.alphabet=[None]*26
        self.isEnd=False

class Trie:
    def __init__(self):
        self.root=Trienode()
        
    def insertkey(self,word):
        p=self.root
        for i in word:
            index=ord(i)-97
            if not p.alphabet[index]:
                p.alphabet[index]=TrieNode()
            p=p.alphabet[index]
        p.isEnd=True    
            

    def searchkey(self,word):
        p=self.root
        for i in word:
            index=ord(i)-97
            if not p.alphabet[index]:
                return False
            p=p.alphabet[index]
         if p.isEnd==False:
             return False      
         return True   # or return simply (p.isEnd)
            




        
        
    
        
