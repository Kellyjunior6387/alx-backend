import { createClient } from 'redis';

const client = createClient()
    .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))

client.connect(console.log('Redis client connected to the server'));

client.hSet('HolbertonSchools', {
    Portland: 50,
    Seattle: 80,
    New_York: 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
})

client.hGetAll('HolbertonSchools')
    .then((value) => { console.log(value) });
