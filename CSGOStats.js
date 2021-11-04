http = require('http');
fs = require('fs');
var newdata = false;
serverport = 3005;
host = '127.0.0.1';
var newData = false;
var newFile = true;
var arrayData = [];
server = http.createServer( function(req, res)
{
    if (req.method == 'POST')
	{
        res.writeHead(200, {'Content-Type': 'text/html'});
        var body = '';
        req.on('data', function (data)
		{
            body += data;
        });
        req.on('end', function ()
		{
        	res.end( '' );

			if (res.statusCode === 200)
			{
				try
				{
					var data = JSON.parse(body);
          var activity = data.player.activity;
          if(activity == "playing"){
            var name = data.player.name;
            var num = parseInt(data.player.state.round_kills)+parseInt(data.player.state.round_killhs);
  					var ts = Date.now().toString().substring(4, 12);
  					//console.log(ts +", " + name + ",  "+ num);
            console.log(ts.substring(3) +", " + name + ",  "+ num);
  					arrayData.push([ts, name, num]);
  					newData = true;
          }
          else{
            if(newData){
              if(newFile){
                fs.writeFileSync('data.txt', arrayData.join("\n"));
                newFile = false;
              }
              else{
                fs.appendFileSync('data.txt', arrayData.join("\n"));
              }
              arrayData = [[]];
              console.log("Left game session | Saved session data");
              newData = false;
            }
            console.log("Not in Game...");
          }
				} catch (e)
				{
					console.log('Not geing valid Game session data');
				}
			}
        });
    }
    else
    {
        console.log("Not expecting other request types...");
        res.writeHead(200, {'Content-Type': 'text/html'});
		var html = '&lt;html>&lt;body>HTTP Server at http://' + host + ':' + serverport + '&lt;/body>&lt;/html>';
        res.end(html);
    }
});

server.listen(serverport, host);
console.log('Listening at http://' + host + ':' + serverport);
