// app.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();

// Middleware
app.use(bodyParser.json());

// DB Connection
mongoose.connect('mongodb://localhost:27017/nacacomstore', { useNewUrlParser: true, useUnifiedTopology: true });

// Routes
app.use('/api/posts', require('./post'));
app.use('/api/users', require('./router'));

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));