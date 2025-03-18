class Item:
    def __init__(self, name, amount=0, price=0):
        self.name = name
        self.amount = amount
        self.price = price

    def __repr__(self):
        return f"{self.name}, {self.amount}, {self.price}"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class dataList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addLast(self, name, amount, price):
        new_node = Node(Item(name, amount, price))
        if self.head is None:
            self.head = new_node  
            self.tail = new_node  
        else:
            self.tail.next = new_node 
            self.tail = new_node       

    def display(self):
        print("Data list:")
        if (self.head is None):
            print("Empty")
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("=========")

    def loadData(self, file_path, size):
        data = read_file(file_path)[0]
        for i in range(size):
            self.addLast(data[3*i], data[3*i+1], data[3*i+2])

class requestQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self, name, amount):
        new_node = Node(Item(name, amount))
        # ===============================
        new_node = Node(Item(name, amount))
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        # end your code
    def deQueue(self):
        if self.front is None:
            return None
        tmp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return tmp.data
        # ===============================

    def display(self):
        print("Request Queue:")
        if (self.front is None):
            print("Empty")
        current = self.front
        while current:
            print(current.data.name + str(", ") + str(current.data.amount))
            current = current.next
        print("=========")

    def loadRequest(self, file_path, size):
        data = read_file(file_path)[1]
        for i in range(size):
            self.enQueue(data[2*i], data[2*i+1])

class computerStore:
    def __init__(self):
        self.data = dataList()
        self.request = requestQueue()

    def load(self, file_path, m, n):
        file_path = "C:\\Users\\Administrator\\Downloads\\ASM01\\ASM01\\Q1\\Given\\data.txt"
        self.data.loadData(file_path, m)
        self.request.loadRequest(file_path, n)

    def display(self):
        self.data.display()
        self.request.display()

    # This function is used for Question 1
        
    def f1(self, file_path,m, n):
        # Đọc dữ liệu trực tiếp từ file đã chỉ định
        self.load(file_path, m, n)  # Load dữ liệu từ file
    # Hiển thị dữ liệu theo yêu cầu
        self.data.display()
        self.request.display()
  
    def purchase(self, t1):
        current = self.data.head
        while current:
            if current.data.name == t1.name:
                if current.data.amount >= t1.amount:
                    current.data.amount -= t1.amount  #  Giảm số lượng sản phẩm
                    return True  #  Trả về True nếu mua thành công
                return False  #  Trả về False nếu không đủ hàng
            current = current.next
        return False  

    def f2(self):
        t1 = self.request.deQueue()
        if t1:
            success = self.purchase(t1)
            if not success:
                print(f"Không thể mua {t1.amount} {t1.name} (không đủ hàng hoặc không có trong kho)")


    def f3(self):
        while self.request.front:
            t1 = self.request.deQueue()
            if t1:
                self.purchase(t1)
        
    def f4(self):
        money = 0
        
        while self.request.front:
            t1 = self.request.deQueue()
            if t1:
                current = self.data.head
                while current:
                    if current.data.name == t1.name:
                        if current.data.amount >= t1.amount:
                            revenue = t1.amount * current.data.price
                            money += revenue
                            current.data.amount -= t1.amount
                        break
                    current = current.next    
                            
        return money

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    item_data = eval(lines[0].strip())
    request_data = eval(lines[1].strip())
    return item_data, request_data


# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    ds = computerStore()
    m = int(input("Input the size of inventory (from 1 to 10):\nm =   "))
    while (m < 1 or m > 10):
        m = int(input("Please input the size of inventory (from 1 to 10):\nm =   "))
    n1 = int(input("Input the size of requests (from 1 to 10):\nn =   "))
    while (n1 < 1 or n1 > 10):
        n1 = int(input("Please input the size of requests (from 1 to 10):\nn =   "))

    file_path = input("Please input file name (ex: data.txt):  ")

    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    n = int(input("Input a question (1=>4) : "))
    if n == 1:
        print("OUTPUT:")
        ds.f1(file_path, m, n1)

    if n == 2:
        ds.load(file_path, m, n1)
        print("OUTPUT:")
        print("Before")
        ds.display()
        ds.f2()
        print("After")
        ds.display()

    if n == 3:
        ds.load(file_path, m, n1)
        print("OUTPUT:")
        print("Before")
        ds.display()
        ds.f3()
        print("After")
        ds.display()

    if n == 4:
        ds.load(file_path, m, n1)
        print("OUTPUT:")
        print("Before")
        ds.display()
        money = ds.f4()
        print("After")
        ds.display()
        print("Money= " + str(money))



# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ================================