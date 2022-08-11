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
        "namespace": f"profile-{region}",
        "locale": "en_US",
    }

    return utils.blizzard.get_data_from_api(region, f"/profile/wow/character/{slug}/{char_name}", params)


@router.get("/mounts/{region}/{slug}/{char_name}")
async def get_character_mounts(region: str, slug: str, char_name: str):
    params = {
        "namespace": f"profile-{region}",
        "locale": "en_US",
    }

    return utils.blizzard.get_data_from_api(region,
                                            f"/profile/wow/character/{slug}/{char_name}/collections/mounts",
                                            params)


@router.get("/media/{region}/{slug}/{char_name}")
async def get_character_media(region: str, slug: str, char_name: str):
    params = {
        "namespace": f"profile-{region}",
        "locale": "en_US",
    }

    return utils.blizzard.get_data_from_api(region,
                                            f"/profile/wow/character/{slug}/{char_name}/character-media",
                                            params)
