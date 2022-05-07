class Node:
    def __init__(self, val=0):
        self.data=val
        self.left=None
        self.right=None

class Inversion:
    def swap(self, root: Node):
        if root == None:
            return

        temp = root.left
        root.left = root.right
        root.right = temp

    def PrintTree ( self ) :
       if self.left :
           self.left.PrintTree ()
       print ( self.data, end= ' ' ) ,
       if self.right :
           self.right.PrintTree ()

    def invert(self, root: Node):
        if root == None:
            return
        stack = []
        stack.append(root)
        print('stack ', stack)
        while (stack):
            print('aesese: ', stack)
            current = stack.pop()
            self.swap(current)
            if(current.right):
                stack.append(current.right)
            if(current.left):
                stack.append(current.left)

    

if __name__ == '__main__':
    '''
                10                                              10
              /    \                                          /    \           
            20      30              ========>>              30      20           
           /         \                                      /        \
          40          50                                  50          40 
          '''
    Tree = Node(10)
    Tree.left = Node(20)
    Tree.right = Node(30)
    Tree.left.left = Node(40)
    Tree.right.right = Node(50)

    print('muh tree: ', Tree.left.left.data)

    # print('Initial Tree :', end='')
    # Tree.PrintTree()
    Inversion().invert(Tree)
    # print('\nInverted Tree:', end='')
    # Tree.PrintTree()

