from agentkit import Agent, Message
from tools.substreams_tool import SubstreamsTool
from agentkit.config import Config

class MonitoringAgent(Agent):
    def __init__(self):
        super().__init__()
        self.substreams = SubstreamsTool()
        self.last_block = int(os.getenv("START_BLOCK", Config.START_BLOCK))

    async def monitor_network(self):
        async for block in self.substreams.stream_transfers(self.last_block):
            await self.publish(
                Message("block_update", block)
            )
            self.last_block = block['number'] + 1 