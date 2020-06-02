# Theia
## Goal: 
Create a Python data collection framework. Theia may replace the data repository.
## Technologies
* Databases
    * MySQL Community 
    * MongoDB
* Language
    * Python
## Tips:
    * Use NoScript or disable Javascript in your browser, you can't scrape something that isn't rendered.
    * Save web pages and launch a docker instance, VM, IIS, Flask, Nginx, Apache, XAMPP etc.
    * When deciding to scrape a website, view the Robots.txt and see if there's an API regarding data collection.
    * Time requests to a website.
    * Use headers and cookies. To generate a website cookie go to the domain > inspect element(f12(Firefox),(f12)(Brave) or...<br>
    Tap the right mouse button (click 'inspect element') 'navigate to the console') > alert(document.cookie); or console.log(document.cookie);
    * If you're using a VPN/TOR make sure your system time aligns with your connections time. If you have JavaScript enabled you can see current system time.(When extracting your cookie!)
    * Establish a goal, unless you're writting a spider determine what information you'd like to collect.  
## Modules:
* Scraping an array
* Scraping from a list
* Inserting into MySQL
* Inserting into MongoDB
* Creating lists
* URL Schemas
