'''
Pinterest video downloader
Made by Harshit
'''
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from os import system
import re
from datetime import datetime
system("cls")

# Download function 
def download_file(url, filename):
    response = requests.get(url, stream=True)

    file_size = int(response.headers.get('Content-Length', 0))
    progress = tqdm(response.iter_content(1024), f'Downloading {filename}', total=file_size, unit='B', unit_scale=True, unit_divisor=1024)

    with open(filename, 'wb') as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


print("Enter page url :",end=" ")
page_url =  input() # Taking input if url
# checking entered url is correct
if("pinterest.com/pin/" not in page_url and "https://pin.it/" not in page_url):
    print("Entered url is invalid")
    exit()

if("https://pin.it/" in page_url): # pin url short check
    print("extracting orignal pin link")
    t_body = requests.get(page_url)
    if(t_body.status_code != 200):
        print("Entered URL is invalid or not working.")
    soup = BeautifulSoup(t_body.content,"html.parser")
    href_link = (soup.find("link",rel="alternate"))['href']
    match = re.search('url=(.*?)&', href_link)
    page_url = match.group(1) # update page url 

print("fetching content from given url")
body = requests.get(page_url) # GET response from url
if(body.status_code != 200): # checks status code
    print("Entered URL is invalid or not working.")
else:
    soup = BeautifulSoup(body.content, "html.parser") # parsing the content
    print("Fetched content Sucessfull.")
    ''' extracting the url
    <video
        autoplay="" class="hwa kVc MIw L4E"
        src="https://v1.pinimg.com/videos/mc/hls/......m3u8"
        ....
    ></video>
    '''
    extract_url = (soup.find("video",class_="hwa kVc MIw L4E"))['src'] 
    # converting m3u8 to V_720P's url
    convert_url = extract_url.replace("hls","720p").replace("m3u8","mp4")
    print("Downloading file now!")
    # downloading the file 
    download_file(convert_url, datetime.now().strftime("%d_%m_%H_%M_%S_")+".mp4")
