from fastapi import APIRouter, Depends, HTTPException

import dependencies

router = APIRouter(
    prefix="/mount",
    tags=["mount"],
    responses={404: {"description": "Mount not found"}},
)

fake_mount = {
    "itemId": 5656,
    "iconDisplay": "https://render.worldofwarcraft.com/us/icons/56/ability_mount_ridinghorse.jpg",
    "id": 6,
    "name": "Brown Horse",
    "creatureDisplays": [
        "https://render.worldofwarcraft.com/us/npcs/zoom/creature-display-2404.jpg"
    ],
    "description": "A favorite among Stormwind's guards thanks to its patience and stamina.",
    "is_useable": "false",
    "source": {
        "type": "VENDOR",
        "name": "Brown Horse"
    }
}


@router.get("/")
async def get_mounts():
    return dependencies.get_access_token()
