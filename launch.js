let fs = require('fs');
//Axios + Cheerio
//npm init --yes
//npm install cheerio
//npm install axios
//https://blog.logrocket.com/how-to-make-http-requests-like-a-pro-with-axios/
let array = fs.readFileSync('test.txt').toString().replace(/\r\n/g,'\n').split('\n'); //When reading the file sometimes \r gets attached this regex removes \r & \n
let placeHolder = []; //Used in tracking the amount of spaces
for (i = 0; i < array.length; i++) //Allocating space.
  {
      placeHolder.push(i); //Push numbers instead of strings so you can loop through them.(Fixing this issue was an all day. This is the only way I figured out how to time the requests)
  }
const sleep = require("./sleep.js"); //Calling sleep js
function target(url) 
{
    const axios = require('axios');
    const cheerio = require('cheerio');
    const options = {
        headers: {'User-Agent': 'CHANGE ME'} //The headers need to align. To change your user agent 'User-Agent' needs to be passed. Not a random value
        //To test your user agent launch a docker image/IIS/Nginx/Apache and view the log files
        //https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search this extension is fantastic for getting user agents
    };
    console.log("Current URL: " + url)
    axios.get(url,options)
    .then((response) => {
        let jsonStore = {};
        const $ = cheerio.load(response.data); //Response.data is the data from the response. Save this as $ and call cheerio to load the data   
        let title = $('title').text();
        let httpCode = response.statusText;
        //I'm making this a json because I eventually plan to implement Mongo for storage/Maybe I'll make a rest API
        jsonStore = {
            "Title ": title,
            "HTTP status" : httpCode
        }
        let final = JSON.stringify(jsonStore);
        //If an error occurs here jsonStore is invalid. In order to parse it has to be valid. You can run the stringify function to ensure a proper json
        final = JSON.parse(final)
        console.log(final); 
    })
    .catch(function(err){
        console.log(err); //Catch an error
        });
}
const launch = async () => {
    for (const loopControl of placeHolder) { //The reason for placeholder is array holds strings and you cannot loop through URLS. 
    target(array[loopControl]); 
    await sleep.sleep(2000) //Every two seconds execute 
    }
}
launch()