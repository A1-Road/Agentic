class Agent:
    def __init__(self):
        pass

    async def setup(self):
        pass

    async def handle_message(self, message):
        pass


class Message:
    def __init__(self, type, content):
        self.type = type
        self.content = content 