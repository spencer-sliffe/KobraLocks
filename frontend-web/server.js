const express = require('express');
const path = require('path');
const app = express();

// Serve static files from the React app
app.use(express.static(path.join(__dirname, 'build')));

// The "catchall" handler: for any request that doesn't
// match one above, send back React's index.html file.
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

// Use the environment variable provided by Azure, or 8080 if local
const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server is up on port ${port}!`);
});
