

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

    def height(self, n):
        return_val = 0
        if(n != None):
            return_val = 1 + max(self.height(n.left), self.height(n.right))
        return return_val

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


    # takes node, returns node
    # return the node with the smallest key greater than n.key
    def successor(self, n):
        if(n == None):
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

    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
        if(n == None):
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
            
    # takes node, returns None if node not found.
    def delete(self, k):
        parent = None
        currNode = self.root
        toDelete = None
        while currNode: #finds node
            if(self.less(k, currNode.key)):
                parent = currNode
                currNode = currNode.left
            elif(self.less(currNode.key, k)):
                parent = currNode
                currNode = currNode.right
            else:

                toDelete = currNode
                break

        if toDelete == None:
            return None

        if toDelete.left == None and toDelete.right == None: #has no children
            if parent.left == toDelete:
                parent.left = None
            if parent.right == toDelete:
                parent.right = None

        elif toDelete.left and toDelete.right == None: #has left child
            if parent.left == toDelete:
                parent.left = toDelete.left
            if parent.right == toDelete:
                parent.right = toDelete.left

        elif toDelete.right and toDelete.left == None: #has right child
            if parent.left == toDelete:
                parent.left = toDelete.right
            if parent.right == toDelete:
                parent.right = toDelete.right

        else: #two children
            succ = self.successor(toDelete).key
            self.delete(succ)
            if parent == None:
                self.root = BSTNode(succ, toDelete.left, toDelete.right)
            elif parent.left == toDelete:
                parent.left = BSTNode(succ, toDelete.left, toDelete.right)
            elif parent.right == toDelete:
                parent.right = BSTNode(succ, toDelete.left, toDelete.right)





