class Book:
    def __init__(self, code, title, author, price):
        self._code = code
        self._title = title
        self._author = author
        self._price = price

    def display(self):
        print("Book code: ", self._code)
        print("Book title: ", self._title)
        print("Book author: ", self._author)
        print("Book price: ", self._price)
    
    def get_title(self):
        return self._title

    def set_code(self, newCode):
        self._code = newCode

    def get_code(self):
        return self._code

    def get_author(self, newAuthor):
        self._author = newAuthor

    
    def set_title(self, title):
        self._title = title    
        
    def set_name(self, new_name):
        self._title = new_name     
        
    def srarchBook(self, name):
        result = []
        tmp = self._head
        while tpm:
            if tmp._element._title == name:
                #result.append(tmp._element)
                result.append(tmp._element)
            tmp = tmp._next
        return result            


class BookList:
    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty list of books."""
        self._head = None
        self._tail = None
        self._size = 0  # number of CURRENT elements in the book list

    def __len__(self):
        """Return the number of CURRENT elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty, False otherwise."""
        return self._size == 0

    def get_first(self):
        """Return (but do not remove) the element stored in head.
            Note that:
                1. list's head means stack's top or peak.
                2. list's head means queue's front.
                3. list's tail means queue's read.
            Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('Book list is empty')
        return self._head._element  # head of list means front of queue

    def get_last(self):
        """ Return (but do not remove) the element stored in tail.
            Note that:
                  1. list's head means stack's top or peak.
                  2. list's head means queue's front.
                  3. list's tail means queue's read.
            Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('Book list is empty')

        return self._tail._element  # tail of list means rear of queue

    def get_at(self, index):
        """ Traverse and return the element at the position 'index' the list.
            This method return -1 if e does not exist in the list.
            Raise Empty exception if:
                1. index > list's size, or
                2. index < 0
        """
        # write your code here, then remove the keyword 'pass'
        if(index>=self._size or index<0):
            raise ()
        

    def check_duplicate(self, e):
        # write your code here, then remove the keyword 'pass'
        return False

    def add_first(self, e):
        """ Add the element e into the head of the list.
            This method is identical to stack's push
        """
        newNode = self._Node(e, self._head)  # create a newNode
        self._head = newNode  # links newNode to head

        if self._tail is None:  # special case: the list is empty
            self._tail = newNode  # update reference to tail node

        self._size += 1

    def add_last(self, e):
        """ Add the element e into the head of the list.
            This method is identical to queue's enqueue.
        """
        newNode = self._Node(e, None)  # newNode will be the new tail node
        if self.is_empty():
            self._head = newNode  # special case: previously empty
        else:
            self._tail._next = newNode

        self._tail = newNode  # update reference to tail node
        self._size += 1

    def remove_first(self):
        """ Remove and return the first element of the list.
            This method is identical to:
                1. stack's pop
                2. dequeue from a queue
            Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('Book list is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():  # special case as the list is empty
            self._tail = None  # removed head had been the tail

        return answer

    def remove_last(self):
        """ Remove and return the last element of the list.
            Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('Book list is empty')

        answer = None
        if self._head._next is None:  # List has only ONE node
            answer = self._head._element
            self._head = None
            self._tail = None
            self._size -= 1
            return answer

        # If the program reaches here,
        # Then there were at least TWO nodes in the list
        second_last = self._head
        while second_last._next._next:
            second_last = second_last._next

        answer = self._tail._element
        second_last._next = None  # None means self._tail._next
        self._tail = second_last
        self._size -= 1
        return answer

    def print_book(self):
        """This function prints contents of book list.
        It starts from head.
        """
        count = 0
        temp = self._head
        while temp:
            print("\nBook ", count, "'s info:")
            temp._element.display()
            temp = temp._next
            count += 1
            
                
                


menu_options = {
        1: 'Add a new book',
        2: 'Update book info',
        3: 'Search book info',
        4: 'Remove a book',
        5: 'Displays n books',
        6: 'Exit',
}

def print_menu():
      """
      displays the menu options on screen
      :return: void
      """
      print("===============MENU===============")
      for key in menu_options.keys():
          print("===", key, '. ', menu_options[key])
      print("==================================")

def add_book(book_list):
      print('Code for handling \'Add a new book\'')
      # Write your code here
      code = input('Input code: ')
      name = input('Input name: ')
      author = input('Input author: ')
      price = int(input('Input price: '))
      newBook = Book(code, name, author, price)

      # Check duplicate before insertion
      if not book_list.check_duplicate(code):
          book_list.add_first(newBook)
          print("Book added successfully")
      else:
          print("Cannot insert! Book is duplicated")

def update_book(book_list):
      print('Code for handling \'Update book info\'')
      # Write your code here
      a_book = bool._list.get._first()
      new_author = input("Enter new author name")
      a_book.set._author(new_author)

def search_book(book_list):
      print('Code for handling \'Search book info\'')
      # Write your code here
      name = input('Enter book')
      print('Code for handling \'Sreach book info\'')
      name = input('Enter book\'s name ')
      r = book_list.sreachBook(name)
      if len(r) == 0:
          print('No book')
      else:
          for item in r:
              item.display()    

def remove_book(book_list):
      print('Code for handling \'Remove a book\'')
      # Write your code here

def display_book(book_list):
      # Write your code here
      book_list.print_book()

def exit_menu():
      print('Thank you, Good Bye, Babies!')
      exit()


def start_menu(b_management):
    while True:
        print_menu()
        user_choice = input('Enter your choice: ')

        # Check what choice was entered and act appropriately
        if user_choice == '1':
            add_book()
        elif user_choice == '2':
            update_book()
        elif user_choice == '3':
            search_book()
        elif user_choice == '4':
            remove_book()
        elif user_choice == '5':
            display_book()
        elif user_choice == '6':
            exit_menu()
        else:
            print('Invalid option. Please enter a number [1--5].')


if __name__ == '__main__':
    book_list = BookList()
    while True:
        print_menu()
        user_choice = input('Enter your choice: ')

        # Check what choice was entered and act appropriately
        if user_choice == '1':
            add_book(book_list)
        elif user_choice == '2':
            update_book(book_list)
        elif user_choice == '3':
            search_book(book_list)
        elif user_choice == '4':
            remove_book(book_list)
        elif user_choice == '5':
            display_book(book_list)
        elif user_choice == '6':
            exit_menu()
        else:
            print('Invalid option. Please enter a number [1--5].')


