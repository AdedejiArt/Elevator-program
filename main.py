#The author of the code is Adio Adedeji
#We imported some necessary tools
import argparse
import sys
import time
import numpy as np


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-floor', '--floor')
    parser.add_argument('-floor_height', '--floor_height')
    parser.add_argument('-speed', '--speed')
    parser.add_argument('-doors', '--doors')

    return parser


parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
timeout = 3.0


class Floor:
    def __init__(self, max_floor, height):
        self.max_floor = int(max_floor)
        self.start_floor = 1
        self.current = 1
        self.current2 = 1
        self.height = height
        self.dest_floor = []

    def check_start_floor(self, new_start_floor):
        if new_start_floor > self.max_floor or new_start_floor < 1:
            print("Floor number is incorrect")
        else:
            self.start_floor = new_start_floor

    def calculate_multiple_floors(self, new_floors):
        a = np.array(new_floors)
        while len(a) > 0:
            i = np.argmin(np.abs(a - self.current2))
            self.dest_floor.append(a[i])
            a = np.delete(a, i)
        for j in self.dest_floor[:]:
            if j > int(self.max_floor):
                self.dest_floor.remove(j)
            elif j < 1:
                self.dest_floor.remove(j)

    def calculate_one_floor(self, new_floors):
        self.dest_floor.append(new_floors)
        if self.dest_floor[0] > int(self.max_floor):
            self.dest_floor = []


class Elevator:
    def __init__(self, speed, doors):
        self.speed = int(speed)
        self.doors = int(doors)

    def route(self, floor_height, speed):
        return int(floor_height) / int(speed)

    def move_up(self, route, floor):
        while floor.current < floor.start_floor:
            print("current floor: %d" % floor.current)
            floor.current += 1
            time.sleep(route)
        print("current floor: %d" % floor.current)
        print("elevator opens the doors")
        time.sleep(self.doors)
        print("elevator opened the doors")
        floor.current2 = floor.current

    def move_down(self, route, floor):
        while floor.current > floor.start_floor:
            print("current floor: %d" % floor.current)
            floor.current -= 1
            time.sleep(route)
        print("current floor: %d" % floor.current)
        print("elevator opens the doors")
        time.sleep(self.doors)
        print("elevator opened the doors")
        floor.current2 = floor.current

    def press_button(self, route, floor):
        print("elevator closes the doors")
        time.sleep(self.doors)
        print("elevator closes the doors")

        for j in floor.dest_floor[:]:

            if floor.current2 < j:
                while floor.current2 < j:
                    print("current floor: %d" % floor.current2)
                    floor.current2 += 1
                    time.sleep(route)
                print("current floor: %d" % floor.current2)
                print("elevator opens the doors")
                time.sleep(self.doors)
                print("elevator opened the doors")
                print("elevator closes the doors")
                time.sleep(self.doors)
                print("elevator closed the doors")

            elif floor.current2 > j:
                while floor.current2 > j:
                    print("current floor: %d" % floor.current2)
                    floor.current2 -= 1
                    time.sleep(route)
                print("current floor: %d" % floor.current2)
                print("elevator opens the doors")
                time.sleep(self.doors)
                print("elevator opened the doors")
                print("elevator closes the doors")
                time.sleep(self.doors)
                print("elevator closed the doors")
            floor.dest_floor.remove(j)


def main():
    elevator = Elevator(namespace.speed, namespace.doors)
    floor = Floor(namespace.floor, namespace.floor_height)
    route = elevator.route(floor.height, elevator.speed)
    if floor.start_floor != 0:
            if floor.current < floor.start_floor:
                elevator.move_up(route, floor)
            elif floor.current > floor.start_floor:
                elevator.move_down(route, floor)
                if floor.dest_floor != []:
                    elevator.press_button(route, floor)

main()