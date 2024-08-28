import { createQueue } from "kue";

const queue = createQueue({ name: 'push_notification_code' })

const job = queue.create('push_notification_code', {
    phoneNumber: '6387',
    message: 'Hi',
})

job
    .on('enqueue', () => {
        console.log('Notification job created:', job.id);
    })
    .on('complete', () => {
        console.log('Notification job completed');
    })
    .on('failed attempt', () => {
        console.log('Notification job failed');
    });
job.save();
