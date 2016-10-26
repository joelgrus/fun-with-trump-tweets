# Tweets on a Globe

This script will display a spinning globe that streams and displays tweets about "trump" (or any other topic)

First, add some credentials in `credentials.js`:

```
module.exports = {
  consumer_key: "...",
  consumer_secret: "...",
  access_token_key: "...",
  access_token_secret: "..."
};
```

And then

```
npm install
node twitter.js
```

or

```
node twitter.js hillary
```

It will serve the app on port 3000.

![globe](https://raw.githubusercontent.com/joelgrus/twitter-globe/master/globe.gif)
