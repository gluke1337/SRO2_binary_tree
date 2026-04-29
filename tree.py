import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print("   " * level + str(node.value))
            self.print_tree(node.left, level + 1)

    def draw_tree(self):
        plt.figure(figsize=(10, 6))
        plt.title("Визуализация бинарного дерева")

        if self.root is not None:
            self._draw_node(self.root, 0, 0, 4)

        plt.axis("off")
        plt.savefig("binary_tree.png", dpi=300, bbox_inches="tight")
        plt.show()

    def _draw_node(self, node, x, y, dx):
        plt.text(
            x, y, str(node.value),
            ha="center",
            va="center",
            bbox=dict(boxstyle="circle", edgecolor="black")
        )

        if node.left:
            plt.plot([x, x - dx], [y, y - 1])
            self._draw_node(node.left, x - dx, y - 1, dx / 2)

        if node.right:
            plt.plot([x, x + dx], [y, y - 1])
            self._draw_node(node.right, x + dx, y - 1, dx / 2)


tree = BinaryTree()

values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

for v in values:
    tree.add(v)

print("Структура дерева:")
tree.print_tree(tree.root)

tree.draw_tree()
