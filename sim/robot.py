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
        self.failed = False
    
    def fail(self):
        self.failed = True
        self.state = "failed"

    def distance(self, point):
        return abs(self.position[0] - point[0]) + abs(self.position[1] - point[1])

    def handle_arrival(self):
        if self.task_phase == "pickup":
            self.task_phase = "dropoff"
            self.current_task.status = "picked"
        
        elif self.task_phase == "dropoff":
            self.current_task.status = "completed"
            self.current_task = None
            self.task_phase = None
            self.state = "idle"

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

        if self.failed:
            return
        
        if self.battery <= 0:
            self.state = "failed"
            return
        
        if self.state != "executing" or not self.current_task:
            return
        
        if self.task_phase == "pickup":
            target = self.current_task.pickup
        
        else:
            target = self.current_task.dropoff
        
        if self.position == target:
            self.handle_arrival()
        
        else:
            self.move_towards(target)


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
        self.battery = max(0, self.battery - MOVE_COST)

