from cosmos.core.cosmos import Cosmos

if __name__ == "__main__":
    bot = Cosmos()
    bot.log.info(f"All initial tasks completed. [{bot.time.round_time()} seconds.]")
    bot.run()
