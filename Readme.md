# Git Operations Tool

This project is a utility designed to automate and streamline common Git operations through a script or command-line interface. It helps developers perform tasks like initializing a repository, committing changes, pushing to remote, pulling latest changes, and managing branches with minimal effort.


## 🚀Features
- Initialize a Git repository

- Add and commit changes

- Push to remote repositories

- Pull updates from remote

- Create, switch, and delete branches

- View Git status and log

## 🛠️Requirements
Make sure you have the following installed:

- Git

- Python 3.x _(if using the Python version)_

- Internet connection (for remote operations)

## 📦Installation
Clone the repository:

> bash

> git clone https://github.com/yourusername/git-operations-tool.git

>cd git-operations-tool

Install dependencies if applicable:

> bash

> pip install -r requirements.txt  # For Python projects

Make the script executable (Linux/macOS):

> bash

> chmod +x git_tool.py

## 💻Usage
Run the script and follow the prompts:

>bash
>python git_tool.py

Or pass arguments directly (if supported):

>bash
>python git_tool.py --init --remote https://github.com/user/repo.git

####Example operations:
Initialize repository:

>bash

>python git_tool.py --init

Commit and push changes:

>bash

>python git_tool.py --commit "Fixed issue" --push

Pull from remote:

>bash

>python git_tool.py --pull

## ⚙️Supported Git Commands
- git init

- git add .

- git commit -m "message"

- git push origin <branch>

- git pull origin <branch>

- git branch, git checkout, git merge, etc.
