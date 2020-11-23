# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            print("Siren sound!")
        print(f"Car {self.name} is ready to go!")

    def stop(self):
        print(f"Car {self.name} has successfully stopped. Hope you've enjoyed your ride!")

    def turn(self, direction):
        print(f"Car {self.name} has turned {direction}.")

    def show_speed(self):
        print(f"Current speed of car {self.name} is {self.speed}")


class TownCar(Car):

    def show_speed(self):
        print(f"Current speed of car {self.name} is {self.speed}")
        if self.speed > 60:
            print("Slow down!")


class SportCar(Car):

    def drift(self):
        print(f"Car {self.name} vzzzzzzzzzh!")


class WorkCar(Car):

    def show_speed(self):
        print(f"Current speed of car {self.name} is {self.speed}")
        if self.speed > 40:
            print("Slow down!")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


print("To start a car press: 't' for a town car, 'w' - work car, 's' - sport car, and 'p' - police car.\nUse 'a' to "
      "turn left and 'd' to turn right, press 'x' to drift with a sport car and 'z' to show current speed.\nPress 'q' "
      "to stop your car and exit.")

while True:
    key = input("")
    if key == 't':
        t_speed = int(input("Enter car speed: "))
        t_color = input("Enter car color: ")
        t_name = input("Enter car name: ")
        t = TownCar(t_speed, t_color, t_name)
        t.go()
        while True:
            key_driving = input("")
            if key_driving == 'a':
                t.turn('left')
                continue
            elif key_driving == 'd':
                t.turn('right')
                continue
            elif key_driving == 'x':
                print("Only a sport car can drift!")
                continue
            elif key_driving == 'z':
                t.show_speed()
                continue
            elif key_driving == 'q':
                t.stop()
                break
            else:
                print("Use 'a' to turn left and 'd' to turn right, press 'x' to drift with a sport car and 'z' "
                      "to show current speed.\nPress 'q' to stop your car and exit.")
                continue
        break

    if key == 'w':
        w_speed = int(input("Enter car speed: "))
        w_color = input("Enter car color: ")
        w_name = input("Enter car name: ")
        w = WorkCar(w_speed, w_color, w_name)
        w.go()
        while True:
            key_driving = input("")
            if key_driving == 'a':
                w.turn('left')
                continue
            elif key_driving == 'd':
                w.turn('right')
                continue
            elif key_driving == 'x':
                print("Only a sport car can drift!")
                continue
            elif key_driving == 'z':
                w.show_speed()
                continue
            elif key_driving == 'q':
                w.stop()
                break
            else:
                print("Use 'a' to turn left and 'd' to turn right, press 'x' to drift with a sport car and 'z' "
                      "to show current speed.\nPress 'q' to stop your car and exit.")
                continue
        break

    if key == 's':
        s_speed = int(input("Enter car speed: "))
        s_color = input("Enter car color: ")
        s_name = input("Enter car name: ")
        s = SportCar(s_speed, s_color, s_name)
        s.go()
        while True:
            key_driving = input("")
            if key_driving == 'a':
                s.turn('left')
                continue
            elif key_driving == 'd':
                s.turn('right')
                continue
            elif key_driving == 'x':
                s.drift()
                continue
            elif key_driving == 'z':
                s.show_speed()
                continue
            elif key_driving == 'q':
                s.stop()
                break
            else:
                print("Use 'a' to turn left and 'd' to turn right, press 'x' to drift with a sport car and 'z' "
                      "to show current speed.\nPress 'q' to stop your car and exit.")
                continue
        break

    if key == 'p':
        p_speed = int(input("Enter car speed: "))
        p_color = input("Enter car color: ")
        p_name = input("Enter car name: ")
        p = PoliceCar(p_speed, p_color, p_name)
        p.go()
        while True:
            key_driving = input("")
            if key_driving == 'a':
                p.turn('left')
                continue
            elif key_driving == 'd':
                p.turn('right')
                continue
            elif key_driving == 'x':
                print("Only a sport car can drift!")
                continue
            elif key_driving == 'z':
                p.show_speed()
                continue
            elif key_driving == 'q':
                p.stop()
                break
            else:
                print("Use 'a' to turn left and 'd' to turn right, press 'x' to drift with a sport car and 'z' "
                      "to show current speed.\nPress 'q' to stop your car and exit.")
                continue
        break
