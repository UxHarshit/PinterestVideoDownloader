# Pinterest Video Downloader

This is a simple Python script developed by Harshit to download videos from Pinterest.

The script makes use of popular Python libraries including requests, BeautifulSoup, tqdm, re, and datetime. It downloads video content from Pinterest by parsing the HTML content and identifying the source of the video. 

## Dependencies

To run this script, you'll need the following Python libraries:
- requests
- BeautifulSoup
- tqdm
- re
- datetime

You can install these libraries using pip:
```shell
pip install requests beautifulsoup4 tqdm
```
**Note**: re and datetime are both standard libraries in Python, so you don't need to install them.

## How to use

To use this script:
1. Make sure you have all dependencies installed.
2. Run the script using python command in terminal:
    ```shell
    python main.py
    ```
3. Enter the Pinterest page URL when prompted.

The script will validate the URL and extract the video source. It will then download the video as an MP4 file, with the current date and time as part of the filename.

## Limitations

This script is designed to work with Pinterest's specific HTML structure as of the time of its creation. If Pinterest changes their website structure, the script may not work as expected.

Additionally, the script currently only supports direct Pinterest URLs or "pin.it" short URLs. Other URL structures may not work.

## License

This script is provided as-is under the MIT license. Feel free to modify and distribute, but please maintain original attribution to the creator.