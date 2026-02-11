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
         
    def handle_failures(self):
        for robot in self.robots:
            if robot.state == "failed" and robot.current_task:
                task = robot.current_task
                task.status = "pending"
                task.bids.clear()

                robot.current_task = None
                robot.task_phase = None

                run_auction(task, self.robots)

    def add_task(self, pickup, dropoff):
        task = Task(len(self.tasks), pickup, dropoff)
        self.tasks.append(task)
        run_auction(task, self.robots)

    def step(self):
        self.handle_failures()

        for robot in self.robots:
            robot.step()

        self.tasks = [t for t in self.tasks if t.status != "completed"]
        self.time += 1
    
    def kill_robot(self, robot_id):
        for robot in self.robots:
            if robot.id == robot_id:
                robot.fail()

