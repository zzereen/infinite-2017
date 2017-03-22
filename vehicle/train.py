from vehicle.robot import Robot
from vehicle.driver import Driver, DriverListener
from railway.route import Route

from enum import IntEnum


class Train(DriverListener):
    class State(IntEnum):
        RUNNING = 0
        STOPPED = 1

    def __init__(self):
        self.robot = Robot()
        self.driver = Driver()
        self.state = self.State.STOPPED

        self.driver.add_listener(self)

    def start(self, route: 'Route'):
        if self.state == self.State.STOPPED:
            self.driver.set_route(route)
            self.state = self.State.RUNNING

            while True:
                self.robot.step()

    def stop(self, is_immediate: bool):
        if is_immediate:
            self.driver.clear_route()
            self.state = self.State.STOPPED

    def on_end_station_reached(self, station: 'Station', line: 'Line'):
        self.stop(True)