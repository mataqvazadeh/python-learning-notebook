class Task:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'[ ] {self.text}'
    
class ToDoList:
    def __init__(self):
        self.tasks : list = []

    def add(self, task):
        self.tasks.append(task)

    def __str__(self) -> str:
        return '\n'.join([str(task) for task in self.tasks])
    
    def __len__(self) -> int:
        return len(self.tasks)
    
    def __iadd__(self, other: Task) -> 'ToDoList':
        self.add(other)
        return self
    
    def __gt__(self, other: 'ToDoList') -> bool:
        return len(self.tasks) > len(other.tasks)
    

def main():
    task1 = Task('Washing dishes')
    print(task1)
    print('-' * 10)
    task2 = Task('Doing my hws')
    print(task2)

    todolist = ToDoList()
    print('-' * 10)
    print(len(todolist))
    print(todolist)

    todolist.add(task1)
    print('-' * 10)
    print(len(todolist))
    print(todolist)

    todolist.add(task2)
    print('-' * 10)
    print(len(todolist))
    print(todolist)

    todolist.add(Task('Solve Problem'))
    print('-' * 10)
    print(len(todolist))
    print(todolist)

    todolist2 = ToDoList()
    todolist2 += Task('Read a good book')
    print('-' * 10)
    print(len(todolist2))
    print(todolist2)

    print('-' * 10)
    print(f'todolist > todolist2? {todolist > todolist2}')

if __name__ == '__main__':
    main()