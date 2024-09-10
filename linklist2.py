class Goods:
    def __init__(self, no, code, name, price):
        self.no = no
        self.code = code
        self.name = name
        self.price = price

class Node:
    def __init__(self, goods):
        self.data = goods
        self.next = None


    def __init__(self):
        self.head = None
        self.size = 0

    # add head
    def addFirst(self, no, code, name, price):
        goods = Goods(no, code, name, price)
        node = Node(goods)
        if (self.head is None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def addLast(self, no, code, name, price):
        goods = Goods(no, code, name, price)
        node = Node(goods)

        if (self.head is None):
            self.head = node
        else:
           cur = self.head
           while (cur.next is not None):
               cur = cur.next
           cur.next = node

    #print list of goods
    def printList(self):
        cur = self.head
        while (cur is not None):
            # in cai node ra
            print(cur.data.no, cur.data.code, cur.data.name, cur.data.price)
            cur = cur.next

    def findGoodMaxPrice(self):
        # b1: giả định max = số rất nhỏ
        maxPrice = 0
        nodeMaxPrice = None
        # b2: vòng lặp
        cur = self.head
        while (cur is not None):
            if (maxPrice < cur.data.price):
                maxPrice = cur.data.price
                nodeMaxPrice = cur
            cur = cur.next
        return nodeMaxPrice
    def deleteByCode(self, c):
        if (self.head.data.code == c):
            self.head = self.head.next
        cur = self.head
        while (cur.next is not None):
            if (cur.next.data.code == c):
                cur.next = cur.next.next
            cur = cur.next

    def updatePrice(self, c, newPrice):
        cur = self.head
        while (cur is not None):
            if (cur.data.code == c):
                cur.data.price = newPrice
            cur = cur.next

    HaoDD


def menu(l: LinkedList):

    while (True):

        print("Moi vao nhap vao chuc nang muon thuc hien:")
        print("1. Them vao dau danh sach")
        print("2. Them vao cuoi danh sach")
        print("3. In ra ma sach co gia lon nhat")
        print("4. Xoa ma sach khoi danh sach")
        print("5. Dung")

        choice = int(input("Input your choice: "))

        if (choice == 1):
            # them vao danh sach
            no = input("Input no = ")
            code = input("Input code = ")
            name = input("Input name = ")
            price = int(input("Input price = "))
            l.addFirst(no, code, name, price)
            print("Danh sach sau khi them")
            l.printList()
        elif (choice == 2):
            no = input("Input no = ")
            code = input("Input code = ")
            name = input("Input name = ")
            price = int(input("Input price = "))
            l.addLast(no, code, name, price)
            print("Danh sach sau khi them")
            l.printList()
        elif (choice == 3):
            goodsMaxPrice = l.findGoodMaxPrice()
            print("Ma sach co gia lon nhat la", goodsMaxPrice.data.code)
        elif (choice == 4):
            code = input("Input code = ")
            l.deleteByCode(code)
            print("Ket qua danh sach sau khi xoa")
            l.printList()
        else:
            print("Cam on ban da su dung")
            break



l = LinkedList()
menu(l)
