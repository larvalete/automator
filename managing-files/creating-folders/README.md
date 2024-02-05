# Automator

Automator is a versatile script designed to automate the creation of versioned directories based on semantic versioning. This tool proves invaluable for managing project versions and ensuring a structured and organized file architecture across projects.

## Features

- **Versioned Directory Creation**: Generate directories named after version numbers (major, minor, patch) and optional labels.
- **Custom Version Incrementing**: Offers flexibility in versioning by supporting user-defined increments and labels.
- **Prefix Support**: Newly added functionality allows for the inclusion of a custom prefix to directory names, enhancing organizational clarity.
- **Workflow Integration**: Designed to seamlessly integrate into existing project workflows, facilitating automation and efficiency.

## Getting Started

Automator requires Python 3 to run. Ensure Python is installed on your system to utilize this script.

### Prerequisites

- Python 3.x

### Installing

To set up Automator on your local machine, follow these steps:

1. **Clone the repository**:
  ```bash
  git clone https://github.com/larvalete/automator.git
  ```

2. **Navigate to the Automator directory**:

  ```bash
  cd automator
  ```

### Usage

Automator is executed from the command line, requiring a base path for directory creation, a starting version, the number of directories to create, and an optional prefix. Here's how to use it:

**Creating Numeric Versioned Folders**:

  ```bash
  python3 create-folders.py /path/to/base/directory ver-1-0-0 10
  ```
This command creates 10 directories, starting from ver-1-0-0.


**Creating Folders with Alpha Versions**:

```bash
python3 create-folders.py /path/to/base/directory ver-1-0-0_alpha-0 5
```
Generates 5 directories beginning with ver-1-0-0_alpha-0, incrementing the alpha label with each subsequent directory.

**Including a Custom Prefix**:

```bash
python3 create-folders.py /path/to/base/directory pos-abs ver-1-0-0 3
```
Prepends pos-abs_ to the versioned directory names, starting with ver-1-0-0 and creating a total of 3 directories.

Ensure to replace /path/to/base/directory with your target directory path and adjust the version numbers and count as needed.

### License
This project is licensed under the MIT License - see the LICENSE file in the repository for details.
