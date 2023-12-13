# Application Server

1. To be able to run the application, go to https://nodejs.org/en/download and install _Node.js_.
To make sure the installation is correct, run either `node -v` or `npm -v`
2. Using a terminal or command prompt, change the working directory to `LOCAL-PATH\shelf-products\code\application-server`,
and run `npm install express`. This will download the required libraries in a `node_modules` folder.
3. In the same directory `LOCAL-PATH\shelf-products\code\application-server`, run `node server.js` to start the web-site.

For this prototype, CORS is enabled to allow the web-site to access the model server which are assumed both local.
This will not be the case in the final version.

To be able to access the server from a different machine, the IP address of the machine running the server needs to be added
to `home.html` in the sendToApi function.