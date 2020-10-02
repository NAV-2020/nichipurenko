"""
Реализуйте класс стека для работы со строками (стек строк).
Стек должен иметь фиксированный размер. Реализуйте набор 
операций для работы со стеком:
■ помещение строки в стек;
■ выталкивание строки из стека;
■ подсчет количества строк в стеке;
■ проверку пустой ли стек;
■ проверку полный ли стек;
■ очистку стека;
■ получение значения без выталкивания верхней строки из стека.
При старте приложения нужно отобразить меню с помощью, которого 
пользователь может выбрать необходимую операцию.

Измените стек из второго задания, таким образом, чтобы его размер 
был нефиксированным.
"""

class Stack():

    def __init__(self, items: list=[], size: int=0):
        self.items = items
        self.size = size
    
    def __str__(self):
        """Method returns a stack"""
        if self.size == 0:
            return f'''The stack has unlimited length.
            Stack: {self.items}
            '''
        else:
            return f'''The glass has a length: {len(self.items)}
            Stack: {self.items}
            '''

    def resize_stack(self, size:int):
        """Setting property value."""
        if len(self.items) > size:
            return True
        else: 
            self.size = size

    def stack_length(self)->bool:
        """The method checks the stack length for capacity."""
        if (len(self.items) < self.size) or self.size == 0:
            return True
        elif len(self.items)>= self.size:
            return False

    def add(self, element: str)->bool:
        """Method adds a string to the stack."""
        if self.stack_length():
            self.items.append(element)
            return True
        else:
            return False

    def remove(self)->list:
        """Method pops a string off the stack."""
        return self.items.pop()
    
    def number_lines(self)->int:
        """Method for counting the number of lines in a stack."""
        return len(self.items)

    def empty_list(self):
        """Method checks if the stack is empty."""
        return self.items == []
    
    def full_stack(self):
        """The method checks if the stack is full."""
        if self.size == 0:
            return "Stack size is not fixed."
        elif (self.size != 0) and ((self.size - len(self.items)) == 0):
            return "Stack full."
        else:
            return "Stack is not full"
    
    def read_stack(self)->list:
        """Stack cleanup method."""
        self.items.clear()

    def get_value(self, num: int)->list:
        """Method for getting value from the stack."""
        try:
            return self.items[num-1]
        except IndexError:
            print("Index specified greater than the stack size!!!\n")
            input("Press to continue...\n")

if __name__ == "__main__":

    stack_1 = Stack()

    while True:
        
        print('*'*60)
        print("Make your choice:")
        choice = input("""    
        1. Push a string onto the stack -------------> 1    Вставьте строку в стек
        2. Remove a line from the stack -------------> 2    выталкивание строки из стека
        3. Count the number of lines on the stack ---> 3    подсчет количества строк в стеке;
        4. Check if the stack is empty --------------> 4    проверку пустой ли стек;
        5. Check if the stack is full ---------------> 5    проверку полный ли стек
        6. Read the stack ---------------------------> 6    очистку стека;
        7. Get value from the stack -----------------> 7    получе значен без выталки верхней стр из стека
        8. Resize stack -----------------------------> 8    Изменить размер стека
        9. Exit -------------------------------------> q
        
        Сhoice: """)
        print('*'*60)

        if choice == 'q':
            break
        elif choice == '1':
            string = input("Enter value: ")
            if stack_1.add(string): 
                print(stack_1, "\n")
                input("Press to continue...\n", )
            elif not stack_1.add(string):
                print("STACK FULL!!!")
                input("Press to continue...\n")

        elif choice == '2':
            print("Current stack: ", stack_1)
            stack_1.remove()
            print("New stack: ",stack_1, "\n")
            input("Press to continue...\n")
        
        elif choice == '3':
            print("Number of lines on the stack: ", stack_1.number_lines(), "\n")
            input("Press to continue...\n")
        
        elif choice == '4':
            if stack_1.empty_list():
                print("The stack is empty.\n")
                input("Press to continue...\n")
            else:
                print("The stack is NOT empty!!!\n")
                input("Press to continue...\n")

        elif choice == '5':
            print(stack_1.full_stack())
            input("Press to continue...\n")

        elif choice == '6':
            stack_1.read_stack()
            print("Stack cleared!\n")
            print("New stack: ",stack_1, "\n")
            input("Press to continue...\n")

        elif choice == '7':
            num = int(input("Enter id: "))
            if stack_1.get_value(num) != None:
                print("Line: ", stack_1.get_value(num),"\n")
                input("Press to continue...\n")
        
        elif choice == '8':
            print("""    Enter a number to indicate the size of the stack.
    0 - Stack size is not fixed.
            """)
            size = int(input("Enter the stack size: "))
            if stack_1.resize_stack(size):
                print("""    The current stack size with data is greater 
    than the specified stack size value!
    Clear the stack and resize the stack again!
    """)
                input("Press to continue...\n")
            