# Automator

Automator is a script that automates the creation of versioned directories based on semantic versioning. This tool is particularly useful for managing project versions and maintaining an organized file structure.


## Features

- Create directories with version names (major, minor, patch, and labels).
- Support for custom version incrementing based on user input.
- Easy to integrate into existing workflows.


## Getting Started

To use Automator, you need to have Python installed on your system. The script is compatible with Python 3.


### Prerequisites

- Python 3.x


### Installing

A step-by-step series of examples that tell you how to get a development environment running:

Clone the repository to your local machine:

```sh
git clone https://github.com/larvalete/automator.git
cd automator
```

### Usage

Run the script with Python, providing the base path for directory creation, the starting version, and the number of directories to create. You can include an optional label after the version number.


#### Create Folders With Numeric Versions:

```sh
python3 create-folders-0-2-0.py /path/to/base/directory ver-1-0-0 10
```

This command will create 10 versioned directories starting from `ver-1-0-0`.


#### Create Folders With Alpha Versions:

```sh
python3 create-folders-0-2-0.py /path/to/base/directory ver-1-0-0_alpha-0 5
```

This command will create 5 versioned directories starting from `ver-1-0-0_alpha-0` and increment the alpha label for each subsequent directory.

Make sure to replace `/path/to/base/directory` with the actual path where you want the directories to be created, and adjust the version numbers and count as needed.



## License

This project is licensed under the MIT License - see the LICENSE file in the repository for details.

