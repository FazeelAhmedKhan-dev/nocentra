import asyncio
import json
from fastapi import FastAPI, WebSocket
from sim.world import WarehouseWorld

app = FastAPI()

world = WarehouseWorld()
world.add_task((5,5),(10,10))

clients = []

def serialize_world():
    return {
        "time": world.time,
        "robots": [
            {
                "id": r.id,
                "x": r.position[0],
                "y": r.position[1],
                "state": r.state,
                "battery": r.battery,
                "task": r.current_task.id if r.current_task else None
            }
            for r in world.robots
        ]
    }

async def simulation_loop():
    while True:
        world.step()
        data = serialize_world()
        for client in clients:
            await client.send_text(json.dumps(data))
        await asyncio.sleep(0.2)

@app.on_event("startup")
async def startup():
    asyncio.create_task(simulation_loop())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        clients.remove(websocket)
