# VSCode Python Setup with Modular Structure and External Packages

This guide provides my approach to setting up a Python project in Visual Studio Code (VSCode) with a focus on modularity and efficient management of external packages. It covers project structure, environment configuration, debugging setup, and three methods for handling external dependencies: pip install from GitHub (recommended), Git submodules, and manual code inclusion. 


## Project Structure

The project follows a modular structure, with separate directories for internal (src/) and external (external/) packages. The modular approach improves organization and maintainability.

```bash
VscodePySetup/
├── .vscode/
│   ├── settings.json        # VSCode workspace settings
│   └── launch.json          # Debug configurations for the project
├── src/                     # Main source directory
│   └── main_package/        # Main package containing Python modules
│       ├── __init__.py      # Marks the directory as a Python package
│       ├── main.py          # Main execution file
│       └── helpers.py       # Helper functions for the main package
├── external/                # Directory for external packages
│   └── sample_package/      # Example external package
│       ├── __init__.py      # Marks the directory as a Python package
│       └── sample_module.py # Module within the external package
├── doc/
│   └── vscode_python_setup.md  # Documentation for the setup
├── .env                     # Environment variables for the project
├── .gitignore               # Files and directories to be ignored by Git
├── create_venv.bat          # Script to create a virtual environment
└── readmd.md                # Project README file
```

### Set up python path and run/debug configuration

- **Modular Structure**:The src/ directory holds the main project code (main_package).The external/ directory is where external packages can be placed if they are needed directly within the project.The project is structured to support modularity, with clearly defined boundaries between internal and external code.
## Environment Variables

The .env file defines environment variables that are essential for running the project, including the PYTHONPATH:

```bash
PYTHONPATH=./src:./external
```

This setup ensures that both the internal (src/) and external (external/) directories are included in Python's module search path.

## Debugging Configuration

The launch.json file defines how VSCode should run and debug the project.
For vscode, unlike pycharm, run and debug configurations can be the same.(best practice is still to use different configurations). Below is an example of the same configuration for run and debug in launch.json:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Run main.py",
            "type": "debugpy",
            "request": "launch",
            "module": "main_package.main",
            "cwd": "${workspaceFolder}",
            "console": "integratedTerminal",
            "args": ["--name", "John"],
            "envFile": "${workspaceFolder}/.env",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/src;${workspaceFolder}/external"
            }
        }
    ]
}
```

### Setup for setting.json and dependencies

- **Module Execution**: The module field specifies the main entry point for the application, allowing the project to be run as a module.
- **Environment Variables**: The envFile field ensures that environment variables from .env are loaded, and the env section further specifies PYTHONPATH.
## Workspace Settings

The settings.json file includes configurations to streamline Python development in VSCode:

```json
{
  "python.terminal.activateEnvironment": true,
  "python.envFile": "${workspaceFolder}/.env",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "charliermarsh.ruff",
  "editor.codeActionsOnSave": {
    "source.fixAll.ruff": "explicit",
    "source.organizeImports.ruff": "explicit"
  },
  "python.analysis.extraPaths": [
    "./external"
  ]
}
```

- **Environment Activation**: The virtual environment is automatically activated in the terminal.
- **Code Formatting**: Ruff is used as the default Python formatter, and formatting is applied on file save.
- **python.analysis.extraPaths**: Adds the external/ folder to the analysis path, ensuring that external packages are correctly recognized by IntelliSense and other VSCode analysis tools.
## Methods for Handling External Packages

There are three primary methods for including and managing external packages, especially when they come from GitHub repositories. **The recommended approach is using pip install from GitHub**, but alternatives like Git submodules or manually copying code into an external/ folder are also options, depending on your company's restrictions.

### Method 1: pip install from GitHub (Recommended)

If pip is available, this is the best and cleanest way to install and manage external dependencies:

```bash
pip install git+https://github.com/username/repo.git
```

#### Advantages:

- **Dependency Management**: pip handles dependencies, installing them into your virtual environment.
- **Versioning**: You can specify branches, tags, or commits, ensuring that you install the exact version you need:Install a specific branch:
```bash
pip install git+https://github.com/username/repo.git@branch-name
```
Install a specific commit:
```bash
pip install git+https://github.com/username/repo.git@
```
- **Ease of Use**: You can include this in your requirements.txt file for easy installation:
```text
git+https://github.com/username/repo.git@branch-name#egg=package_name
```
- **Automatic Updates**: Simply run pip install --upgrade git+https://github.com/username/repo.git to fetch the latest changes.
#### Conclusion:

Using pip install from GitHub is the best approach because it handles dependencies automatically, integrates well with virtual environments, and simplifies updates.

### Method 2: Git Submodules (Alternative)

If pip is unavailable in your environment, using Git submodules is a good alternative. A submodule allows you to include another Git repository in your project while keeping the version control histories separate.

#### How to Set Up:

1. Navigate to your project directory.
2. Add the submodule:
```bash
git submodule add https://github.com/username/repo external/repo
```
3. Commit the changes.
#### Advantages:

- **Version Control**: The external package remains under its own version control, making it easy to pull updates or rollback changes.
- **Separation**: It maintains a clear boundary between your code and external dependencies.
#### Disadvantages:

- **Complexity**: Working with submodules requires extra steps, especially when cloning the repository:
```bash
git clone --recurse-submodules 
```
- **Dependency Handling**: Submodules do not handle additional dependencies, meaning you may need to manually install other required packages.
### Method 3: Copying Code into the external/ Folder (Simple but Not Ideal)

This is the most straightforward option but has several drawbacks. You simply copy the code from the GitHub repository into the external/ folder in your project.

#### How to Do It:

1. Download the code from GitHub.
2. Copy it into the external/ folder of your project.
#### Advantages:

- **Simplicity**: No additional tools or commands are required, and the code is immediately available.
- **Offline Availability**: Once the code is copied, you are not reliant on external repositories or the internet.
#### Disadvantages:

- **Manual Updates**: You will have to manually update the code whenever the original repository changes.
- **Versioning Issues**: It's harder to track the exact version of the external code you're using, leading to potential inconsistencies.
- **No Dependency Management**: Any dependencies of the external code need to be installed manually.
#### Conclusion:

Copying code is simple, but it’s not scalable and makes updating more difficult. This method is best suited for small, stable libraries that don’t require frequent updates.

## Summary of Methods

| **Method** | **Use Case** | **Pros** | **Cons** |
| ---- | ---- | ---- | ---- |
| **pip install from GitHub** | Recommended if pip is available | Clean dependency management, automatic updates, version control | Requires pip; must be online to install |
| **Git Submodules** | For environments without pip, or where frequent updates are needed | Version control, easy to pull updates, keeps external code separate | Slightly more complex, requires Git knowledge |
| **Copy Code into external/** | Best for stable libraries that rarely change | Simple, no external tools needed | No versioning, manual updates, harder to track changes |

### Conclusion:

If pip is available, always use pip install git+https://github.com/username/repo.git as the best method. It simplifies dependency management, versioning, and updates. If pip is not an option, Git submodules offer better control than copying code manually. However, copying the code is viable for simple, rarely updated packages.

This guide provides a flexible and modular setup, supporting external packages while giving you the best practices for managing dependencies.