
## This agent will:
- Subscribe to blockchain block updates.
- Perform a test transaction to verify wallet functionality.
- Ask for external approval before executing a main transaction.

### Using Docker

A Dockerfile is provided to containerize the application. To build and run using Docker:

1. **Build the Docker image:**

    ```sh
    docker build -t agentkit .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 8000:8000 --env-file agentkit/.env agentkit
    ```

This starts the FastAPI server inside a Docker container, mapping port 8000 to your host.

## API Endpoints

AgentKit exposes the following API endpoints:

- **POST `/sendTransaction`**

  Sends a transaction using the provided wallet ID, target address, and amount (in Ether).

  **Request Body Example:**

  ```json
  {
      "wallet_id": "wallet123",
      "target_address": "0xd9efBA40ccf09B80b8e7Fa83FFf35187542c53BB",
      "amount": 0.001
  }
  ```

- **GET `/confirmTransaction`**

  Confirms a transaction by providing the transaction hash (`tx_hash`) as a query parameter.

  **Example:**

  ```
  GET /confirmTransaction?tx_hash=0xabc123...
  ```

## Customization and Extensibility

- **Agents**: Extend or create new agents by modifying files under `agentkit/agents`. Each agent extends the base `Agent` class.
- **Tools**: Utilities for blockchain interaction and substreams simulation are located in `agentkit/tools`.
- **Configuration**: All configurable parameters are loaded from environment variables in `agentkit/config.py`.

## Troubleshooting

- **Environment Variables**: Make sure the `.env` file has the correct values for RPC endpoints and Privy authentication.
- **Network Issues**: Verify connectivity to Infura or your Ethereum node.
- **Container Issues**: When running with Docker, ensure the environment file is properly referenced with the `--env-file` flag.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests with your improvements. Ensure that you maintain the existing coding style and include tests when applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
