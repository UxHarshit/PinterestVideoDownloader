'''
Pinterest video downloader
Made by Harshit
'''

import requests
from bs4 import BeautifulSoup
from os import system
from tqdm import tqdm
import re
from datetime import datetime

system("cls")


def download_file(url, filename):
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('Content-Length', 0))

    progress = tqdm(response.iter_content(1024),desc=f"Downloading {filename}",total=file_size,unit='B',unit_scale=True,unit_divisor=1024)

    with open(filename, 'wb') as f:
        for data in progress:
            f.write(data)
            progress.update(len(data))

    print("Download completed!")


print("Enter page url :", end=" ")
page_url = input()


if ("pinterest.com/pin/" not in page_url and "https://pin.it/" not in page_url):
    print("Entered url is invalid")
    exit()


if ("https://pin.it/" in page_url):

    print("extracting original pin link")

    t_body = requests.get(page_url)

    if t_body.status_code != 200:
        print("Entered URL is invalid or not working.")
        exit()

    soup = BeautifulSoup(t_body.content,"html.parser")

    link_tag = soup.find("link",rel="alternate")

    if link_tag is None:
        print("Original pin link not found.")
        exit()

    href_link = link_tag.get("href")

    match = re.search('url=(.*?)&',href_link)

    if match is None:
        print("Could not extract original url.")
        exit()

    page_url = match.group(1)


print("fetching content from given url")

body = requests.get(page_url)


if body.status_code != 200:
    print("Entered URL is invalid or not working.")


else:
    soup = BeautifulSoup(body.content,"html.parser")

    print("Fetched content Successful.")

    video_urls = re.findall(r'https://v1\.pinimg\.com/videos/[^"]+', body.text)

    if len(video_urls) == 0:
        print("Video url not found.")
        exit()

    extract_url = video_urls[0]

    convert_url = (extract_url.replace("hls", "720p").replace("m3u8", "mp4"))

    print("Downloading file now!")

    download_file(convert_url, datetime.now().strftime("%d_%m_%H_%M_%S_") + ".mp4")