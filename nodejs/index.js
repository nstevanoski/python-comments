const config = require('../output.json');

const ids = config.map((o) => o.user_id)
const filtered = config.filter(({user_id}, index) => !ids.includes(user_id, index + 1))

console.log('config', config)
console.log('filtered', filtered)