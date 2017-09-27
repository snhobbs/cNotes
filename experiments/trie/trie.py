# trie
class Node(object):
    '''
    Make a new node for an entry that doesnt already exist
    Put all of the letters after the first node in a single node
    when the node above it increases in count break off the top letter and
    create a new node below it. Add the new node in above it.
    If the new node matches one of the next nodes letters then this will just recurse
    '''
    def __init__(self):
        self.entry = False
        self.nodes = {}
        self.subEntries = 0
        
    def addNode(self, key):
        if key in self.nodes.keys():
            self.nodes[key].subEntries += 1
            return self.nodes[key]
        else:
            self.nodes.update({key: Node()})
            self.nodes[key].subEntries += 1
            return self.nodes[key]
            
def addEntry(root, entry):
    node = root
    for char in entry:
        node = node.addNode(char)
    node.entry = True

def findEntry(root, entry):
    node = root
    try:
        for char in entry:
            node = node.nodes[char]
        return node.subEntries
    except KeyError:
        return 0
    
if __name__ == "__main__":
    root = Node()
    out = []
    import time
    with open('trieData.txt', 'r') as f:
        start = time.time()
        for line in f:
            op, entry = line.strip().split(' ')
            if op == 'add':
                addEntry(root, entry)
            elif op == 'find':
                out.append(findEntry(root, entry))
    print(out)
    print(time.time()- start)