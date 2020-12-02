# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from abc import ABC, abstractmethod


class ItemNotFound(Exception):

    def __init__(self, text):
        self.text = text


class Stock:

    stock_dict = {"p001": 20, "p002": 10, "p003": 35, "s001": 15, "s003": 40, "s004": 5, "c002": 1}
    division_1 = {"p001": 3, "p002": 1, "p003": 10, "s001": 5, "s003": 10, "s004": 5, "c001": 1}
    division_2 = {"p003": 20, "s003": 15}
    division_3 = {}

    @classmethod
    def accept(cls, obj, quantity):
        if not cls.stock_dict.get(obj):
            cls.stock_dict[obj] = quantity
        else:
            cls.stock_dict[obj] += quantity

    @classmethod
    def show(cls):
        print(cls.stock_dict)

    @classmethod
    def ship(cls, division, obj, quantity):
        if not cls.stock_dict.get(obj) or cls.stock_dict[obj] < quantity:
            print("Invalid quantity. Please make sure that there is enough stock for the shipment.")
        else:
            cls.stock_dict[obj] -= quantity
        if division == '1':
            if not cls.division_1.get(obj):
                cls.division_1[obj] = quantity
            else:
                cls.division_1[obj] += quantity
        elif division == '2':
            if not cls.division_2.get(obj):
                cls.division_2[obj] = quantity
            else:
                cls.division_2[obj] += quantity
        elif division == '3':
            if not cls.division_3.get(obj):
                cls.division_3[obj] = quantity
            else:
                cls.division_3[obj] += quantity
        else:
            print("Invalid division. Please check the division number.")


class Goods(ABC):

    def __init__(self, art, brand, model, price):
        self.art = art
        self.brand = brand
        self.model = model
        self.price = price

    @abstractmethod
    def output(self):
        print({"art.": self.art, "brand": self.brand, "model": self.model, "price": self.price})


class Printer(Goods):

    p_features = ["art", "brand", "model", "price", "p_type", "p_rate", "p_max_format", "is_color"]
    p_info = {}

    def __init__(self, art, brand, model, price, p_type, p_rate, p_max_format, is_color=False):
        super().__init__(art, brand, model, price)
        self.p_type = p_type
        self.p_rate = p_rate
        self.p_max_format = p_max_format
        self.is_color = is_color
        Printer.p_info.update({art: self})

    def output(self):
        print({"Art. no": self.art, "brand": self.brand, "model": self.model, "price": self.price, "type": self.p_type,
               "rate": self.p_rate, "max_format": self.p_max_format, "is_color": self.is_color})

    @classmethod
    def initial(cls, data):
        art, brand, model, price, p_type, p_rate, p_max_format, is_color = data
        return cls(art, brand, model, price, p_type, p_rate, p_max_format, is_color)

    @staticmethod
    def info(art):
        try:
            Printer.p_info.get(art)
            if not Printer.p_info.get(art):
                raise ItemNotFound("There is no such item in the database.")
        except ItemNotFound as err:
            print(err)
        else:
            return Printer.p_info.get(art).output()


class Scanner(Goods):

    s_features = ["art", "brand", "model", "price", "s_type", "s_dpi", "s_max_format", "interface"]
    s_info = {}

    def __init__(self, art, brand, model, price, s_type, s_dpi, s_max_format, interface):
        super().__init__(art, brand, model, price)
        self.s_type = s_type
        self.s_dpi = s_dpi
        self.s_max_format = s_max_format
        self.interface = interface
        Scanner.s_info.update({art: self})

    def output(self):
        print({"Art. no": self.art, "brand": self.brand, "model": self.model, "price": self.price, "type": self.s_type,
               "dpi": self.s_dpi, "max_format": self.s_max_format, "interface": self.interface})

    @classmethod
    def initial(cls, data):
        art, brand, model, price, s_type, s_dpi, s_max_format, interface = data
        return cls(art, brand, model, price, s_type, s_dpi, s_max_format, interface)

    @staticmethod
    def info(art):
        try:
            Scanner.s_info.get(art)
            if not Scanner.s_info.get(art):
                raise ItemNotFound("There is no such item in the database.")
        except ItemNotFound as err:
            print(err)
        else:
            return Scanner.s_info.get(art).output()


class Copier(Goods):

    c_features = ["art", "brand", "model", "price", "c_rate", "c_dpi", "c_max_format", "is_color"]
    c_info = {}

    def __init__(self, art, brand, model, price, c_rate, c_dpi, c_max_format, is_color=False):
        super().__init__(art, brand, model, price)
        self.c_rate = c_rate
        self.c_dpi = c_dpi
        self.c_max_format = c_max_format
        self.is_color = is_color
        Copier.c_info.update({art: self})

    def output(self):
        print({"Art. no": self.art, "brand": self.brand, "model": self.model, "price": self.price, "rate": self.c_rate,
               "dpi": self.c_dpi, "max_format": self.c_max_format, "is_color": self.is_color})

    @classmethod
    def initial(cls, data):
        art, brand, model, price, c_rate, c_dpi, c_max_format, is_color = data
        return cls(art, brand, model, price, c_rate, c_dpi, c_max_format, is_color)

    @staticmethod
    def info(art):
        try:
            Copier.c_info.get(art)
            if not Copier.c_info.get(art):
                raise ItemNotFound("There is no such item in the database.")
        except ItemNotFound as err:
            print(err)
        else:
            return Copier.c_info.get(art).output()


p_1 = Printer("p001", "Xerox", "Phaser 3020BI", "7990", "laser", "20", "A4")
p_2 = Printer("p002", "HP", "Laser 107w", "7315", "laser", "20", "A4")
p_3 = Printer("p003", "Pantum", "P2207", "5299", "laser", "20", "A4")
p_4 = Printer("p004", "Canon", "PIXMA TS704", "6050", "jet", "15", "A4", True)

s_1 = Scanner("s001", "Canon", "CanoScan LiDE 400", "6390", "flatbed", "4800x4800", "A4", "USB")
s_2 = Scanner("s002", "Epson", "Perfection V19", "5700", "flatbed", "4800x4800", "A4", "USB 2.0")
s_3 = Scanner("s003", "Espada", "iScan A4", "4248", "hand", "900", "A4", "USB 2.0")
s_4 = Scanner("s004", "Ion", "Docs 2 Go", "1200", "broaching", "300x300", "A4", "USB 2.0")

c_1 = Copier("c001", "Duplo", "DP-A100 II", "236674", "75", "300x360", "A4", True)
c_2 = Copier("c002", "Ricoh", "Priport DX 2430", "157748", "90", "300x300", "B4", True)
c_3 = Copier("c003", "Riso", "CV 1200", "180000", "60", "300x300", "A4")
c_4 = Copier("c004", "Ricoh", "PRIPORT DD 5450", "524657", "150", "300x600", "A3", True)


menu = "******* Goods database *******\n1. Add item\n2. Show stock\n3. Goods info\n\nEnter '0' to quit the program." \
       "\n******************************\n"
item = []

while True:
    request = input(menu)
    if request == '1':
        while True:
            good_type = input("Choose a good type to add:\n1. Printer\n2. Scanner\n3. Copier\n"
                              "\n0. Return to main menu\n")
            if good_type == '1':
                item = [input(f"Enter {i}: ") for i in Printer.p_features]
                printer = Printer.initial(item)
                printer.output()
                continue
            elif good_type == '2':
                item = [input(f"Enter {i}: ") for i in Scanner.s_features]
                scanner = Scanner.initial(item)
                scanner.output()
                continue
            elif good_type == '3':
                item = [input(f"Enter {i}: ") for i in Copier.c_features]
                copier = Copier.initial(item)
                copier.output()
                continue
            elif good_type == '0':
                break
            else:
                continue
    elif request == '2':
        Stock.show()
        while True:
            stock_operation = input("1. Accept goods\n2. Shipment\n3. Divisions\n\n0. Return to main menu\n")
            if stock_operation == '1':
                try:
                    to_acc = input("Enter art. no of the goods to accept: ")
                    quant = int(input("Enter quantity: "))
                except ValueError:
                    print("Goods quantity should be integer!")
                    continue
                else:
                    Stock.accept(to_acc, quant)
                    Stock.show()
                    continue
            elif stock_operation == '2':
                try:
                    to_ship = input("Enter art. no of the goods to ship: ")
                    divis = input("Enter division number (1, 2 or 3): ")
                    quant = int(input("Enter quantity: "))
                except ValueError:
                    print("Goods quantity should be integer!")
                    continue
                else:
                    Stock.ship(divis, to_ship, quant)
                    Stock.show()
                continue
            elif stock_operation == '3':
                print(f"Division 1:\n{Stock.division_1}")
                print(f"Division 2:\n{Stock.division_2}")
                print(f"Division 3:\n{Stock.division_3}")
                continue
            elif stock_operation == '0':
                break
            else:
                continue
    elif request == '3':
        while True:
            good_type = input("1. Printer\n2. Scanner\n3. Copier\n\n0. Return to main menu\n")
            if good_type == '1':
                art_no = input("Enter art. no to show printer features: ")
                Printer.info(art_no)
                continue
            elif good_type == '2':
                art_no = input("Enter art. no to show scanner features: ")
                Scanner.info(art_no)
                continue
            elif good_type == '3':
                art_no = input("Enter art. no to show copier features: ")
                Copier.info(art_no)
                continue
            elif good_type == "0":
                break
            else:
                continue
    elif request == "0":
        break
    else:
        continue
