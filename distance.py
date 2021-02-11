# distance.py

from HashTable import HashTable
from queue import SimpleQueue


def formatPath(w1: str, w2: str, d: dict):
    path = w2
    current = w2
    length = 0
    
    while current != w1:
        current = d[current]
        path = current + " --> " + path
        length += 1
        
    return (path, length)


def distance(w1: str, w2: str, words: HashTable) -> str:
    d = dict()
    q = SimpleQueue()
    current = ""
    temp = ""
    
    q.put(w1)
    d[w1] = w1
    
    while q.empty() == False:
        current = q.get()
        
        for letter in range(len(current)):
            temp = current
            
            for i in range(97,123):
                temp = temp[:letter] + chr(i) + temp[letter + 1:]
                
                if words.contains(temp) == True:
                    if d.get(temp) == None:
                        d[temp] = current
                        
                        if temp == w2:
                            return formatPath(w1, w2, d)
                        
                        q.put(temp)
    
    
    return ("", -1)



def run():
    ht = HashTable()
    
    # words_alpha.txt from https://github.com/dwyl/english-words/blob/master/words_alpha.txt
    f = open("./words_alpha.txt", "r")
    for line in f:
        ht.add(line.strip())
    
    
    print("Lewis Carroll Distance")
    print("*press '!q' to quit")
    word1 = ""
    word2 = ""
    
    while True:
        print()
        word1 = input("enter first word: ")
        if word1 == "!q":
            break
        
        word2 = input("enter second word: ")
        if word2 == "!q":
            break
            
        dist = distance(word1, word2, ht)
        
        if dist[0] == "":
            print("no path found with current dict")
        else:
            print("distance: ", dist[1])
            print(dist[0])
        
        
    print("\ngoodbye.")


if __name__ == "__main__":
    run()

    