class Task:
    task_id = 1

    def __init__(self, description, programmer, workload):
        self.id = Task.task_id
        Task.task_id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self._finished = False

    def mark_finished(self):
        self._finished = True

    def is_finished(self):
        return self._finished

    def __str__(self):
        status = "FINISHED" if self._finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self._orders = []

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self._orders.append(task)

    def all_orders(self):
        return self._orders

    def programmers(self):
        programmers_set = set(task.programmer for task in self._orders)
        return list(programmers_set)
    
    def mark_finished(self, id: int):
        found = False
        for task in self._orders:
            if task.id == id:
                task.mark_finished()
                found = True
                break
        if not found:
            raise ValueError("No task with the given id")
        
    def finished_orders(self):
        return [task for task in self._orders if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self._orders if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        finished_count = 0
        unfinished_count = 0
        finished_hours = 0
        unfinished_hours = 0

        for task in self._orders:
            if task.programmer == programmer:
                if task.is_finished():
                    finished_count += 1
                    finished_hours += task.workload
                else:
                    unfinished_count += 1
                    unfinished_hours += task.workload

        return finished_count, unfinished_count, finished_hours, unfinished_hours

orders = OrderBook()

"""
# Part 1
t1 = Task("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())

t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)
"""

# Part 2
orders.add_order("program webstore", "Adele", 10) #id 1
orders.add_order("program mobile app for workload accounting", "Eric", 25) #id 2
orders.add_order("program app for practising mathematics", "Adele", 100) #id 3

for order in orders.all_orders():
    print(order)

for programmer in orders.programmers():
    print(programmer)

my_list = [1, 1, 3, 6, 4, 1, 3]
my_list2 = list(set(my_list))
print(my_list)
print(my_list2)

# Part 3
for order in orders.all_orders():
    print(order)

orders.mark_finished(1)
orders.mark_finished(2)

for order in orders.all_orders():
    print(order)

# Part 4
orders.add_order("program the next facebook", "Eric", 1000) #id 4

for order in orders.all_orders():
    print(order)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)

for order in orders.all_orders():
    print(order)