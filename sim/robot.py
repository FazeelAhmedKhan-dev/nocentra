import math
from sim.config import MOVE_COST

class RobotAgent:
    def __init__(self, robot_id, position):
        self.id = robot_id
        self.position = position
        self.battery = 100
        self.current_task = None
        self.state = "idle"
	self.task_phase = None

    def distance(self, point):
        return abs(self.position[0] - point[0]) + abs(self.position[1] - point[1])

    def compute_bid(self, task):
        if self.state != "idle":
            return None
        cost = self.distance(task.pickup) + (100 - self.battery) * 0.1
        return cost

    def receive_task_announcement(self, task):
        bid = self.compute_bid(task)
        if bid is not None:
            task.collect_bid(self.id, bid)

    def assign_task(self, task):
        self.current_task = task
	self.task_phase = "pickup"
        self.state = "executing"

    def step(self):
        if self.current_task:
            self.move_towards(self.current_task.pickup)

    def move_towards(self, target):
        x, y = self.position
        tx, ty = target

        if x < tx:
            x += 1
        elif x > tx:
            x -= 1
        elif y < ty:
            y += 1
        elif y > ty:
            y -= 1

        self.position = (x, y)
        self.battery -= MOVE_COST

