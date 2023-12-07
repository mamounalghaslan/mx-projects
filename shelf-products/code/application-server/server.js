const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// add cross-origin to the flask server from any origin
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    next();
});

app.use(express.static('public'));

app.get('/', (req, res) => {
    // log the request
    console.log(`Request received: ${req.url}`);
    res.sendFile(path.join(__dirname, 'public', 'home.html'));
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
