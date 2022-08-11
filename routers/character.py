from fastapi import APIRouter, Depends, HTTPException

import utils.blizzard

router = APIRouter(
    prefix="/character",
    tags=["character"],
    responses={404: {"description": "Character not found"}},
)


@router.get("/")
async def test():
    return "Hello Character"


@router.get("/{region}/{slug}/{char_name}")
async def get_character(region: str, slug: str, char_name: str):
    params = {
        "namespace": "static-eu",
        "locale": "en_US",
    }

    return utils.blizzard.get_data_from_api(region, f"/profile/wow/character/{slug}/{char_name}", params)
