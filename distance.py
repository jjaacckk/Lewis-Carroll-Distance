# distance.py


from queue import SimpleQueue
import sys, json


def formatPath(path: list) -> str:
    return " --> ".join(path)


def getPath(w1: str, w2: str, d: dict) -> (int, list):
    path = [w2]
    current = w2
    length = 0
    
    while current != w1:
        current = d[current]
        path.append(current)
        length += 1
        
    path.reverse()    
    return (length, path)


def distance(w1: str, w2: str, words: set) -> (int, list):
    d = dict()
    q = SimpleQueue()
    current = ""
    temp = ""
    
    q.put(w1)
    d[w1] = w1
    
    if w1 == w2:
        return (0, [w1])
    
    while q.empty() == False:
        current = q.get()
        
        for letter in range(len(current)):
            temp = current
            
            for i in range(97,123):
                temp = temp[:letter] + chr(i) + temp[letter + 1:]
                
                if temp in words:
                    if d.get(temp) == None:
                        d[temp] = current
                        
                        if temp == w2:
                            return getPath(w1, w2, d)
                        
                        q.put(temp)
    
    
    return ([], -1)



def runUI(s: set) -> None:
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
            
        dist = distance(word1, word2, s)

        if dist[1] == -1:
            print("no path found with current dict")
        else:
            print("distance: ", dist[0])
            print("path: ", formatPath(dist[1]))
        
        
    print("\ngoodbye.")
    
    
def runSysArg(s: set) -> json:
    dist = distance(sys.argv[1], sys.argv[2], s)
    d = {"distance": dist[0], "path": dist[1]}
    return json.dumps(d)
    

if __name__ == "__main__":
    s = set()
    
    # words_alpha.txt from https://github.com/dwyl/english-words/blob/master/words_alpha.txt
    f = open("./words_alpha.txt", "r")
    for line in f:
        s.add(line.strip())
        
    runUI(s)
#    print(runSysArg(s))

    