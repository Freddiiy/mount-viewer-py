from fastapi import APIRouter, Depends, HTTPException

import utils.oauth
import utils.blizzard

router = APIRouter(
    prefix="/mount",
    tags=["mount"],
    responses={404: {"description": "Mount not found"}},
)


@router.get("/")
async def get_mounts():
    params = {
        "namespace": "static-eu",
        "locale": "en_US",
    }

    return utils.blizzard.get_data_from_api("eu", "/data/wow/mount/index", params)


@router.get("/{mount_id}")
async def get_mount(mount_id: int):
    params = {
        "namespace": "static-eu",
        "locale": "en_US",
    }

    return utils.blizzard.get_data_from_api("eu", f"/data/wow/mount/{mount_id}", params)
