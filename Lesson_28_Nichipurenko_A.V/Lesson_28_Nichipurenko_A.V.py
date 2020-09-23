"""
# Stack: pop(), push()
# Queue: push(), pop(), top()


Queue = []
QueueStart = 0


def push(val):
    Queue.append(val)

def pop():
    global QueueStart
    if QueueStart > len(Queue)/2:
        Queue[:QueueStart] = []
        QueueStart = 0

    if QueueStart < len(Queue):
        QueueStart += 1
        return Queue[QueueStart - 1]

def top():
    if QueueStart < len(Queue):
        return Queue[QueueStart]

def size():
    return len(Queue) - QueueStart

def is_empty():
    return (len(Queue) - QueueStart)== 0

def clear():
    Queue[:] = []   

if __name__ == "__main__":
    push(1)
    push(2)
    push(3)
    print(f"Size: {size()}")
    print(pop())
    print(f"Size: {size()}")
    print(pop())
    print(pop())
    print(pop())
    
#######################
H = []
H[1] == 100
H[2] == 20
H[3] == 30
H[4] == 17
H[5] == 3
H[6] == 25
H[7] == 1
H[8] == 2
H[9] == 7

"""
stack = []

def approve_number(num)->bool:
    if num not in stack:
        return True

def approve(question)->bool:
    if question == add:
        app = input('Do you want to add it? y/n')
    app = int('Do you want to change all numbers? y/n')

def add(num):
    if approve_number(num):
        stack.append(num)
        
def show_steck():
    print(f'Stack: {stack}')

def edit_number(num_1, nun_2):
    pass
      

if __name__ == "__main__":
    while True:
        print('What to do?')

        choice = int(input('Enter the choice: '))
        if choice == 'q':
            break
        elif choice = '1':
            add(num)
        elif choice == '0':
            show_steck()
        elif  choice == '2':
            num_1 = int(input('Enter num_1: '))
            num_2 = int(input('Enter num_2: '))
            edit_number(num_1, num_2)