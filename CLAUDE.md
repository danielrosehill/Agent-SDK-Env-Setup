# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an interactive CLI tool designed to quickly set up various agent development kits (SDKs) on a system. The tool supports 21 different agent SDKs across three programming languages (Python, TypeScript/JavaScript, Rust) from various vendors including Google, Microsoft, OpenAI, Anthropic, IBM Watson, and others.

The architecture consists of:
- **setup_agent_sdks.py**: Main Python script (355 lines) - orchestrates the installation workflow
- **sdks.json**: JSON configuration file containing all SDK metadata organized by language

## Running the Application

Execute the script directly:

```bash
python3 setup_agent_sdks.py
```

Or with execute permissions:

```bash
./setup_agent_sdks.py
```

No external dependencies are required - the script uses only Python standard library modules.

## Architecture

### Configuration-Driven Design

The application uses a **JSON configuration file** (`sdks.json`) to define all SDKs, separating data from code. The main script loads this configuration at runtime.

**User Flow:**
1. User selects installation directory (default: `~/agents/sdks`)
2. User selects programming languages to filter SDKs (Python, TypeScript/JavaScript, Rust)
3. User selects specific SDKs from filtered list
4. User confirms installation
5. Script clones repositories and runs language-specific installation commands

### JSON Configuration Structure (`sdks.json`)

```json
{
  "languages": {
    "python": {
      "name": "Python",
      "sdks": {
        "SDK Name": {
          "repo": "https://github.com/...",
          "install_commands": ["pip install ..."],
          "description": "..."
        }
      }
    }
  },
  "metadata": {
    "version": "1.0.0",
    "total_sdks": 21
  }
}
```

**Key Design Benefits:**
- Easy to add new SDKs without modifying Python code
- Language-based organization allows filtering by technology stack
- Metadata tracking for version management
- Supports multiple languages/runtimes (Python, TypeScript/JavaScript, Rust)

### Core Components

**Configuration Management**
- `load_sdk_config()`: Loads and validates `sdks.json` configuration file at startup
- Handles JSON parsing errors and missing file errors gracefully

**User Interaction Functions**
- `get_installation_directory()`: Handles directory selection with validation
- `select_languages(config)`: NEW - Interactive language filter menu (Python, TypeScript/JavaScript, Rust)
- `display_sdk_menu(config, selected_languages)`: Interactive multi-select menu showing SDKs with language tags
- Uses ANSI color codes (via `Colors` class) for color-coded visual feedback

**Installation Logic**
- `clone_repository()`: Handles git cloning with duplicate detection and update prompts
- `run_command()`: Executes shell commands with support for both simple and complex shell operations (handles `&&` and `source` commands with `shell=True`)
- `install_sdk(sdk_name, sdk_data, base_dir, language)`: Orchestrates the full installation flow for a single SDK
  - Now accepts SDK data as a parameter instead of looking up in hardcoded dictionary
  - Language parameter used for display/logging purposes

### Command Execution Strategy

The script handles two types of commands differently:
- **Simple commands**: Split on whitespace and executed without shell
- **Complex commands** (containing `&&` or `source`): Executed with `shell=True` to support shell features

## SDK-Specific Installation Methods

Different SDKs use different installation approaches based on their language and requirements:

### Python SDKs
- **Standard pip**: Most Python SDKs (LangChain, CrewAI, AutoGen, etc.)
- **uv-based**: Arcade AI uses `uv sync --extra all --dev`
- **venv creation**: OpenAI Agents creates its own virtual environment
- **Clone-only**: Microsoft Agents (no installation commands)

### TypeScript/JavaScript SDKs
- All use `npm install` after cloning

### Rust SDKs
- All use `cargo build --release`

## Error Handling

The script includes comprehensive error handling for:
- **Configuration errors**: Missing or invalid `sdks.json` file (FileNotFoundError, JSONDecodeError)
- **Directory creation failures**: OSError when creating installation directory
- **Git clone failures**: subprocess errors during repository cloning
- **Command execution failures**: CalledProcessError during SDK installation
- **User interruption**: KeyboardInterrupt for graceful exit
- **Invalid user input**: Validation loops in all interactive menus

Failed installations are tracked separately and reported in the final summary, allowing the script to continue installing other SDKs even if one fails.

## User Experience Features

**Two-Stage Interactive Selection**
1. **Language Selection**: Filter SDKs by programming language (all selected by default)
   - Shows SDK count for each language
   - Toggle languages with number keys

2. **SDK Selection**: Choose specific SDKs from filtered list
   - SDKs displayed with colored language tags (e.g., `[Python]`, `[TypeScript/JavaScript]`)
   - Alphabetically sorted for easy scanning
   - Toggle individual SDKs by number
   - Select all with 'a' command
   - Deselect all with 'n' command
   - Real-time feedback showing selected items with `[*]` markers
   - Selection count and summary displayed

**Color-Coded Output**
- Success messages: Green with checkmark
- Errors: Red with X
- Warnings: Yellow with warning symbol
- Info: Blue with info symbol
- Headers and prompts: Bold with various colors

## Adding New SDKs

To add a new SDK, edit `sdks.json`:

1. Add the SDK under the appropriate language section:
```json
{
  "languages": {
    "python": {
      "sdks": {
        "New SDK Name": {
          "repo": "https://github.com/owner/repo",
          "install_commands": ["pip install package-name"],
          "description": "Brief description of the SDK"
        }
      }
    }
  }
}
```

2. Update `metadata.total_sdks` to reflect the new count

3. To add a new language category:
```json
{
  "languages": {
    "golang": {
      "name": "Go",
      "sdks": { ... }
    }
  }
}
```

The script automatically loads the updated configuration and incorporates new SDKs into the alphabetically sorted menu with appropriate language tags.

## Default Behavior

- Default installation directory: `~/agents/sdks`
- All languages selected by default in language filter
- Creates directory structure automatically
- Alphabetical ordering of SDKs in menu (across all selected languages)
- Prompts for update if repository already exists
- Loads configuration from `sdks.json` in script directory
- No external Python dependencies needed (uses only stdlib: os, sys, subprocess, json, pathlib, typing)

## Files in Repository

- **setup_agent_sdks.py**: Main executable script (355 lines)
- **sdks.json**: Configuration file with all SDK definitions organized by language
- **requirements.txt**: Documents that no external dependencies are needed
- **README.md**: User-facing documentation
- **CLAUDE.md**: This file - developer/AI guidance
