import random
import ctypes
import requests
import bs4


def flow(query):
    # Modifying the query to replace %20 instead of spaces.
    new_query = query.replace(" ", "%20")

    print(new_query)

    page = requests.get(f"https://wallpaperswide.com/search.html?q={new_query}")
    page = get_random_page(page, query)
    if page is None:
        return False
    page = get_random_wallpaper(page)
    download_wallpaper(page)
    set_wallpaper()
    return True

# Get random picture.
def get_random_page(page, query):
    src = page.content
    soup = bs4.BeautifulSoup(src, 'lxml')

    # Getting number of pages available.
    pagination = soup.find('div', {'class': 'pagination'})
    if pagination is None:
        return None

    max_page = int(pagination.contents[len(pagination) - 2].text)

    random_page = random.randint(1, max_page)
    page = requests.get(f'https://wallpaperswide.com/search/page/{random_page}?q={query}')
    src = page.content
    soup = bs4.BeautifulSoup(src, 'lxml')
    return soup




# Get random wallpaper.
def get_random_wallpaper(page):
    wallpapers = page.find_all('li', {'class': 'wall'})
    print(wallpapers)
    random_index = random.randint(0, len(wallpapers) - 1)
    random_wallpaper = 'https://wallpaperswide.com' + wallpapers[random_index].find('a')['href']
    print(random_wallpaper)
    return random_wallpaper




# Download wallpaper
def download_wallpaper(url):
    page = requests.get(url)
    src = page.content
    soup = bs4.BeautifulSoup(src, 'lxml')

    resolutions = soup.findAll('a', {'target': '_self'})

    image_link = 'https://wallpaperswide.com'
    for a in resolutions:
        if a['href'].find('1920x1080') > -1:
            image_link += a['href']

    print(image_link)
    image = requests.get(image_link)
    with open("image.jpg", "wb") as f:
        f.write(image.content)




# Setting the downloaded image to be the desktop wallpaper.
def set_wallpaper():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "E:\Codes\Web Scraping\image.jpg", 3)
    return

