import threading
import time
from threading import Thread


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables, client_maximum):
        self.queue = []
        self.tables = tables
        self.customers_count = 0
        self.client_maximum = client_maximum

    def customer_arrival(self):
        while True:
            if self.customers_count < self.client_maximum:
                self.customers_count += 1
                new_customer = Customer(self.customers_count)
                print("Посетитель номер", new_customer.name, "прибыл.")
                self.queue.append(new_customer)

            if len(self.queue) == 0:
                break

            self.serve_customer(self.queue[0])
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print("Посетитель номер", customer.name, "сел за стол", table.number)
                self.queue.remove(customer)
                # Запускаем поток обслуживания посетителя
                t = Thread(target=customer.serve, args=(table,))
                t.start()
                break
        else:
            print("Посетитель номер", customer.name, "ожидает свободный стол.")
            return


class Customer:
    def __init__(self, name):
        self.name = name

    def serve(self, table):
        time.sleep(5)
        table.is_busy = False
        print("Посетитель номер", self.name, "покушал и ушёл.")


tables = [Table(i) for i in range(3)]
cafe = Cafe(tables, 5)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
