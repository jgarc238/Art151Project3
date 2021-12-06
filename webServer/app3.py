from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route("/")
def helloworld():

    #CLIENT_ID = "j68jjce84wl6viql4ybagvokpg94wq"
    #User_ID = 126968602
    #SECRET = "pvxumf8ijbw0p3f2ascv6ch46bo04b"
    #working urls = https://api.twitch.tv/helix/games/top , https://api.twitch.tv/helix/users?login=arkeyanmetalman

    URL = 'https://api.twitch.tv/helix/moderation/banned?broadcaster_id=126968602'
    authURL = 'https://id.twitch.tv/oauth2/token'
    Client_ID = "j68jjce84wl6viql4ybagvokpg94wq"
    Secret  = "pvxumf8ijbw0p3f2ascv6ch46bo04b"

    AutParams = {
            'client_id': Client_ID,
            'client_secret': Secret,
            'grant_type': 'client_credentials'
            }


    #def Check():
    AutCall = requests.post(url=authURL, params=AutParams) 
    access_token = AutCall.json()['access_token']
    print(access_token)

    head = {
        'Authorization' :  "Bearer " + 'pt5oii091dxwqxeaid0rf2kd34aubm',
        'Client-ID' :  Client_ID,
        'scope' : "moderation:read"
    }

    r = requests.get(URL, headers = head).json()#['data']
    print(requests.get(URL, headers = head).json())

   

    #print(Check())


    return render_template("index.html", r = r)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)