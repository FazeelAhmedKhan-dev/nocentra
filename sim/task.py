class Task:
    def __init__(self, task_id, pickup, dropoff):
        self.id = task_id
        self.pickup = pickup
        self.dropoff = dropoff
        self.status = "pending"
        self.bids = {}

    def announce(self, robots):
        for robot in robots:
            robot.receive_task_announcement(self)

    def collect_bid(self, robot_id, bid_value):
        self.bids[robot_id] = bid_value

    def assign(self):
        if not self.bids:
            return None
        winner = min(self.bids, key=self.bids.get)
        self.status = "assigned"
        return winner
