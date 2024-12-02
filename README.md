# ChainPilot-cli

# ChainPilot: Blockchain Interaction Agent

## Overview

ChainPilot is an advanced blockchain interaction agent built on the Coinbase Developer Platform (CDP) SDK, designed to perform various blockchain tasks on the Base Layer 2 network autonomously or through interactive modes.

## Features

### Blockchain Interactions
- Create ERC-20 tokens
- Transfer assets
- Check wallet balances
- Deploy NFT contracts
- Mint NFTs
- Register Basenames
- Swap assets (on Base Mainnet)
- Request testnet ETH from faucet

### Modes of Operation
1. **Chat Mode**: Interactive command-line interface
2. **Autonomous Mode**: Agent takes creative actions independently
3. **Two-Agent Mode**: Conversation between ChainPilot and an OpenAI-powered guide

## Prerequisites

- Python 3.8+
- Coinbase Developer Platform (CDP) account
- OpenAI API key (optional)
- Base network (Mainnet or Sepolia testnet)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ChainPilot.git
cd ChainPilot
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with the following:
```
CDP_API_KEY_NAME=your_cdp_api_key
CDP_PRIVATE_KEY=your_private_key
OPENAI_API_KEY=your_openai_api_key  # Optional
```

## Usage

Run the ChainPilot agent:
```bash
python run.py
```

### Mode Selection
- **Chat Mode**: Interactively run blockchain commands
- **Autonomous Mode**: Agent performs actions automatically
- **Two-Agent Mode**: AI-guided blockchain exploration

## Functions

ChainPilot supports multiple blockchain-related functions:
- `create_token`: Deploy custom ERC-20 tokens
- `transfer_asset`: Send assets between wallets
- `get_balance`: Check wallet asset balances
- `deploy_nft`: Create NFT collections
- `mint_nft`: Mint individual NFTs
- `register_basename`: Register blockchain domain names
- `swap_assets`: Exchange tokens (Mainnet only)

## Research Capabilities

Includes a built-in Research Agent for cryptocurrency and blockchain market research using DuckDuckGo search.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Contact

Project Link: [https://github.com/puneetred/ChainPilot](https://github.com/puneetred/ChainPilot)
