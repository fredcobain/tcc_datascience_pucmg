var gplay = require('google-play-scraper');
const converter = require('json-2-csv');
const fs = require('fs')
const {promisify} = require('util')
const csvasync = promisify(converter.json2csv)

const appOptions= {
    category: gplay.category.APPLICATION,
    //collection: gplay.collection.TOP_PAID,
    throttle: 5,
    country: 'br',
    num: 2000
}


const streamOptions = {
    flags: 'w+',
    encoding: 'utf-8'
}

async function scrape() {
    const response = await (gplay.list(appOptions))

    const csv_var = await csvasync(response)

    const stream = fs.createWriteStream('google_apps_br_fullofshit.csv', streamOptions)
    stream.write(csv_var)

}

scrape()

