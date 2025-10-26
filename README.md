# Agent SDK Environment Setup

Interactive CLI tool to quickly set up various agent development kits (SDKs) on your system.

## Features

- **Interactive CLI Interface**: User-friendly menu system with color-coded output
- **Language Filtering**: Select SDKs by programming language (Python, TypeScript/JavaScript, Rust)
- **Multi-SDK Support**: Install multiple agent SDKs in a single session (21 SDKs supported)
- **Flexible Directory Management**: Choose default or custom installation paths
- **Organized SDK Display**: SDKs displayed with language tags for easy identification
- **JSON Configuration**: Easily extensible SDK configuration via `sdks.json`
- **Error Handling**: Robust error handling and validation
- **Progress Tracking**: Real-time installation progress and status updates

## Supported Agent SDKs

### Python (13 SDKs)
| SDK | Repository | Description |
|-----|------------|-------------|
| Arcade AI | [arcade-ai](https://github.com/ArcadeAI/arcade-ai) | Arcade AI agent development kit |
| AutoGen | [autogen](https://github.com/microsoft/autogen) | Microsoft's multi-agent conversation framework |
| Claude Agent SDK | [claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | Anthropic's official Claude agent SDK |
| CrewAI | [crewAI](https://github.com/joaomdmoura/crewAI) | Beginner-friendly multi-agent collaboration |
| Google ADK | [adk-python](https://github.com/google/adk-python) | Google Agent Development Kit |
| IBM Watson | [ibm-watsonx-orchestrate-adk](https://github.com/IBM/ibm-watsonx-orchestrate-adk) | IBM Watson Orchestrate ADK |
| LangChain | [langchain](https://github.com/langchain-ai/langchain) | Popular AI agent framework with extensive ecosystem |
| LangGraph | [langgraph](https://github.com/langchain-ai/langgraph) | Graph-based agent orchestration |
| Microsoft Agents | [Agents](https://github.com/microsoft/Agents) | Microsoft Agent Framework |
| Nerve | [nerve](https://github.com/evilsocket/nerve) | Nerve agent development kit |
| OpenAI Agents | [openai-agents-python](https://github.com/openai/openai-agents-python) | OpenAI Agents Python SDK |
| Qwen Agent | [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | Qwen Agent Framework |
| Semantic Kernel | [semantic-kernel](https://github.com/microsoft/semantic-kernel) | Microsoft's enterprise AI orchestration |

### TypeScript/JavaScript (6 SDKs)
| SDK | Repository | Description |
|-----|------------|-------------|
| ADK TypeScript | [adk-typescript](https://github.com/njraladdin/adk-typescript) | TypeScript port of Google's ADK |
| AgentKit | [agent-kit](https://github.com/inngest/agent-kit) | Multi-provider agent framework with MCP support |
| Claude Agent SDK TS | [claude-agent-sdk-typescript](https://github.com/anthropics/claude-agent-sdk-typescript) | Anthropic's TypeScript SDK |
| MCP SDK | [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | Model Context Protocol SDK |
| Microsoft Agents JS | [Agents-for-js](https://github.com/microsoft/Agents-for-js) | Microsoft M365 Agent SDK for JS |
| OpenAI Agents JS | [openai-agents-js](https://github.com/openai/openai-agents-js) | Official OpenAI TypeScript framework |

### Rust (2 SDKs)
| SDK | Repository | Description |
|-----|------------|-------------|
| Anda | [anda](https://github.com/ldclabs/anda) | Rust AI agent framework with ICP/TEE support |
| rust-agentai | [rust-agentai](https://github.com/AdamStrojek/rust-agentai) | Rust library for creating AI agents |

## Prerequisites

- **Python 3.6 or higher** (for running the installer)
- **Git** (for cloning repositories)

### Language-Specific Requirements

**For Python SDKs:**
- pip (Python package installer)
- uv (for Arcade AI installation)

**For TypeScript/JavaScript SDKs:**
- Node.js and npm

**For Rust SDKs:**
- Rust toolchain (rustc and cargo)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Agent-SDK-Env-Setup
```

2. Make the script executable:
```bash
chmod +x setup_agent_sdks.py
```

## Usage

Run the interactive setup script:

```bash
python3 setup_agent_sdks.py
```

### Step-by-Step Process

1. **Directory Selection**: Choose between the default directory (`~/agents/sdks`) or specify a custom path
2. **Language Selection**: Choose which programming languages you want to work with:
   - Python (13 SDKs)
   - TypeScript/JavaScript (6 SDKs)
   - Rust (2 SDKs)
   - All languages selected by default
3. **SDK Selection**: Use the interactive menu to select which SDKs to install:
   - SDKs are displayed with language tags for easy identification
   - Enter numbers to toggle selection
   - Use 'a' to select all SDKs
   - Use 'n' to deselect all SDKs
   - Enter 'done' to proceed with installation
4. **Installation Confirmation**: Review your selections and confirm installation
5. **Automated Installation**: The script will clone repositories and run installation commands for each selected SDK

### Example Session

```
============================================================
           Agent SDK Setup Tool
============================================================
Interactive installer for various agent development kits

Installation Directory Setup
Default directory: ~/agents/sdks

Use default directory? (y/n): y
✓ Created directory: /home/user/agents/sdks

Select Programming Languages
Choose which languages you want to see SDKs for

1. [*] Python (13 SDKs)
2. [*] TypeScript/JavaScript (6 SDKs)
3. [ ] Rust (2 SDKs)

Commands: (1-3) to toggle, 'a'=all, 'n'=none, 'done'=continue
Your choice: done

Select Agent SDKs to Install
Enter numbers to toggle selection with asterisk [*] markers

 1. [ ] ADK TypeScript [TypeScript/JavaScript]
 2. [*] AgentKit [TypeScript/JavaScript]
 3. [ ] Arcade AI [Python]
 4. [*] AutoGen [Python]
 5. [*] Claude Agent SDK [Python]
 6. [ ] CrewAI [Python]
 7. [*] Google ADK [Python]
 8. [ ] LangChain [Python]
 9. [ ] LangGraph [Python]
...

Selected (4): AgentKit, AutoGen, Claude Agent SDK, Google ADK

Commands: (1-19) to toggle, 'a'=all, 'n'=none, 'done'=install
Your choice: done

Installation Summary
Installation directory: /home/user/agents/sdks
SDKs to install (4): AgentKit, AutoGen, Claude Agent SDK, Google ADK

Proceed with installation? (y/n): y
```

## Default Installation Directory

The script uses `~/agents/sdks` as the default installation directory. This directory will be created automatically if it doesn't exist.

## Error Handling

The script includes comprehensive error handling for:
- Directory creation failures
- Git clone failures
- Package installation failures
- Invalid user input
- Missing dependencies

## Troubleshooting

### Common Issues

1. **Git not found**: Ensure Git is installed and available in your PATH
2. **Permission errors**: Make sure you have write permissions to the installation directory
3. **Package installation failures**: Check that pip and other required tools are properly installed
4. **Network issues**: Ensure you have internet connectivity for cloning repositories

### Getting Help

If you encounter issues:
1. Check the error messages for specific details
2. Ensure all prerequisites are installed
3. Verify network connectivity
4. Check file permissions in the installation directory

## Contributing

To add new SDKs to the installer:

1. Edit the `sdks.json` configuration file
2. Add the new SDK under the appropriate language section:
```json
{
  "languages": {
    "python": {
      "name": "Python",
      "sdks": {
        "Your SDK Name": {
          "repo": "https://github.com/owner/repo",
          "install_commands": ["pip install package-name"],
          "description": "Brief description of the SDK"
        }
      }
    }
  }
}
```

3. Update the `metadata.total_sdks` count in `sdks.json`
4. The script will automatically incorporate your changes on the next run
