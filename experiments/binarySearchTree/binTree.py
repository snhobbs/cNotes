'''
Check to see if a binary tree is indeed what is claims to be
'''

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST(root):
    try:
        checkNode(root)
        return True
    except UserWarning:
        return False
        
def checkNode(node):
    '''
    check that all nodes to the left are smaller than it and all to the right are greater
    '''
    if node.left is None and node.right is None:
        return [node.data]

    dataRight = checkNode(node.right)
    dataLeft = checkNode(node.left)
        
    for dataR in dataRight:
        if dataR <= node.data:
            raise UserWarning("Not a binary tree")
    for dataL in dataLeft:
        if dataL >= node.data:
            raise UserWarning("Not a binary tree")
    return dataRight + dataLeft

def treeA():
    root = node(4)
    root.left = node(2)
    root.left.left = node(1)
    root.left.right = node(3)
    root.right = node(6)
    root.right.left = node(5)
    root.right.right = node(12)
    return root
    
def treeB():
    root = node(8)
    root.left = node(4)
    root.left.left = node(2)
    root.left.left.left = node(1)
    root.left.left.right = node(3)
    root.left.right = node(6)
    root.left.right.left = node(5)
    root.left.right.right = node(7)
    
    root.right = node(13)
    root.right.left = node(10)
    root.right.left.left = node(9)
    root.right.left.right = node(11)
    root.right.right = node(14)
    root.right.right.left = node(12)
    root.right.right.right = node(15)
    
    return root
           
if __name__=="__main__":
    print(checkBST(treeA()))
    print(checkBST(treeB()))

