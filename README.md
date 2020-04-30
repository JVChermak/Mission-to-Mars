# Mission-to-Mars

## Overview of the Project
Create a web app to display articles, images and imformation about Mars by scraping data from various websites. The following tasks were done to complete the project.
1. Use BeautifulSoup and Splinter to automate a web browser and scrape NASA's top article and featured image, Space-Facts table of information and four USGS high-resolution images.
2. Use a MongoDB database to store data from the scrape.
3. Create a Flask app to display the data from the scrape.
4. Use Bootstrap to style the app, including a carousel for the high-resolution images.

## Resources
- Data Source: 
  - NASA Mars article: https://mars.nasa.gov/news/
  - NASA featured image: https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
  - Mars Facts: https://space-facts.com/mars/
  - High res images: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
- Software: Jupyter Notebook, Python 3.6.1, Flask, MongoDB, BeautifulSoup, Splinter, Bootstrap

## App
The main page will load with the most recently scraped article from NASA's Mars news page, the featured image, Mars facts and four high resolution images rotating in a carousel. On each image of the carousel is a button to view the full enhanced image. Once viewing the enhanced page, you have the option to return to the home page. By selecting the "Scrape New Data" button, the app will run the code to scrape each site again and will show today's article and featured image. When done, you will receive a message and the option to return to the home page to view the updated content. The table and high resolution images will remain the same.

![Mars app demo](/images/mars_scrape_demo.gif)
