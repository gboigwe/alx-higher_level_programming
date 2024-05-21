#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./6-completed_tasks.js API_URL');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasks = tasks.filter(task => task.completed);
    const userCompletedTasks = completedTasks.reduce((userTasks, task) => {
      const userId = task.userId;
      if (userTasks[userId]) {
        userTasks[userId]++;
      } else {
        userTasks[userId] = 1;
      }
      return userTasks;
    }, {});

    for (const userId in userCompletedTasks) {
      console.log(`${userId}: ${userCompletedTasks[userId]}`);
    }
  } else {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    process.exit(1);
  }
});
