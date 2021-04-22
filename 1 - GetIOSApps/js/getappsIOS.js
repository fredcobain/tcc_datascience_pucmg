
var apple = require('app-store-scraper'); //lib de apoio para fazer o scrape na página da AppStore
const converter = require('json-2-csv'); //lib de apoio para converter resultado para arquivo csv
const fs = require('fs') //lib para manipular arquivos
const {promisify} = require('util') //lib para transformar um callback em promise - assim evitamos o callback hell e deixamos o código mais enxuto.
const csv_async = promisify(converter.json2csv) //variável onde vamos armazenar o resultado do nosso scrape convertendo-o pra csv

/*---------Objeto com as opções utilizadas para listar os TOP 200 APPS pagos para IOS-----*/
const appOptions= { 
    //category: apple.category.APPLICATION,
    collection: apple.collection.TOP_PAID_IOS,
    throttle: 5,
    country: 'br',
    num: 200
}

/*---------Objeto com as opções utilizadas para gerar o arquivo csv via filestream-----*/
const streamOptions = {
    flags: 'w+',
    encoding: 'unicode'
}

/*---------Função para fazer o scrape e salvar o resultado-----*/
async function scrape() {
    const response = await (apple.list(appOptions)) //invocamos o método list() da nossa lib que automatiza o scrape
    const csv_var = await csv_async(response) //armazenamos o resultado na variavel csv_var transformando o stream em csv
    const stream = fs.createWriteStream('ios_apps_br_paid-unicode.csv', streamOptions) //preparamos um novo arquivo no file server o arquivo para receber o fluxo de dados no formato csv
    stream.write(csv_var) //salvamos o resultado no arquivo
}


scrape()
