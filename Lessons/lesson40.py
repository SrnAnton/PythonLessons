import queue
import random
import threading
import time
from threading import Thread


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.customers_count = 0

    def customer_arrival(self):
        while True:
            self.customers_count += 1
            new_customer = Customer(self.customers_count)
            print("Посетитель номер", new_customer.name, "прибыл.")
            self.queue.put(new_customer)
            self.serve_customer(self.queue.get())
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print("Посетитель номер", customer.name, "сел за стол", table.number)
                break
        else:
            print("Посетитель номер", customer.name, "ожидает свободный стол.")
            return

        # Запускаем поток обслуживания посетителя
        t = Thread(target=customer.serve, args=(table,))
        t.start()


class Customer:
    def __init__(self, name):
        self.name = name

    def serve(self, table):
        time.sleep(5)
        table.is_busy = False
        print("Посетитель номер", self.name, "покушал и ушёл.")


tables = [Table(i) for i in range(3)]
cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
