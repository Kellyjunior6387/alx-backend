import { createQueue } from "kue";

// Create a Kue queue
const queue = createQueue();

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
    // Track initial progress
    job.progress(0, 100);

    // Check if the phone number is blacklisted
    if (blacklistedNumbers.includes(phoneNumber)) {
        // Fail the job if the number is blacklisted
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // Track progress to 50%
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Complete the job
    done();
}

// Process jobs in the queue "push_notification_code_2" with concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
