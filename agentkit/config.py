import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Privy Auth
    PRIVY_APP_ID = os.getenv("PRIVY_APP_ID")
    PRIVY_APP_SECRET = os.getenv("PRIVY_APP_SECRET")
    
    # Substreams 関連（不要なので削除またはコメントアウト）
    # SUBSTREAMS_ENDPOINT = os.getenv("SUBSTREAMS_ENDPOINT", "mainnet.eth.streamingfast.io:443")
    # SUBSTREAMS_API_KEY = os.getenv("SUBSTREAMS_API_KEY")
    # SUBSTREAMS_MODULES = os.getenv("SUBSTREAMS_MODULES", "default_module")  # 利用するSubstreamsモジュールを指定
    # OUTPUT_MODULE = os.getenv("OUTPUT_MODULE", "map_transfers")
    
    # Web3設定
    RPC_ENDPOINT = os.getenv("RPC_ENDPOINT", "https://base-sepolia.infura.io/v3/87b3eb85dee44e4fa2f3085229f95fad")
    # PRIVATE_KEY は、Privy API 経由で署名を実施するため、本番環境では利用しません。
    PRIVATE_KEY = ""
    TARGET_ADDRESS = os.getenv("TARGET_ADDRESS", "0x...")
    
    POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", 60))
    TEST_AMOUNT = float(os.getenv("TEST_AMOUNT", 0.001))
    MAIN_AMOUNT = float(os.getenv("MAIN_AMOUNT", 1.0)) 
    
    START_BLOCK = "0"
    
    INFURA_URL = os.getenv("INFURA_URL", "https://base-sepolia.infura.io/v3/87b3eb85dee44e4fa2f3085229f95fad")
    
    TEST_RECIPIENT_ADDRESS = "0xd9efBA40ccf09B80b8e7Fa83FFf35187542c53BB"