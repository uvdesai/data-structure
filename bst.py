class BSt:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BSt(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BSt(data)
    def in_order(self):
        num=[]
        if self.left:
            num+=self.left.in_order()
        num.append(self.data)
        if self.right:
            num+=self.right.in_order()
        return num
def built_tree(num):
    root=BSt(num[0])
    for i in range(1,len(num)):
        root.add_child(num[i])
    return root

if __name__ == '__main__':
    numbers=[17, 4, 1, 20, 9, 23, 18, 34]
    num_tree=built_tree(numbers)

    print(num_tree.in_order())
        


