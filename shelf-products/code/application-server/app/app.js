const express = require('express');
const app = express();
const mainRoutes = require('./routes/mainRoutes');

app.use('/', mainRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});