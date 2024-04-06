from tortoise import Tortoise
from .models import User, User_text


async def init_db(config):
    await Tortoise.init(
        db_url='sqlite:identifier.sqlite',
        modules={'models': ['tgbot.models']}
    )

    await Tortoise.generate_schemas()
