# Catalog Image Downloader

This Python script is designed to download images from a specific API for various catalogs and save them to your local directory. Each catalog is identified by a unique URL, and this script automates the process of fetching and storing the images.

## Prerequisites

Before using this script, make sure you have the following prerequisites in place:

- ***Python***: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

- ***Required Libraries***: Install the necessary Python libraries by running the following command:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script by executing the following command:
    ```bash
    python main.py
    ```

4. The script will download the images from the specified catalogs and organize them into folders by catalog name and date in the "Downloads" directory.

5. You can monitor the progress as the script prints messages for each image downloaded.

## Customization

- You can customize the `download_dir` variable to specify a different download directory.

- The script assumes that the image URLs are available in the specified format. If the API or data source changes, you may need to adapt the script accordingly.

- Handle exceptions and errors as needed for your specific use case to ensure robust operation in a production environment.