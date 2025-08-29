import logging
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Utils

SINGLETON_ID = 1


async def get_utils(
        session: AsyncSession) -> Optional[Utils]:
    return await session.get(Utils, SINGLETON_ID)


async def get_channel_invite_link(session: AsyncSession) -> str | None:
    utils = await get_utils(session)
    if utils and utils.get_channel_invite_link():
        return utils.get_channel_invite_link()
    return None

async def update_channel_invite_link(
        session: AsyncSession,
        channel_invite_link: str,
        ) -> str:
    utils = Utils(SINGLETON_ID, channel_invite_link)
    session.add(utils)

    await session.flush()
    await session.commit()
    logging.info(f"Channel invite link updated: {utils.get_channel_invite_link()}")
    return utils.get_channel_invite_link()
