from stack import Stack
from my_queue import Queue

def main():
    # my_stack = Stack()
    # my_stack.push(1)
    # my_stack.push(10)
    # my_stack.push("ali")

    # print(my_stack.top)

    # while not my_stack.is_empty():
    #     print(len(my_stack))
    #     print(my_stack.pop())

    my_q = Queue()
    my_q.enqueue(500)
    my_q.enqueue(10)
    my_q.enqueue("ali")

    print(my_q.head)

    while not my_q.is_empty():
        print(len(my_q))
        print(my_q.dequeue())


if __name__ == '__main__':
    main()