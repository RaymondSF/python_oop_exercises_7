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


class OrderBookApplication:
    def __init__(self):
        self.orders = OrderBook()

    def run(self):
        while True:
            print("commands:")
            print("0 exit")
            print("1 add order")
            print("2 list finished tasks")
            print("3 list unfinished tasks")
            print("4 mark task as finished")
            print("5 programmers")
            print("6 status of programmer")

            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_task_finished()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.programmer_status()
            else:
                print("erroneous input")

    def add_order(self):
        try:
            description = input("description: ")
            programmer_workload = input("programmer and workload estimate: ").split()
            programmer = programmer_workload[0]
            workload = int(programmer_workload[1])
            self.orders.add_order(description, programmer, workload)
            print("added!")
        except (ValueError, IndexError):
            print("erroneous input")

    def list_finished_tasks(self):
        finished_orders = self.orders.finished_orders()
        if not finished_orders:
            print("no finished tasks")
        else:
            for order in finished_orders:
                print(order)

    def list_unfinished_tasks(self):
        unfinished_orders = self.orders.unfinished_orders()
        if not unfinished_orders:
            print("no unfinished tasks")
        else:
            for order in unfinished_orders:
                print(order)

    def mark_task_finished(self):
        try:
            id = int(input("id: "))
            self.orders.mark_finished(id)
            print("marked as finished")
        except (ValueError, IndexError):
            print("erroneous input")

    def list_programmers(self):
        programmers = self.orders.programmers()
        for programmer in programmers:
            print(programmer)

    def programmer_status(self):
        try:
            programmer = input("programmer: ")
            status = self.orders.status_of_programmer(programmer)
            print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
        except ValueError:
            print("erroneous input")


if __name__ == "__main__":
    app = OrderBookApplication()
    app.run()