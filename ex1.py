# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


def out_red(text):
    print("\033[31m {}".format(text), end="")


def out_yellow(text):
    print("\033[33m {}".format(text), end="")


def out_green(text):
    print("\033[32m {}".format(text), end="")


class TrafficLight:

    __color = "black"

    def running(self, counts):
        i = 0
        while i < counts:
            TrafficLight.__color = "red"
            out_red(f"\r{TrafficLight.__color}")
            sleep(7)
            TrafficLight.__color = "yellow"
            out_yellow(f"\r{TrafficLight.__color}")
            sleep(2)
            TrafficLight.__color = "green"
            out_green(f"\r{TrafficLight.__color}")
            sleep(7)
            TrafficLight.__color = "yellow"
            out_yellow(f"\r{TrafficLight.__color}")
            sleep(2)
            i += 1


a = TrafficLight()
a.running(2)
