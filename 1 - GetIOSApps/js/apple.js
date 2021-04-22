var store = require('app-store-scraper');

store.list({
  collection: store.collection.TOP_PAID_IOS,
  //category: store.category.GAMES_ACTION,
  num: 6
})
.then(console.log)
.catch(console.log);