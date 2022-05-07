import collections 

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def swap(root):
    if root is None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp


def invertBinaryTree(root):
    if root is None:
        return
    
    q = collections.deque()
    q.append(root)

    while q:
        curr = q.popleft()
        swap(curr)

        if curr.left:
            q.append(curr.left)

        if curr.right:
            q.append(curr.right)

if __name__ == '__main__':
     
    ''' Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    invertBinaryTree(root)
    preorder(root)
 