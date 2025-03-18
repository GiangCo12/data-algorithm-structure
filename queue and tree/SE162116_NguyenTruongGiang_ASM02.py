class Order:
    def __init__(self, order_id=None, customer_name=None, total_price=None):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_price = total_price

    def __str__(self):
        return f"{self.order_id}, {self.customer_name}, {self.total_price}"

class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class TreeNode:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class OrderQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def loadData(self, file_path, size):
        data = read_file(file_path)
        for i in range(size):
            self.enqueue(data[3*i], data[3*i+1], data[3*i+2])

    def enqueue(self, order_id, customer_name, total_price):
        new_node = Node(Order(order_id, customer_name, total_price))
        if self.rear is None:
            self.front = self.rear = new_node   
        else:
            self.rear.next = new_node
            self.rear = new_node
            
        self.length += 1    
      
    def remove(self, order_id):
        #Xóa một đơn hàng theo order_id
        if self.isEmpty():
            print(f"Queue is empty, cannot remove order {order_id}")
            return
        
        current = self.front
        prev = None
        
        # Duyệt qua danh sách để tìm order_id
        while current and current.info.order_id != order_id:
            prev = current
            current = current.next

        if current is None:  # Không tìm thấy đơn hàng
            print(f"Order ID {order_id} not found in queue.")
            return

        # Nếu cần xóa node đầu tiên
        if prev is None:
            self.front = current.next
        else:
            prev.next = current.next  # Bỏ qua current để xóa nó

        # Nếu node bị xóa là rear, cập nhật rear
        if current == self.rear:
            self.rear = prev

        self.length -= 1  # Giảm số lượng đơn hàng
        print(f"Removed order {order_id} from queue.")

        # ===============================
       
    def display(self):
        print("Order Queue:")
        if self.front is None:
            print("Empty")
        current = self.front
        while current:
            print(current.info.order_id + str(", ") + str(current.info.customer_name) + str(", ") + str(current.info.total_price))
            current = current.next
        print("=========")


class OrderTree:
    def __init__(self):
        self.root = None

    def insert(self, order):
        self.root = self._insert(self.root, order)

    def _insert(self, root, order):
        # ===============================
        if root is None:
            return TreeNode(order)  # Nếu cây rỗng, tạo nút mới

        # So sánh order_id để xác định vị trí chèn
        if order.order_id < root.info.order_id:
            root.left = self._insert(root.left, order)
        elif order.order_id > root.info.order_id:
            root.right = self._insert(root.right, order)
        return root

    def search(self, sreach_id):
        return self._search(self.root, sreach_id)

    def _search(self, root, search_id):
        if root is None:
            return None

        if root.info.order_id == search_id:
            return root.info  # Trả về đơn hàng khớp chính xác
    
        left_result = self._search(root.left, search_id)
        if left_result:
            return left_result  # Nếu tìm thấy ở cây con trái thì trả về ngay

        return self._search(root.right, search_id)
    
    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
    
    def _inOrder_search(self, root, search_id, result):
        """Duyệt cây theo in-order để tìm đơn hàng"""
        if root is None:
            return
        
        # Duyệt cây con trái trước
        self._inOrder_search(root.left, search_id, result)

        # Kiểm tra nếu order_id khớp chính xác hoặc bắt đầu bằng search_id
        if root.info.order_id == search_id or root.info.order_id.lower().startswith(search_id.lower()):
            result.append(root.info)
        
        # Duyệt cây con phải sau
        self._inOrder_search(root.right, search_id, result)    
        
    def remove(self, order_id):
        self.root = self._remove(self.root, order_id)

    def _remove(self, root, order_id):
        # ===============================
        if root is None:
            return root
        #Xác định ví trí Node cần xóa
        if order_id < root.info.order_id:
            root.left = self._remove(root.left, order_id)
        elif order_id > root.info.order_id:
            root.right = self._remove(root.right, order_id)
        else:
            #Trường hợp chỉ có 1
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Trường hợp 2: Node có 2 con, tìm giá trị nhỏ nhất ở cây con phải
            min_larger_node = self._find_min(root.right)
            root.info = min_larger_node.info  # Thay thế bằng giá trị nhỏ nhất
            root.right = self._remove(root.right, min_larger_node.info.order_id)

        return root
    
    def findMax(self):
        max_order = self._findMax(self.root)
        return max_order.info if max_order else None

    def _findMax(self, root):
        if root is None:
            return None  # Nếu cây rỗng, không có giá trị lớn nhất
        while root.right is not None:  # Duyệt về phía phải đến node cuối cùng
            root = root.right
        return root
      
    def display(self):
        print("Order Tree:")
        stack = list()
        current = self.root
        while current is not None or len(stack) != 0:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.info.order_id + str(", ") + str(current.info.customer_name) + str(", ") + str(
                current.info.total_price))
            current = current.right
        print("=========")

    def loadData(self, file_path, size):
        data = read_file(file_path)
        for i in range(size):
            new_order = Order(data[3 * i], data[3 * i + 1], data[3 * i + 2])
            self.insert(new_order)


class ComputerStore:
    def __init__(self):
        self.order_queue = OrderQueue()
        self.order_tree = OrderTree()

    def load(self, file_path, m):
        file_path = "C:\\Users\\Administrator\\Downloads\\ASM02\\ASM02\\Q1\\Given\\data.txt"
        self.order_queue.loadData(file_path, m)
        self.order_tree.loadData(file_path, m)

    def display(self):
        self.order_queue.display()
        self.order_tree.display()

    # This function is used for Question 1
    def f1(self, file_path, m):
        self.load(file_path, m)
        self.display()

    def f2(self, search_id):
        found = self.order_tree.search(search_id)
        return found
    
    def f3(self):
       return self.order_tree.findMax()

    def f4(self, delete_id):
        print("OUTPUT: Before")
        self.display()
        
        self.order_queue.remove(delete_id)
        self.order_tree.remove(delete_id)

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    orders = eval(lines[0].strip())
    return orders
    
# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    ds = ComputerStore()
    m = int(input("Input the size of inventory (from 1 to 10):\nm =   "))
    while (m < 1 or m > 10):
        m = int(input("Please input the size of inventory (from 1 to 10):\nm =   "))

    file_path = input("Please input file name (ex: data.txt):  ")

    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    n = int(input("Input a question (1=>4) : "))
    if n == 1:
        print("OUTPUT:")
        ds.f1(file_path, m)

    if n == 2:
        ds.load(file_path, m)
        search_id = str(input("Search ID: "))
        print("OUTPUT:")
        ds.display()
        found = ds.f2(search_id)
        print("Search Result:")
        if found is not None:
            print(found.order_id + str(", ") + str(found.customer_name) + str(", ") + str(
                found.total_price))
        else:
            print("Not found")

    if n == 3:
        ds.load(file_path, m)
        print("OUTPUT:")
        ds.display()
        max = ds.f3()
        print("Highest Alphabetical ID order: ")
        print(max.order_id + str(", ") + str(max.customer_name) + str(", ") + str(
                max.total_price))

    if n == 4:
        ds.load(file_path, m)
        delete_id = str(input("Delete ID: "))
        print("OUTPUT:")
        print("Before")
        ds.display()
        ds.f4(delete_id)
        print("After")
        ds.display()


# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ================================
