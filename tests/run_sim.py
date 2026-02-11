from sim.world import WarehouseWorld
import time

world = WarehouseWorld()

world.add_task((5, 5), (10, 10))

for t in range(30):

    if t == 0:
        print("\n Robot 4 Failed \n")
        world.kill_robot(4)
        
    world.step()
    print("Time:", world.time)
    for r in world.robots:
        print(
            f"Robot {r.id} | Pos {r.position} | "
            f"State {r.state} | Phase {r.task_phase}"
        )
    print("-" * 30)
    time.sleep(0.2)

