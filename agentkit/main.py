import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agentkit.tools.web3_tool import Web3Tool

app = FastAPI()
web3_tool = Web3Tool()

class TxRequest(BaseModel):
    wallet_id: str
    target_address: str
    amount: float

@app.post("/sendTransaction")
async def send_transaction(req: TxRequest):
    try:
        tx_hash = await web3_tool.send_transaction(
            wallet_id=req.wallet_id,
            target_address=req.target_address,
            amount_ether=req.amount
        )
        return {"success": True, "tx_hash": tx_hash}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/confirmTransaction")
async def confirm_transaction(tx_hash: str):
    try:
        receipt = await web3_tool.confirm_transaction(tx_hash)
        if receipt and receipt.get("status") == 1:
            return {"success": True, "receipt": receipt}
        else:
            return {"success": False, "receipt": receipt}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)