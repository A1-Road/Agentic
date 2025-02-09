# Agent Message dummy
class Agent:
    async def publish(self, message):
        print("Publishing message:", message)

class Message:
    def __init__(self, type, content=None):
        self.type = type
        self.data = content
        self.content = content