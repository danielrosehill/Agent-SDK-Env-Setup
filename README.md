# Agent SDK Environment Setup

Interactive CLI tool to quickly set up various agent development kits (SDKs) on your system.

## Features

- **Interactive CLI Interface**: User-friendly menu system with color-coded output
- **Multi-SDK Support**: Install multiple agent SDKs in a single session
- **Flexible Directory Management**: Choose default or custom installation paths
- **Alphabetical SDK Listing**: Clean, organized display of available SDKs
- **Error Handling**: Robust error handling and validation
- **Progress Tracking**: Real-time installation progress and status updates

## Supported Agent SDKs

| SDK | Repository | Description |
|-----|------------|-------------|
| Arcade AI | [arcade-ai](https://github.com/ArcadeAI/arcade-ai) | Arcade AI agent development kit |
| Google ADK | [adk-python](https://github.com/google/adk-python) | Google Agent Development Kit |
| IBM Watson | [ibm-watsonx-orchestrate-adk](https://github.com/IBM/ibm-watsonx-orchestrate-adk) | IBM Watson Orchestrate Agent Development Kit |
| Microsoft Agents | [Agents](https://github.com/microsoft/Agents) | Microsoft Agent Framework |
| Nerve | [nerve](https://github.com/evilsocket/nerve) | Nerve agent development kit |
| OpenAI Agents | [openai-agents-python](https://github.com/openai/openai-agents-python) | OpenAI Agents Python SDK |
| Qwen Agent | [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | Qwen Agent Framework |

## Prerequisites

- Python 3.6 or higher
- Git (for cloning repositories)
- pip (Python package installer)
- uv (for Arcade AI installation)

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
2. **SDK Selection**: Use the interactive menu to select which SDKs to install:
   - Enter numbers to toggle selection
   - Use 'a' to select all SDKs
   - Use 'n' to deselect all SDKs
   - Enter 'done' to proceed with installation
3. **Installation Confirmation**: Review your selections and confirm installation
4. **Automated Installation**: The script will clone repositories and run installation commands for each selected SDK

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

Select Agent SDKs to Install
Use ↑/↓ to navigate, Space to select/deselect, Enter to confirm

SDK Selection Menu
1. [ ] Arcade AI
2. [*] Google ADK
3. [ ] IBM Watson
4. [*] Microsoft Agents
5. [ ] Nerve
6. [*] OpenAI Agents
7. [ ] Qwen Agent

Commands:
  Enter number to toggle selection
  'a' to select all
  'n' to select none
  'done' to proceed with installation

Your choice: done

Installation Summary
Installation directory: /home/user/agents/sdks
SDKs to install: Google ADK, Microsoft Agents, OpenAI Agents

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

1. Edit the `SDKS` dictionary in `setup_agent_sdks.py`
2. Add the new SDK with the following structure:
```python
"SDK Name": {
    "repo": "https://github.com/owner/repo",
    "install_commands": ["pip install package-name"],
    "description": "Brief description of the SDK"
}
```
