import { createClient } from 'redis';

const client = createClient()
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))

client.connect(console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value)
  console.log('ok')
}

const displaySchoolValue = (schoolName) => {
  client.GET(schoolName)
    .then((value) => { console.log(value) })
  //console.log(value)

}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
