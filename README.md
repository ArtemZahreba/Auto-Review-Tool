# Automated Code Review Tool

## Task Description

In this task, you are required to create a prototype of a backend version of an automated code review tool using Python. This tool will help automate the process of reviewing coding assignments by utilizing the OpenAI GPT API for code analysis and the GitHub API for accessing repositories.

The task is divided into two parts:

1. **Prototype (code)**: You will write code for a backend service that performs automated code reviews. It can be assumed that this service will be used with relatively small repositories, where the total size does not exceed the OpenAI token limits for a single request (see more at [OpenAI Limits](https://platform.openai.com/settings/organization/limits)).

2. **What if**: You will explain how to scale this solution to work with large repositories and/or large volumes of review requests.

## My Solution

This solution is not implemented in a web version due to time constraints. Instead, it is implemented in a console version. In this version, we prompt the user for a project description, a link to the repository, and the level of the specialist who was assigned the test task.

Main execution steps:
1. **Input Retrieval**: The tool asks the user for the project description, the GitHub repository URL, and the specialist's level (junior, middle, senior).
2. **Code Analysis**: Using the OpenAI API, the tool performs automated analysis of the code from the repository.
3. **Results Output**: The user receives feedback on the quality of the task execution.

### Installation Instructions

To install and run this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd <REPOSITORY_FOLDER_NAME>
   ```

2. **Install dependencies**:
   To run this project, you need to have Python 3.7 or higher. You also need to install the required libraries. Use `pip` to install them:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**:
   Before running the program, you will need to obtain API keys for OpenAI and configure them in the configuration file.

4. **Run the program**:
   To start the program, use the command:
   ```bash
   python main.py
   ```

5. **Interacting with the program**:
   Follow the on-screen instructions and enter the required information when prompted by the program.
