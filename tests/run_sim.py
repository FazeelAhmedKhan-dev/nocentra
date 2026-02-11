from sim.world import WarehouseWorld
import time

world = WarehouseWorld()

world.add_task((5, 5), (10, 10))

for t in range(30):

    world.step()

    if t == 5:
        print("\n💥 Killing robot that is executing\n")
        # kill whichever robot currently has a task
        for r in world.robots:
            if r.state == "executing":
                world.kill_robot(r.id)
                break

    print("Time:", world.time)
    for r in world.robots:
        print(
            f"Robot {r.id} | Pos {r.position} | "
            f"State {r.state} | Phase {r.task_phase}"
        )
    print("-" * 30)
    time.sleep(0.2)

