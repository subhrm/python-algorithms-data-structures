class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, value):
        self.left = Node(value)
        return self.left

    def add_right(self, value):
        self.right = Node(value)
        return self.right

    def __str__(self):
        value = str(self.value)
        left,right = "",""
        if self.left:
            left = str(self.left)
        if self.right:
            right = str(self.right)
        return f"{left} <- {value} -> {right}"


if __name__ == "__main__":
    root = Node(1)
    n2 = root.add_left(2)
    n3 = root.add_right(3)

    n2.add_left(20)
    n2.add_right(25)

    n3.add_left(30)
    n3.add_right(39)

    print(root)