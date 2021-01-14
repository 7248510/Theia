//https://flaviocopes.com/javascript-sleep/
function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
}   
  module.exports = {sleep}