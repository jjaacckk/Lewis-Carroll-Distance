# HashTable.py

class DuplicateException(Exception):
    pass


class RemovalException(Exception):
    pass


def isPrime(p: int) -> bool:
    for i in range(2, (p//2) + 1):
        if p % i == 0:
            return False
    return True


class HashTable:
    BASE = 37
    START_SIZE = 11
    LOAD_FACTOR = 0.25
    
    
    def __init__(self):
        self.bucketArray = [None] * HashTable.START_SIZE
        self.numBuckets = 0
        
    
    def capacity(self) -> int:
        return len(self.bucketArray)
    
    
    def size(self) -> int:
        return self.numBuckets
    
    
    def hash(self, s: str) -> int:
        h = 0;
	
        for i in range(len(s)):
            temp = (ord(s[i]) - 97) * pow(HashTable.BASE, len(s) - 1 - i)
            h += temp % self.capacity()

        return h % self.capacity()
    
    
    def add(self, s: str) -> None:
        if self.contains(s) == True:
            raise DuplicateException("This key already exists.")
        
        if (self.size() + 1) / self.capacity() > HashTable.LOAD_FACTOR:
            self.rehash()
            
        oh = self.hash(s)
        h = oh
        
        count = 0
        while self.bucketArray[h] != None:
            h = (oh + pow(count, 2)) % self.capacity()
            count += 1
        
        self.bucketArray[h] = s
        
        self.numBuckets += 1
    
    
    def remove(self, s: str) -> None:
        if self.contains(s) == False:
            raise RemovalException("This key does not exist.")
            
        self.numBuckets -= 1
    
    
    def rehash(self) -> None:
        newPrime = (self.capacity() * 2) + 1
        
        while isPrime(newPrime) == False:
            newPrime += 2
            
        oldBucketArray = self.bucketArray
        self.bucketArray = [None] * newPrime
        
        for b in oldBucketArray:
            if b != None:
                oh = self.hash(b)
                h = oh
        
                count = 0
                while self.bucketArray[h] != None:
                    h = (oh + pow(count, 2)) % self.capacity()
                    count += 1

                self.bucketArray[h] = b
                
        
    
    
    def contains(self, s: str) -> bool:
        oh = self.hash(s)
        h = oh
        
        count = 0
        while self.bucketArray[h] != None:
            if self.bucketArray[h] == s:
                return True
            h = (oh + pow(count, 2)) % self.capacity()
            count += 1
        
        return False

