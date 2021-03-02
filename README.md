# Theia
## Goal: 
Create a web scraping framework. Python is fantastic for simpler tasks like harvesting. NodeJS was significantly easier than Python for extracting data on websites with a ton of JS.
As a result The framework will consist of two components. Python for harvesting & JavaScript for extracting information.
## Technologies:
* Virtualization/Containers
    * Docker
    * VirtualBox
* Databases
    * MySQL Community 
    * MongoDB
* JavaScript
    * NodeJS
    * Axios
    * Cheerio
* Python
    * BS4
    * Requests
## Tips:
    * Use NoScript or disable Javascript in your browser, you can't scrape something that isn't rendered.
    * Save web pages and launch a docker instance, VM, IIS, Flask, Nginx, Apache, XAMPP etc.
    * When deciding to scrape a website, view the Robots.txt and see if there's an API regarding data collection.
    * Time requests to a website.
    * Use headers and cookies. To generate a website cookie go to the domain > inspect element(f12(Firefox),(f12)(Brave) or...<br>
    * Tap the right mouse button (click 'inspect element') 'navigate to the console') > alert(document.cookie); or console.log(document.cookie);
    * If you're using a VPN/TOR make sure your system time aligns with your connections time. If you have JavaScript enabled you can see current system time.(When extracting your cookie!)

