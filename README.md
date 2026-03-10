# Test Data Generator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white)

### Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [TODO](#todo)

# Overview

Test Data Generator is a simple tool designed to generate realistic test data for your applications. Built on top of [Faker](https://pypi.org/project/Faker/), a popular library for generating fake data and [Tkinter ](https://docs.python.org/3/library/tkinter.html) for simple UI. Whether you're testing data handling, user interfaces, or database performance, this tool helps streamline your testing process by providing diverse, locale-specific data.

## Features:

- **Random Name Generation**: Generate realistic names for different regions and languages.
- **Phone Number Generation**: Generate phone numbers suitable for different regions.
- **Email Address Generation**: Generate email addresses for different regions.
- **Bulk Generation**: Generate up to 100,000 records in bulk.
- **Export Options**: Copy to clipboard, Save to JSON, Save to CSV.

## Project Structure

```
test-data-generator/
  src/
    main.py              # Entry point
    app.py               # Application setup
    data_generator.py    # Data generation logic
    gui/
      base_generator.py  # Base class for views
      main_menu.py       # Main screen of the app
      name_generator.py  # View for name generation
      phone_generator.py # View for phone number generation
  .gitignore             # Files and directories to ignore in version control
  LICENSE.txt            # Project License
  README.md              # Project overview and documentation
  requirements.txt       # Dependencies for the project
```

## Installation

### Option 1: Download Executable (Windows)

1. Download the latest release from [Releases](https://github.com/papachili/test-data-generator/releases)
2. Run `TestDataGenerator.exe`

### Option 2: Run from Source

```bash
# Clone repository
git clone https://github.com/papachili/test-data-generator.git
cd test-data-generator

# Install dependencies
pip install -r requirements.txt

# Run application
python src/main.py
```

## Contributing

Contributions are welcome! Please submit a pull request with your changes.

- Follow PEP8 style.
- Write clear, descriptive commit messages.

## License

Test Data Generator is open-sourced software licensed under the MIT License, which means you are free to use, modify, and distribute the project as you see fit.
See the [MIT License](https://github.com/papachili/test-data-generator/blob/main/LICENSE) file for details.

## TODO

- Support generation of other data types (e.g., addresses, passport, credit cards etc.)
- Control data format, quantity, and structure
