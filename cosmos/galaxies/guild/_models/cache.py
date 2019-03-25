from .guild_profile import CosmosGuild


class GuildCache(object):

    def __init__(self, plugin):
        self.plugin = plugin
        self.bot = self.plugin.bot
        self.redis = None
        self.collection = self.plugin.collection
        self.bot.loop.create_task(self.__fetch_redis_client())

    async def __fetch_redis_client(self):
        await self.bot.wait_until_ready()
        self.redis = self.bot.cache.redis

    async def get_profile(self, guild_id) -> CosmosGuild:
        profile = await self.redis.get_object(self.collection.name, guild_id)
        if not profile:
            profile_document = (await self.collection.find_one({"guild_id": guild_id})) or {"guild_id": guild_id}
            profile = CosmosGuild.from_document(profile_document)
            await self.redis.set_object(self.collection.name, guild_id, profile)
        return profile
