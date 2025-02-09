import asyncio
from agentkit import Agent, Message
from agentkit.tools.web3_tool import TransactionTool
from agentkit.tools.fraud_detector import FraudDetector
from agentkit.config import Config
import os

class TransactionAgent(Agent):
    def __init__(self):
        super().__init__()
        self.transaction = TransactionTool()
        self.detector = FraudDetector()
        self.last_block = int(os.getenv("START_BLOCK", Config.START_BLOCK))
        
    async def setup(self):
        await self.subscribe("block_update")
        print("TransactionAgent setup complete.")
        # Initialize any additional components if needed.
        
    async def handle_message(self, message: Message):
        if message.type == "block_update":
            await self.process_blocks(message.content)
        elif message.type == "external_trigger":
            print("Received external trigger message with data:", message.data)
            
            # Step 1: Execute a small test transaction to verify wallet functionality.
            print("Executing a small test transaction to verify wallet functionality...")
            try:
                test_tx_hash = self.transaction.send_transaction(Config.TEST_RECIPIENT_ADDRESS)
                print("Test transaction sent successfully! Tx hash:", test_tx_hash.hex())
            except Exception as e:
                print("Test transaction failed:", e)
                # Abort further processing if the test transaction fails.
                return
            
            # Step 2: Wait for external approval before performing the main transaction.
            approval = input("Please approve the main transaction (enter 'ok' to proceed): ")
            if approval.lower() == "ok":
                print("Approval received. Executing main wallet transaction...")
                try:
                    main_tx_hash = self.transaction.send_transaction(Config.ACTUAL_RECIPIENT_ADDRESS)
                    print("Main wallet transaction sent successfully! Tx hash:", main_tx_hash.hex())
                except Exception as e:
                    print("Main wallet transaction failed:", e)
            else:
                print("Approval not received. Aborting main wallet transaction.")
            
    async def process_blocks(self, blocks):
        for block in blocks:
            if self.detector.analyze(block):
                await self.trigger_alarm(block)
                return
                
        await self.execute_transaction_flow()
        
    async def trigger_alarm(self, block):
        print(f"Fraud detected in block {block['number']}")
        await self.publish(
            Message("system_alert", {"type": "fraud", "block": block})
        )
        
    async def execute_transaction_flow(self):
        try:
            tx_hash = self.transaction.send_transaction(Config.TEST_RECIPIENT_ADDRESS)
            print("Transaction sent! Tx hash:", tx_hash.hex())
        except Exception as e:
            print("Transaction failed:", e)

    async def subscribe(self, event_type: str):
        """
        ダミーのsubscribeメソッドです。
        サブストリーム等からの実際の購読処理がない場合は、単にログ出力するだけにします。
        """
        print(f"Simulated subscription to event: {event_type}")
        # シミュレーションのため、ここで待機や何か処理を入れる場合は追加できます 

# Sample asynchronous execution demonstrating the external trigger flow.
async def main():
    agent = TransactionAgent()
    await agent.setup()

    # Create a dummy external trigger message.
    dummy_data = {"info": "trigger transaction sequence"}
    message = Message("external_trigger", dummy_data)
    
    # Pass the message to the agent for processing.
    await agent.handle_message(message)

if __name__ == '__main__':
    asyncio.run(main()) 