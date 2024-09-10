class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):   #Thêm một nút con vào danh sách nút con của nút hiện tại
        self.children.append(child)

    def remove_child(self, child):  #Xóa một nút con khỏi danh sách nút con của nút hiện tại.
        self.children.remove(child)

    def get_children(self):   #trả về danh sách con nút cuủa childern
        return self.children

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def is_leaf(self):
        return len(self.children) == 0

    def traverse(self):
        print(self.data)
        for child in self.children:
            child.traverse()


# Tạo cây
root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")

# Thiết lập liên kết giữa các nút
root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)

# Truy cập và sử dụng các phương thức của cây
print("Data của nút gốc:", root.get_data())

children = root.get_children()
print("Số lượng con của nút gốc:", len(children))

print("Các nút con của nút gốc:")
for child in children:
    print(child.get_data())

print("Cây:")
root.traverse()

