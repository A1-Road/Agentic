import logging
from web3 import Web3
from agentkit.config import get_wallet_info, sign_message

class Web3Tool:
    def __init__(self, rpc_endpoint: str):
        self.web3 = Web3(Web3.HTTPProvider(rpc_endpoint))

    async def send_transaction(self, wallet_id: str, target_address: str, amount_ether: float):
        try:
            # Retrieve wallet information via Privy
            wallet = await get_wallet_info(wallet_id)
            wallet_address = wallet.address

            # Retrieve gas price and nonce
            gas_price = self.web3.eth.gas_price
            nonce = self.web3.eth.get_transaction_count(wallet_address)

            tx = {
                "from": wallet_address,
                "to": target_address,
                "value": self.web3.toWei(amount_ether, 'ether'),
                "gas": 21000,  # Adjust based on actual calculation logic
                "gasPrice": gas_price,
                "nonce": nonce
            }

            # Execute Privy signature (actual implementation should sign the transaction data)
            signature_resp = await sign_message(wallet_id, "transactionData")
            signature_hex = signature_resp.signature

            # Combine signature with transaction to generate a RawTransaction (dummy implementation)
            signed_tx = self._combine_signature(tx, signature_hex)

            tx_hash = self.web3.eth.send_raw_transaction(signed_tx)
            logging.info(f"Transaction sent, hash: {tx_hash.hex()}")
            return tx_hash.hex()
        except Exception as e:
            logging.error(f"Error sending transaction: {e}")
            raise 