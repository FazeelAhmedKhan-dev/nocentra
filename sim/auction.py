def run_auction(task, robots):
    task.announce(robots)
    winner_id = task.assign()

    if winner_id is None:
        return

    for robot in robots:
        if robot.id == winner_id:
            robot.assign_task(task)

