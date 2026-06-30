# Pinterest Video Downloader

This is a simple Python script developed by Harshit to download videos from Pinterest.

The script uses popular Python libraries including `requests`, `BeautifulSoup`, `tqdm`, `re`, and `datetime`.

It downloads Pinterest videos by extracting the video source URL from the page content and converting the HLS stream (`.m3u8`) into an MP4 download link.

## Dependencies

To run this script, you'll need the following Python libraries:

- requests
- beautifulsoup4
- tqdm

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4 tqdm
```

Note:
`re` and `datetime` are standard Python libraries and do not need to be installed separately.

## How to use

1. Install the required dependencies.

2. Run the script:

```bash
python main.py
```

3. Enter the Pinterest video URL when prompted.

The script supports:

* Direct Pinterest pin URLs
* `pin.it` short URLs

After extracting the video source, the script downloads the video as an MP4 file.

The filename is generated using the current date and time.

Example:

```
16_06_23_40_10_.mp4
```

## Changes

The video extraction method has been updated to improve compatibility with Pinterest changes.

Previously, the script depended on a specific HTML structure and CSS class:

```html
<video class="hwa kVc MIw L4E">
```

This could cause the script to stop working if Pinterest changed its HTML structure or class names.

The updated version extracts video URLs directly from the page content by searching for Pinterest video URLs instead of relying on specific HTML classes.

This makes the script:

* Less dependent on Pinterest frontend changes
* More reliable when the page structure changes
* Easier to maintain

## Download Progress

The script uses `tqdm` to display download progress in the terminal.

The progress bar shows:

* Download percentage
* Download speed
* Downloaded size
* Remaining time

## Limitations

This script depends on Pinterest's internal video URL format.

If Pinterest changes:

* Video URL format
* Video hosting domain
* Page data structure

the script may require updates.

Currently supported URL formats:

* `https://pin.it/...`
* `https://www.pinterest.com/pin/...`

## License

This script is provided as-is under the MIT license.

Feel free to modify and distribute it, but please maintain original attribution to the creator.
