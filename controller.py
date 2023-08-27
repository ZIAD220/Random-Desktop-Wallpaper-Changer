import os.path
import random
import ctypes
import requests
import bs4


def flow(query):
    # Modifying the query to replace %20 instead of spaces.
    new_query = query.replace(" ", "%20")

    page = requests.get(f"https://wallpaperswide.com/search.html?q={new_query}")

    page = get_random_page(page, query)
    if page is None:
        return False

    page = get_random_wallpaper(page)

    download_wallpaper(page)

    set_wallpaper()

    return True


def get_random_page(page, query):
    src = page.content
    soup = bs4.BeautifulSoup(src, 'lxml')

    # Handling corner case when there's no results at all.
    pagination = soup.find('div', {'class': 'pagination'})
    if pagination is None:
        return None

    # Getting number of pages available.
    max_page = int(pagination.contents[len(pagination) - 2].text)

    random_page = random.randint(1, max_page)
    page = requests.get(f'https://wallpaperswide.com/search/page/{random_page}?q={query}')

    src = page.content
    soup = bs4.BeautifulSoup(src, 'lxml')
    return soup


def get_random_wallpaper(page):
    wallpapers = page.find_all('li', {'class': 'wall'})

    random_index = random.randint(0, len(wallpapers) - 1)
    random_wallpaper = 'https://wallpaperswide.com' + wallpapers[random_index].find('a')['href']

    return random_wallpaper


def download_wallpaper(url):
    page = requests.get(url)
    src = page.content
    soup = bs4.BeautifulSoup(src, 'lxml')

    resolutions = soup.findAll('a', {'target': '_self'})

    image_link = 'https://wallpaperswide.com'
    for a in resolutions:
        if a['href'].find('1920x1080') > -1:
            image_link += a['href']

    image = requests.get(image_link)
    with open("image.jpg", "wb") as f:
        f.write(image.content)


# Setting the downloaded image to be the desktop wallpaper.
def set_wallpaper():
    SPI_SETDESKWALLPAPER = 20
    ROOT = os.path.dirname(os.path.abspath(__file__))
    path = ROOT + "\image.jpg"
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
    return

