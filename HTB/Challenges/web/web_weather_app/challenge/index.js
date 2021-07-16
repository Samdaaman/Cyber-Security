const express       = require('express');
const app           = express();
const bodyParser    = require('body-parser');
const routes        = require('./routes');
const path          = require('path');
const Database      = require('./database');

const db = new Database('weather-app.db');

app.use(bodyParser.json({
    verify: (req, res, buf) => {
      req.rawBody = buf
    }
}));
app.use(bodyParser.urlencoded({
    extended: true
}));

app.use((req, res, next) => {
    console.log(`--> ${req.method}: ${req.url}`);
    req.rawBody != null && console.log(req.rawBody.toString());
    console.log('-----------------------');
    console.log(req.body);
    console.log('=======================');

    next();
})

app.set('views', './views');
app.use('/static', express.static(path.resolve('static')));

app.use(routes(db));

app.all('*', (req, res) => {
    return res.status(404).send({
        message: '404 page not found'
    });
});

(async () => {
    await db.connect();
    await db.migrate();

    app.listen(80, () => console.log('Listening on port 80'));
})();