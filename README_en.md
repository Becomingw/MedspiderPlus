# MedSpiderPlus <img src="https://image-1307946721.cos.ap-shanghai.myqcloud.com/logo.png" alt="logo" width=39;/>


## Table of Contents

- [MedSpiderPlus ](#medspiderplus-)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
    - [Standard Method](#standard-method)
    - [Simplified Method](#simplified-method)
  - [Usage](#usage)
  - [Features](#features)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction
简体中文[./README.md] | English

if this project is helpful to you, please give me a star🤗.

MedSpiderPlus, akin to [Medspider](https://github.com/Becomingw/Med-Spider), is a Python-based GUI tool designed to enhance literature retrieval from the PubMed database. This project leverages the advanced capabilities of various AI models like GPT3.5Turbo, GPT4, GeminPro, ChatGLM4, and other custom models supported by OpenAI, to generate relevant search keywords for literature research. The application provides an intuitive and more aesthetically pleasing interface developed using PyQt5 and the qt_material package, aimed at streamlining the literature search and retrieval process.

## Installation

### Standard Method

Ensure Python version 3.10 or higher is installed.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Becomingw/MedSpiderPlus.git
   cd MedspiderPlus
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt # Use the -i option for alternative indexes like Tsinghua
   ```

3. **Run the application:**

   ```bash
   python main.py
   ```

### Simplified Method

Download the `Medspider+.7z` file from the releases section, extract it, and double-click `run.vbs` to start the application.

## Usage

Follow the sequence of actions for optimal operation:

1. Enter the research topic.
2. Configure search and AI model settings.
3. Set up network proxies.
4. Initiate the search.
5. Download the literature only if search results are present and confirmed by the presence of `Medspider+.xlsx`.
6. GreatAPI https://api.surger.xyz


**Notes:**

- English keywords or regular expressions should be used if not utilizing AI assistance.
- Avoid downloading without search results to prevent errors.
- Files produced are overwritten; save important data separately.
- Use of the random proxy feature may lead to network errors; a direct connection is advisable for small downloads.
- Large-scale downloads are not recommended as the tool functions as a web crawler.

## Features

- **Advanced AI Integration:** Supports multiple AI models for enhanced keyword generation.
- **Improved User Interface:** Built with PyQt5 and styled with qt_material.
- **Enhanced Performance:** Utilizes multi-threading for smoother operation.
- **Security Features:** Includes random and customizable proxy support.
- **Direct Insight:** Direct observation of program operation and settings through logs and previews.
- **Extended Accessibility:** Future updates to include direct downloads from publishers.

## Contributing

Contributions are welcome. If you have improvements or suggestions, feel free to fork the repository and submit a pull request.

## License

Specify the license under which the project is released.