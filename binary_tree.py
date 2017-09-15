class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Binary_Tree(object):
    def __init__(self,root_node):
        self.root = root_node

    def add_node(self,node):
        self.temp = self.root
        while self.temp != None:
            if self.temp.val < node.val:
                if self.temp.right == None:
                    self.temp.right = node
                    return
                else:
                    self.temp = self.temp.right
            else :
                if self.temp.left == None:
                    self.temp.left = node
                    return
                else:
                    self.temp = self.temp.left

    def print_tree(self,head):
        temp = head
        print temp.val
        if temp.left != None:
            print "Left"
            self.print_tree(temp.left)
        if temp.right != None:
            print "Right"
            self.print_tree(temp.right)
        return
first_node = TreeNode(2)
second_node = TreeNode(1)
third_node = TreeNode(3)
fourth_node = TreeNode(4)

my_binary_tree = Binary_Tree(first_node)
my_binary_tree.add_node(second_node)
my_binary_tree.add_node(third_node)
my_binary_tree.add_node(fourth_node)
my_binary_tree.print_tree(first_node)
