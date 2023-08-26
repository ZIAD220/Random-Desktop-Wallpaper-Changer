import random
import ctypes
import requests
import bs4

# Here we need to handle input.


page = requests.get("https://wallpaperswide.com/search.html?q=assassins%20creed")


# Get random picture.
def getRandomPage(page):
    src = page.content
    soup = bs4.BeautifulSoup(src, 'lxml')

    # Getting number of pages available.
    max_page = int(soup.find('div', {'class': 'pagination'}).contents[4].text)

    random_page = random.randint(1, max_page)
    page = requests.get(f'https://wallpaperswide.com/search/page/{random_page}?q=assassins%20creed')
    src = page.content
    soup = bs4.BeautifulSoup(src, 'lxml')
    return soup

page = getRandomPage(page)

# Get random wallpaper.
def getRandomWallpaper(page):
    wallpapers = page.find_all('li', {'class': 'wall'})
    print(wallpapers)
    random_index = random.randint(0, len(wallpapers) - 1)
    random_wallpaper = 'https://wallpaperswide.com' + wallpapers[random_index].find('a')['href']
    print(random_wallpaper)
    return random_wallpaper

page = getRandomWallpaper(page)

# Download wallpaper
def downloadWallpaper(url):
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

page = downloadWallpaper(page)

# Setting the downloaded image to be the desktop wallpaper.
def setWallpaper():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "E:\Codes\Web Scraping\image.jpg", 3)
    return

setWallpaper()