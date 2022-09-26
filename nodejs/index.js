const config = require('../output.json');

const arr = [{id: 1, name: 'one'}, {id: 2, name: 'two'}, {id: 1, name: 'one'}]

const ids = config.map(o => o.user_id)
const filtered = config.filter(({user_id}, index) => !ids.includes(user_id, index + 1))

console.log('config', config)
console.log('filtered', filtered)