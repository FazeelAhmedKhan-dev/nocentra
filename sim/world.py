from sim.robot import RobotAgent
from sim.task import Task
from sim.auction import run_auction
from sim.config import NUM_ROBOTS

class WarehouseWorld:
    def __init__(self):
        self.robots = [
            RobotAgent(i, (i, 0)) for i in range(NUM_ROBOTS)
        ]
        self.tasks = []
        self.time = 0

    def add_task(self, pickup, dropoff):
        task = Task(len(self.tasks), pickup, dropoff)
        self.tasks.append(task)
        run_auction(task, self.robots)

    def step(self):
        for robot in self.robots:
            robot.step()
        self.tasks = [t for t in self.tasks if t.status != "completed"]
        self.time += 1

