# Python Script Code Improve

## Overview

The **Python Script Code Improver** is a tool designed to enhance Python code by adding best practices such as:
- Comments and logging
- Try-exception clauses for error handling
- Refactoring of redundant code into functions
- Ensuring compliance with PEP8 standards by using tools like `black` or `flake8`

Additionally, the tool provides an option for users to input suggestions for further improvements or next steps, enabling more personalized code enhancements.

This application is built using:
- LangChain for natural language processing
- OpenAI's GPT-4 API for generating code improvements
- Streamlit for an interactive user interface

## Features

1. **Standard Code Improvement**: Automatically enhances the Python script by applying best practices.
2. **Advanced Improvement (User Suggestions)**: Allows users to input suggestions or additional improvements to further enhance the code.
3. **Code Comparison**: Displays the original code side by side with the improved code.
4. **Download Improved Code**: Users can download the improved script directly from the web interface.
5. **Automatic `requirements.txt` Generation**: Extracts imported libraries from the code and generates a `requirements.txt` file with the correct versions of the libraries.

## Installation

### Requirements

- Python 3.7+
- Install the required packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables

The tool uses the OpenAI API for generating improvements. Ensure you have your OpenAI API key set up:

1. Create a `.env` file in the root directory of the project.
2. Add the following environment variables:

   ```bash
   OPENAI_API_KEY=<your_openai_api_key>
   ```

### Additional Dependencies
Make sure you have `black` and `flake8` installed for code formatting:
```bash
pip install black flake8
```

## How to Use

1. **Run the Application**
   To run the Streamlit app locally:
   ```bash
   streamlit run app.py
   ```

2. **Upload Python Script**
   - Upload your Python script (.py) using the interface.
   - Choose between **Standard Improvements** or **Improve with Suggestions**.
   - Optionally, provide additional improvement suggestions in the text box.

3. **View & Download**
   - The app will display the original code on the left and the improved code on the right.
   - You can download the improved script by clicking the download button.

4. **Generate `requirements.txt`**
   - The tool automatically detects imported libraries from your Python scripts and generates a `requirements.txt` file.

## Example Usage

After running the app, the interface looks like this:

1. **Upload a Python file**: Select a `.py` file from your system.
2. **Standard or Custom Improvements**: Choose whether you want to apply standard improvements or provide additional suggestions.
3. **Improved Code**: View the improved Python code side by side with the original.
4. **Download**: Download the improved Python script with a single click.

## Code Structure

- `app.py`: The main Streamlit app file.
- `code_improve_class.py`: Contains the logic for improving Python scripts using the OpenAI API and handling user suggestions.
- `.env`: (Not included in the repository) Should contain your OpenAI API key.
- `requirements.txt`: Automatically generated file listing the necessary dependencies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you encounter any issues, feel free to open an issue or submit a pull request. When contributing, please ensure your code follows PEP8 standards.
