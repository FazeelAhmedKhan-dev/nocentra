from sim.world import WarehouseWorld
import time

world = WarehouseWorld()

world.add_task((5, 5), (10, 10))
world.add_task((2, 6), (8, 1))
world.add_task((15, 3), (1, 1))

for _ in range(20):
    world.step()
    print("Time:", world.time)
    for r in world.robots:
        print(
            f"Robot {r.id} | Pos {r.position} | "
            f"State {r.state} | Phase {r.task_phase}"
        )
    print("-" * 30)
    time.sleep(0.2)

