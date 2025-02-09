from privy_io.server_auth import PrivyClient
from agentkit.config import PRIVY_APP_ID, PRIVY_APP_SECRET

# Privy クライアントの初期化
privy_client = PrivyClient(app_id=PRIVY_APP_ID, app_secret=PRIVY_APP_SECRET)

async def get_wallet_info(wallet_id: str):
    """指定したwallet_idのウォレット情報を取得する."""
    return await privy_client.walletApi.getWallet({'walletId': wallet_id})

async def sign_message(wallet_id: str, message: str):
    """指定したwallet_idでメッセージの署名を行う."""
    return await privy_client.walletApi.ethereum.signMessage({
        'walletId': wallet_id,
        'message': message
    })