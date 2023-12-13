# Application Server

1. To be able to run the application, go to https://nodejs.org/en/download and install _Node.js_.
To make sure the installation is correct, run either `node -v` or `npm -v`
2. Using a terminal or command prompt, change the working directory to where you would like to have the application files,
for example `path\to\application\`, and run `npm install express`. This will download the required libraries in a `node_modules` folder.
3. In the same directory `path\to\application\`:
   1. Add the `server.js` file
   2. Create a new folder `public` and add the `home.html` file there. It should look like `path\to\application\public\home.html`
   3. From the terminal, run `node server.js` to start the web-site.