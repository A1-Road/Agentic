import asyncio
import logging
from agentkit.agents.transaction_agent import TransactionAgent
from config import Config

logger = logging.getLogger("agentkit.workflow")

class Workflow:
    def __init__(self):
        # 必要に応じて他のエージェントも初期化する
        self.transaction_agent = TransactionAgent()
    
    async def setup(self):
        logger.info("Setting up workflow and agents...")
        await self.transaction_agent.setup()
        # 他のエージェントのセットアップも呼び出す
    
    async def run(self):
        await self.setup()
        logger.info("Starting the transaction verification flow...")
        
        # Execute a small test transaction for verification
        try:
            logger.info("Executing small test transaction for verification...")
            wallet_id = "your_test_wallet_id"  # 実際は動的に取得するか設定値を利用
            test_tx_hash = await self.transaction_agent.transaction.send_transaction(
                wallet_id,
                Config.TEST_RECIPIENT_ADDRESS,
                Config.TEST_AMOUNT
            )
            print("Test transaction sent! Tx hash:", test_tx_hash)
        except Exception as e:
            logger.error("Test transaction failed: %s", e)
            return
        
        # Wait for approval to proceed with the main transaction
        approval = input("Test transaction executed. Approve main transaction? (enter 'ok' to proceed): ")
        if approval.lower() == "ok":
            logger.info("Approval received. Executing main transaction...")
            try:
                main_tx_hash = await self.transaction_agent.transaction.send_transaction(
                    wallet_id,
                    Config.TARGET_ADDRESS,
                    Config.MAIN_AMOUNT
                )
                print("Main transaction sent! Tx hash:", main_tx_hash)
            except Exception as e:
                logger.error("Main transaction failed: %s", e)
        else:
            logger.info("Approval not received. Aborting the main transaction.")
        
        logger.info("Workflow completed.")

# ワークフローを直接実行する場合のエントリーポイント
if __name__ == "__main__":
    wf = Workflow()
    asyncio.run(wf.run()) 