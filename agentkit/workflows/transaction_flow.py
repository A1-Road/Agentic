from agentkit import Workflow
from agentkit.agents.transaction_agent import TransactionAgent
from agentkit.agents.monitoring_agent import MonitoringAgent

class TransactionWorkflow(Workflow):
    def __init__(self):
        super().__init__()
        self.monitor = MonitoringAgent()
        self.transaction = TransactionAgent()
        
    async def setup(self):
        await self.add_node(self.monitor)
        await self.add_node(self.transaction)
        await self.connect(self.monitor, self.transaction)
        
    async def run(self):
        await self.monitor.start()
        await self.transaction.start() 