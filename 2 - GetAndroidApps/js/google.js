var gplay = require('google-play-scraper');
const converter = require('json-2-csv');
var fs = require('fs')

async function meuovo(){
    return gplay.list({
        category: gplay.category.APPLICATION,
        collection: gplay.collection.TOP_PAID,
        throttle:5,
        num: 1000})
}

meuovo().then
( response => { converter.json2csv(response, (err, csv) => {
    if (err) {
        throw err;
    }
    
    fs.writeFileSync('app_paid_android_fullofshit.csv', csv);
    
})})


  /*.then(converter.json2csv(this, (err,csv) => {
      if (err) {throw err;}
      console.log(csv);
      fs.writeFile('todos.csv', csv);
  }));
    */

