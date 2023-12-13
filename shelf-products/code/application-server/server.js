const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// add cross-origin to from any origin
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    next();
});

// serve the static HTML page under the public folder
app.use(express.static('public'));

// handle the GET request to the home page
app.get('/', (req, res) => {
    // log the request
    console.log(`Request received: ${req.url}`);
    res.sendFile(path.join(__dirname, 'public', 'home.html'));
});

// start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
