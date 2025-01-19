#!/usr/bin/env python3
import os
import sys
import subprocess
import platform

def print_step(message):
    print(f"\n{'='*50}")
    print(f"🚀 {message}")
    print(f"{'='*50}\n")

def run_command(command, error_message):
    try:
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        if process.returncode != 0:
            print(f"❌ Error: {error_message}")
            print(f"Details: {process.stderr}")
            return False
        print(process.stdout)  # Print stdout for debugging
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {error_message}")
        print(f"Details: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

def setup_macos_dependencies():
    print_step("Setting up macOS dependencies...")
    
    # Install SDL dependencies via brew
    dependencies = [
        "sdl2",
        "sdl2_image",
        "sdl2_mixer",
        "sdl2_ttf",
        "portmidi"
    ]
    
    for dep in dependencies:
        print(f"Installing {dep}...")
        if not run_command(f"brew install {dep}", f"Failed to install {dep}"):
            print(f"Warning: Failed to install {dep}, continuing anyway...")

def main():
    print_step("Welcome to Asteroids Game Setup!")
    
    # Detect OS
    system = platform.system().lower()
    print(f"📌 Detected OS: {system}")

    # Install system dependencies for macOS
    if system == "darwin":
        setup_macos_dependencies()

    # Create virtual environment
    venv_name = "venv"
    print_step("Creating virtual environment...")
    if not run_command(f"python3 -m venv {venv_name}", "Failed to create virtual environment"):
        return

    # Set up commands based on OS
    if system == "windows":
        python_cmd = f"{venv_name}\\Scripts\\python"
        pip_cmd = f"{venv_name}\\Scripts\\pip"
    else:
        python_cmd = f"{venv_name}/bin/python3"
        pip_cmd = f"{venv_name}/bin/pip3"

    # Upgrade pip
    print_step("Upgrading pip...")
    if not run_command(f"{python_cmd} -m pip install --upgrade pip", "Failed to upgrade pip"):
        return

    # Install requirements one by one
    print_step("Installing requirements...")
    with open("requirements.txt", "r") as f:
        requirements = f.readlines()
    
    for req in requirements:
        req = req.strip()
        if req:
            print(f"Installing {req}...")
            if not run_command(f"{pip_cmd} install {req}", f"Failed to install {req}"):
                if "pygame" in req:
                    print("Trying alternative pygame installation...")
                    if not run_command(f"{pip_cmd} install pygame --pre", "Failed to install pygame with --pre flag"):
                        return
                else:
                    return

    # Launch the game
    print_step("🎮 Starting the game...")
    if not run_command(f"{python_cmd} main.py", "Failed to start the game"):
        return

    print("\n✨ Setup completed successfully! Enjoy the game! ✨")

if __name__ == "__main__":
    main() 