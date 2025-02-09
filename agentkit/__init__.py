import logging

# 必要なモジュールのインポート
from .workflow import Workflow
from .agents.base import Agent, Message

# 本番環境用のロガー設定
logger = logging.getLogger("agentkit")
logger.setLevel(logging.INFO)

# ハンドラがまだ設定されていなければ追加
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# パッケージの公開APIを明示
__all__ = [
    "Workflow",
    "Agent",
    "Message",
]

class Agent:
    async def publish(self, message):
        print("Publishing message:", message)

class Message:
    def __init__(self, type, content=None):
        self.type = type
        self.data = content
        self.content = content