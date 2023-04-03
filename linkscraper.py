import requests
from bs4 import BeautifulSoup

# https://jadi.net/tag/podcast/page/2/
base_url = "https://jadi.net/tag/podcast/page/"


num_pages = 50

for page in range(1,num_pages+1):
    url = base_url + str(page)+ "/"
    response = requests.get(url)

    if response.status_code == 404:
        print(f" Page {page} not found. Stopping the loop.")
        break

    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    links = soup.find_all("a")

    mp3_links = [link.get("href") for link in links if link.get("href").endswith(".mp3")]

    for link in mp3_links:
        print(link)
        with open('./links-py','a') as f:
            f.write(link)
            f.write('\n')


