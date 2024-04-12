# Web Screenshot Tool

Web Screenshot Tool is a Python script that allows users to capture screenshots of websites using Selenium and Chrome WebDriver. It provides a simple command-line interface for users to enter the URL of the website they want to capture, and it saves the screenshots in a specified output folder.

## Features

- Capture screenshots of websites in headless mode.
- Support specifying the URL with or without "http://" or "https://".
- Save screenshots with a random filename to prevent overwriting existing files.
- Set viewport size to 1920x1080 for high-quality screenshots.
- Automatically create an output folder if it doesn't exist.
- Display informative messages, including the progress and status of the screenshot process.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/1ceB1ade/web-screenshot-tool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd web-screenshot-tool
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Python script `main.py`:

    ```bash
    python main.py
    ```

2. Enter the URL of the website you want to capture when prompted.

3. Press `Enter` to take the screenshot. The screenshot will be saved in the `output` folder with a random filename.

4. Choose whether to take another screenshot by entering `Y` or `N` when prompted.

## Example

[09:00:00] [+] Enter Site: example.com
[09:00:03] [+] Navigating to https://example.com
[09:00:05] [+] Taking Screenshot and saving as output/example_com_abc123.png
[09:00:10] [+] Closing Browser
[09:00:15] [+] Would you like to Screenshot Another Site (Y/N): Y
[09:00:20] [+] Enter Site: another-example.com
[09:00:25] [!] Website Not Found
[09:00:30] [+] Would you like to Screenshot Another Site (Y/N): N


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
