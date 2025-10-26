#!/usr/bin/env python3
"""
Agent SDK Setup Script
Interactive CLI tool to install various agent SDKs on your system.
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Tuple, Set

# ANSI color codes for better CLI experience
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

DEFAULT_BASE_DIR = os.path.expanduser("~/agents/sdks")
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "sdks.json")

def load_sdk_config() -> Dict:
    """Load SDK configuration from JSON file."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print_error(f"Configuration file not found: {CONFIG_FILE}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON in configuration file: {e}")
        sys.exit(1)

def print_header():
    """Print the application header."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}")
    print("           Agent SDK Setup Tool")
    print(f"{'='*60}{Colors.ENDC}")
    print(f"{Colors.OKCYAN}Interactive installer for various agent development kits{Colors.ENDC}\n")

def print_success(message: str):
    """Print success message."""
    print(f"{Colors.OKGREEN}✓ {message}{Colors.ENDC}")

def print_error(message: str):
    """Print error message."""
    print(f"{Colors.FAIL}✗ {message}{Colors.ENDC}")

def print_warning(message: str):
    """Print warning message."""
    print(f"{Colors.WARNING}⚠ {message}{Colors.ENDC}")

def print_info(message: str):
    """Print info message."""
    print(f"{Colors.OKBLUE}ℹ {message}{Colors.ENDC}")

def get_installation_directory() -> str:
    """Get the installation directory from user input."""
    print(f"\n{Colors.BOLD}Installation Directory Setup{Colors.ENDC}")
    print(f"Default directory: {Colors.OKCYAN}{DEFAULT_BASE_DIR}{Colors.ENDC}")
    
    while True:
        choice = input(f"\nUse default directory? (y/n): ").lower().strip()
        
        if choice == 'y':
            base_dir = DEFAULT_BASE_DIR
            break
        elif choice == 'n':
            base_dir = input("Enter custom directory path: ").strip()
            if not base_dir:
                print_error("Directory path cannot be empty!")
                continue
            base_dir = os.path.expanduser(base_dir)
            break
        else:
            print_error("Please enter 'y' for yes or 'n' for no")
    
    # Create directory if it doesn't exist
    if not os.path.exists(base_dir):
        try:
            os.makedirs(base_dir, exist_ok=True)
            print_success(f"Created directory: {base_dir}")
        except OSError as e:
            print_error(f"Failed to create directory: {e}")
            sys.exit(1)
    else:
        print_info(f"Using existing directory: {base_dir}")
    
    return base_dir

def select_languages(config: Dict) -> Set[str]:
    """Display language selection menu and return selected languages."""
    languages = list(config['languages'].keys())
    selected = set(languages)  # All selected by default

    print(f"\n{Colors.BOLD}Select Programming Languages{Colors.ENDC}")
    print("Choose which languages you want to see SDKs for\n")

    while True:
        # Show current selection state
        for i, lang_key in enumerate(languages, 1):
            lang_name = config['languages'][lang_key]['name']
            sdk_count = len(config['languages'][lang_key]['sdks'])
            marker = f"{Colors.OKGREEN}[*]{Colors.ENDC}" if lang_key in selected else "[ ]"
            print(f"{i}. {marker} {Colors.BOLD}{lang_name}{Colors.ENDC} ({sdk_count} SDKs)")

        # Show selection summary
        if selected:
            selected_names = [config['languages'][k]['name'] for k in selected]
            print(f"\n{Colors.WARNING}Selected: {Colors.OKGREEN}{', '.join(selected_names)}{Colors.ENDC}")
        else:
            print(f"\n{Colors.WARNING}No languages selected{Colors.ENDC}")

        print(f"\n{Colors.BOLD}Commands:{Colors.ENDC} (1-{len(languages)}) to toggle, 'a'=all, 'n'=none, 'done'=continue")
        choice = input(f"{Colors.BOLD}Your choice: {Colors.ENDC}").strip().lower()

        # Process choice
        if choice == 'done':
            if not selected:
                print_warning("No languages selected! Please select at least one.")
                print()
                continue
            break
        elif choice == 'a':
            selected = set(languages)
            print_success("All languages selected")
        elif choice == 'n':
            selected.clear()
            print_success("All selections cleared")
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(languages):
                lang_key = languages[index]
                if lang_key in selected:
                    selected.remove(lang_key)
                    print_success(f"Deselected: {config['languages'][lang_key]['name']}")
                else:
                    selected.add(lang_key)
                    print_success(f"Selected: {config['languages'][lang_key]['name']}")
            else:
                print_error("Invalid selection number")
        else:
            print_error("Invalid choice")

        # Add separator and redisplay
        print("\n" + "="*50)

    return selected

def display_sdk_menu(config: Dict, selected_languages: Set[str]) -> List[Tuple[str, str]]:
    """Display SDK selection menu and return selected SDKs with their languages."""
    # Build list of SDKs from selected languages
    sdk_list = []
    for lang_key in selected_languages:
        lang_name = config['languages'][lang_key]['name']
        for sdk_name, sdk_data in config['languages'][lang_key]['sdks'].items():
            sdk_list.append({
                'name': sdk_name,
                'language': lang_key,
                'lang_display': lang_name,
                'data': sdk_data
            })

    # Sort by SDK name
    sdk_list.sort(key=lambda x: x['name'])
    selected = set()

    print(f"\n{Colors.BOLD}Select Agent SDKs to Install{Colors.ENDC}")
    print("Enter numbers to toggle selection with asterisk [*] markers\n")

    while True:
        # Show current selection state
        for i, sdk_info in enumerate(sdk_list, 1):
            marker = f"{Colors.OKGREEN}[*]{Colors.ENDC}" if i-1 in selected else "[ ]"
            lang_tag = f"{Colors.OKCYAN}[{sdk_info['lang_display']}]{Colors.ENDC}"
            print(f"{i:2d}. {marker} {Colors.BOLD}{sdk_info['name']}{Colors.ENDC} {lang_tag}")

        # Show selection summary
        if selected:
            selected_names = [sdk_list[i]['name'] for i in selected]
            print(f"\n{Colors.WARNING}Selected ({len(selected)}): {Colors.OKGREEN}{', '.join(selected_names)}{Colors.ENDC}")
        else:
            print(f"\n{Colors.WARNING}No SDKs selected{Colors.ENDC}")

        print(f"\n{Colors.BOLD}Commands:{Colors.ENDC} (1-{len(sdk_list)}) to toggle, 'a'=all, 'n'=none, 'done'=install")
        choice = input(f"{Colors.BOLD}Your choice: {Colors.ENDC}").strip().lower()

        # Process choice and show immediate feedback
        if choice == 'done':
            if not selected:
                print_warning("No SDKs selected! Please select at least one SDK.")
                print()
                continue
            break
        elif choice == 'a':
            selected = set(range(len(sdk_list)))
            print_success("All SDKs selected")
        elif choice == 'n':
            selected.clear()
            print_success("All selections cleared")
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(sdk_list):
                if index in selected:
                    selected.remove(index)
                    print_success(f"Deselected: {sdk_list[index]['name']}")
                else:
                    selected.add(index)
                    print_success(f"Selected: {sdk_list[index]['name']}")
            else:
                print_error("Invalid selection number")
        else:
            print_error("Invalid choice")

        # Add separator and redisplay
        print("\n" + "="*50)

    # Return list of (sdk_name, language, sdk_data) tuples
    return [(sdk_list[i]['name'], sdk_list[i]['language'], sdk_list[i]['data']) for i in selected]

def run_command(command: str, cwd: str = None) -> bool:
    """Run a shell command and return success status."""
    try:
        print_info(f"Running: {command}")
        
        # Handle shell commands that need shell=True
        if "&&" in command or "source" in command:
            result = subprocess.run(command, shell=True, cwd=cwd, check=True)
        else:
            result = subprocess.run(command.split(), cwd=cwd, check=True)
        
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print_error(f"Command failed: {e}")
        return False
    except Exception as e:
        print_error(f"Error running command: {e}")
        return False

def clone_repository(repo_url: str, target_dir: str) -> bool:
    """Clone a git repository."""
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    clone_path = os.path.join(target_dir, repo_name)
    
    if os.path.exists(clone_path):
        print_warning(f"Repository already exists: {clone_path}")
        choice = input("Update existing repository? (y/n): ").lower().strip()
        if choice == 'y':
            return run_command("git pull", cwd=clone_path)
        else:
            return True
    
    return run_command(f"git clone {repo_url}", cwd=target_dir)

def install_sdk(sdk_name: str, sdk_data: Dict, base_dir: str, language: str) -> bool:
    """Install a specific SDK."""
    print(f"\n{Colors.BOLD}Installing {sdk_name} ({language})...{Colors.ENDC}")

    repo_url = sdk_data["repo"]
    install_commands = sdk_data["install_commands"]

    # Clone repository
    print_info(f"Cloning repository: {repo_url}")
    if not clone_repository(repo_url, base_dir):
        print_error(f"Failed to clone {sdk_name}")
        return False

    print_success(f"Successfully cloned {sdk_name}")

    # Run installation commands
    if install_commands:
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        repo_path = os.path.join(base_dir, repo_name)

        for command in install_commands:
            if not run_command(command, cwd=repo_path):
                print_error(f"Failed to install {sdk_name}")
                return False

        print_success(f"Successfully installed {sdk_name}")
    else:
        print_info(f"{sdk_name} cloned successfully (no additional installation required)")

    return True

def main():
    """Main application entry point."""
    try:
        print_header()

        # Load configuration
        config = load_sdk_config()

        # Get installation directory
        base_dir = get_installation_directory()

        # Select languages
        selected_languages = select_languages(config)

        # Select SDKs to install
        selected_sdks = display_sdk_menu(config, selected_languages)

        if not selected_sdks:
            print_warning("No SDKs selected. Exiting.")
            return

        # Confirm installation
        print(f"\n{Colors.BOLD}Installation Summary{Colors.ENDC}")
        print(f"Installation directory: {Colors.OKCYAN}{base_dir}{Colors.ENDC}")
        sdk_names = [sdk[0] for sdk in selected_sdks]
        print(f"SDKs to install ({len(sdk_names)}): {Colors.OKCYAN}{', '.join(sdk_names)}{Colors.ENDC}")

        confirm = input(f"\nProceed with installation? (y/n): ").lower().strip()
        if confirm != 'y':
            print("Installation cancelled.")
            return

        # Install selected SDKs
        print(f"\n{Colors.BOLD}Starting Installation...{Colors.ENDC}")
        successful_installs = []
        failed_installs = []

        for sdk_name, language, sdk_data in selected_sdks:
            if install_sdk(sdk_name, sdk_data, base_dir, language):
                successful_installs.append(sdk_name)
            else:
                failed_installs.append(sdk_name)

        # Installation summary
        print(f"\n{Colors.BOLD}Installation Complete!{Colors.ENDC}")

        if successful_installs:
            print_success(f"Successfully installed ({len(successful_installs)}): {', '.join(successful_installs)}")

        if failed_installs:
            print_error(f"Failed to install ({len(failed_installs)}): {', '.join(failed_installs)}")

        print(f"\nInstallation directory: {Colors.OKCYAN}{base_dir}{Colors.ENDC}")

    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Installation cancelled by user.{Colors.ENDC}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
