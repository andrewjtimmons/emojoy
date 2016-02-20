var webdriverio = require('webdriverio');
var options = {
    desiredCapabilities: {
        browserName: 'firefox'
    }
};
var slackname = process.argv[2]

webdriverio
    .remote(options)
    .init()
    .url('https://' + slackname + '.slack.com/')

    .title(function(err, res) {
        if (err) {
            console.log(err)
        }
        console.log('Title was: ' + res.value);
    })
    .end();

