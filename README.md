# Random-Desktop-Wallpaper-Changer

## Description
This is a simple python program where you can get a random desktop wallpaper. This program offers an extensive collection of stunning HD wallpapers. You also have the freedom to get wallpapers from various categories, like nature, video games, landscapes, animals, abstract art, and more by typing some search words in the search box, which gives you a random wallpaper from the words you've written. 
The program is optimized to run seamlessly without worrying about slowdowns or performance issues. It's simple, fast and easy to use ;).

## How it works?
Tiil now, the program only uses https://wallpaperswide.com/ to get the wallpaper. It's a great website and contains a lot of HD wallpapers from different categories.
This is the flow of the program:
  <pre>
 - The program sends a request to https://wallpaperswide.com/ with the search query that the user has written in the search box.
 - By accessing the pagination div, the program gets the maximum number of pages available for the specified search query.
 - A random page is selected between (1, maximum page).
 - A random wallpaper is selected from the list of the wallpapers in that page.
 - The program gets the resolution of the user's monitor and downloads the wallpaper with that resoultion. 
 - The wallpaper is saved as "image.jpg" and set as desktop background.
</pre>

## Libraries
The libraries used are:
- Tkinter (For the GUI)
- Requests (To send get requests to the website)
- BeautifulSoup (For web scraping)
- Screeninfo (To get the user's monitor resoultion) 
- Ctypes (To set the downloaded image as desktop wallpaper)
- Random (For randomiazation)
- Os.path (To get the path of the current directory)

## Sample
![Loading a sample gif...](sample.gif)
