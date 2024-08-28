import { createClient } from 'redis';

const client = createClient()
    .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))

client.connect(console.log('Redis client connected to the server'));

client.subscribe('holberton school channel')

client.on('message', (channel, msg) => {
    console.log(msg)
    if (msg === 'KILL_SERVER') {
        client.unsubscribe(channel)
        client.quit()
    }
})
