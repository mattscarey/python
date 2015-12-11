

class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def less_than(x,y):
    return x < y

class BinarySearchTree:
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.parents = True
        self.less = less

    # takes value, returns node with key value
    def insert(self, k):
        current = self.root
        if(self.root == None):
            self.root = BSTNode(k)
            return self.root
        while (current):
            if self.less(k, current.key):
                if current.left:
                    current = current.left
                else:
                    current.left = BSTNode(k)
                    return current.left
            elif self.less(current.key, k):
                if current.right:
                    current = current.right
                else:

                    current.right = BSTNode(k)
                    return current.right
            else:
                return current


    # takes key, returns node
    # return the node with the smallest key greater than key
    def successor(self, k):
        n = self.search(k)
        if(n == None or n == None):
            return None
        if(n.right != None):
            TempNode = n.right
            while(TempNode):
                if(TempNode.left):
                    TempNode = TempNode.left
                else:
                    return TempNode
        else:
            TempNode = self.root
            winner = 0
            while(TempNode):
                if(self.less(n.key, TempNode.key)):
                    winner = TempNode
                    TempNode = TempNode.left
                elif(self.less(TempNode.key, n.key)):
                    TempNode = TempNode.right

                else:
                    break
            return winner

    # return the node with the largest key smaller than key
    def predecessor(self, k):
        n = self.search(k)
        if(n == None or n == None):
            return None
        if(n.left != None):
            TempNode = n.left
            while(TempNode):
                if(TempNode.right):
                    TempNode = TempNode.right
                else:
                    return TempNode
        else:
            TempNode = self.root
            winner = 0
            while(TempNode):
                if(self.less(TempNode.key, n.key)):
                    winner = TempNode
                    TempNode = TempNode.right
                elif(self.less(n.key, TempNode.key)):
                    TempNode = TempNode.left

                else:
                    break
            return winner

    # takes key returns node
    # can return None
    def search(self, k):
        node = self.root
        while(node):
            if(self.less(k, node.key)):
                node = node.left
            elif(self.less(node.key, k)):
                node = node.right
            else:
                return node
        return None
            
    # takes key, returns node
    def delete(self, k):
        n = self.search(k)
        if(self.root == None or n == None):
            return None
        prev = self.root
        curr = self.root
        parent = self.root
        while(curr):
            if(self.less(k, curr.key)):
                prev = curr
                curr = curr.left
            elif(self.less(curr.key, k)):
                prev = curr
                curr = curr.right
            else:
                parent = prev
                break
            bigTree = False
            newNode = n
            if(n.left == None and n.right == None):
                newNode = None
            elif(n.left and n.right == None):
                newNode = n.left
            elif(n.right and n.left == None):
                newNode = n.right
            else:
                bigTree = True
                newNode = BSTNode(self.successor(n), n.left, n.right)
            if(parent.left):
                if(parent.left.key == n.key):
                    parent.left = newNode
            if(parent.right):
                if(parent.right.key == n.key):
                    parent.right = newNode
            if(bigTree):
                self.delete(self.successor(n))
            return newNode
