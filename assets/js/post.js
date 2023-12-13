// models/Post.js
const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const PostSchema = new Schema({
 title: String,
 content: String,
 date: { type: Date, default: Date.now }
});

module.exports = Post = mongoose.model('post', PostSchema);