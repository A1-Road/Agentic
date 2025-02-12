# Fetch Wallet Data (English Version)

This project provides a Python script to set up an AI agent for fetching Ethereum transaction details.

## File Structure

- `fetch_wallet_data.py`: Main script for fetching Ethereum transaction details.
- `check_reputation.py`: Script for checking reputation based on commands.

## Required Libraries

This script uses the following libraries:

- `langchain_core`
- `pydantic`
- `langchain_openai`
- `dotenv`
- `cdp_langchain`
- `flask`

## Environment Variables Setup

The script uses environment variables for configuration. Create a `.env` file and set the necessary environment variables.

## Script Description

### `fetch_wallet_data.py`

This script analyzes the details of an Ethereum transaction input by the user and generates output according to the specified format.

### Input

The user inputs a prompt containing the details of an Ethereum transaction. For example:

```plaintext
Send 0.0005 ETH to 0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a
```

### Output

The script generates transaction information based on the input prompt and returns the following output:

```json
{
    "amount": 0.0005,
    "who": "0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a"
}
```

### Script Flow

1. Import necessary libraries and load environment variables.
2. Instantiate the `ChatOpenAI` model.
3. Define the `EthTransaction` Pydantic model.
4. Create a `PydanticOutputParser`.
5. Generate format instructions.
6. Set up the prompt template.
7. Create and execute the langchain.

Here is the main part of the script:

```python
# filepath: /workspaces/codespaces-jupyter/Agentic/backend/fetch_wallet_data.py
// ...existing code...
```

### `check_reputation.py`

This script checks reputation based on a command and returns the result.

### Input

The user inputs a command to check reputation. For example:

```plaintext
Check the reputation of 0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a
```

### Output

The script generates reputation information based on the input command and returns the following output:

```json
{
    "output": true
}
```

### Script Flow

1. Import necessary libraries and load environment variables.
2. Instantiate the `CdpAgentkitWrapper`.
3. Create the `CdpToolkit`.
4. Instantiate the `ChatOpenAI` model.
5. Create and execute the agent.
6. Set up and run the Flask application.

Here is the main part of the script:

```python
# filepath: /workspaces/codespaces-jupyter/Agentic/backend/in_progress_takara/check_reputation.py
// ...existing code...
```

## How to Run

1. Install the required libraries.
2. Create a `.env` file and set the necessary environment variables.
3. Run the script.

```bash
python fetch_wallet_data.py
```

or

```bash
python check_reputation.py
```

This script analyzes the details of the command input by the user and generates output according to the specified format.

---

# Fetch Wallet Data

このプロジェクトは、Ethereumトランザクションの詳細を取得するためのAIエージェントを設定するPythonスクリプトを提供します。

## ファイル構成

- `fetch_wallet_data.py`: Ethereumトランザクションの詳細を取得するためのメインスクリプト。
- `check_reputation.py`: コマンドに基づいて評判をチェックするためのスクリプト。

## 必要なライブラリ

このスクリプトは以下のライブラリを使用しています：

- `langchain_core`
- `pydantic`
- `langchain_openai`
- `dotenv`
- `cdp_langchain`
- `flask`

## 環境変数の設定

スクリプトは環境変数を使用して設定を読み込みます。`.env` ファイルを作成し、必要な環境変数を設定してください。

## スクリプトの説明

### `fetch_wallet_data.py`

このスクリプトは、ユーザーが入力したEthereumトランザクションの詳細を解析し、指定されたフォーマットに従って出力を生成します。

### 入力

ユーザーは、Ethereumトランザクションの詳細を含むプロンプトを入力します。例えば、以下のような入力があります：

```plaintext
Send 0.0005 ETH to 0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a
```

### 出力

スクリプトは、入力されたプロンプトに基づいてトランザクション情報を生成し、以下のような出力を返します：

```json
{
    "amount": 0.0005,
    "who": "0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a"
}
```

### スクリプトの流れ

1. 必要なライブラリのインポートと環境変数の読み込み。
2. `ChatOpenAI` モデルのインスタンス化。
3. `EthTransaction` というPydanticモデルの定義。
4. `PydanticOutputParser` の作成。
5. フォーマット指示の生成。
6. プロンプトテンプレートの設定。
7. langchainの作成と実行。

以下は、スクリプトの主要部分です：

```python
# filepath: /workspaces/codespaces-jupyter/Agentic/backend/fetch_wallet_data.py
// ...existing code...
```

### `check_reputation.py`

このスクリプトは、コマンドに基づいて評判をチェックし、結果を返します。

### 入力

ユーザーは、評判をチェックするためのコマンドを入力します。例えば、以下のような入力があります：

```plaintext
Check the reputation of 0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a
```

### 出力

スクリプトは、入力されたコマンドに基づいて評判情報を生成し、以下のような出力を返します：

```json
{
    "output": true
}
```

### スクリプトの流れ

1. 必要なライブラリのインポートと環境変数の読み込み。
2. `CdpAgentkitWrapper` のインスタンス化。
3. `CdpToolkit` の作成。
4. `ChatOpenAI` モデルのインスタンス化。
5. エージェントの作成と実行。
6. Flaskアプリケーションの設定と実行。

以下は、スクリプトの主要部分です：

```python
# filepath: /workspaces/codespaces-jupyter/Agentic/backend/in_progress_takara/check_reputation.py
// ...existing code...
```

## 実行方法

1. 必要なライブラリをインストールします。
2. `.env` ファイルを作成し、必要な環境変数を設定します。
3. スクリプトを実行します。

```bash
python fetch_wallet_data.py
```

または

```bash
python check_reputation.py
```

このスクリプトは、ユーザーが入力したコマンドの詳細を解析し、指定されたフォーマットに従って出力を生成します。