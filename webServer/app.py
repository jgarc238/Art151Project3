from flask import Flask, render_template, jsonify
import requests
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from pprint import pprint

app = Flask(__name__)

client_id = 'j68jjce84wl6viql4ybagvokpg94wq'
secret = 'pvxumf8ijbw0p3f2ascv6ch46bo04b'
twitch = Twitch(client_id, secret)
target_scope = [AuthScope.MODERATION_READ]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
# this will open your default browser and prompt you with the twitch verification
token, refresh_token = auth.authenticate()
# add User authentication
twitch.set_user_authentication(token, target_scope, refresh_token)
Twitch(client_id, secret, target_app_auth_scope=target_scope) 
l = len(twitch.get_banned_users(broadcaster_id=126968602, user_id=None)['data'])
pprint(f'{l} sus peeps in chat.')

@app.route("/internalcall", methods = ['GET', 'POST'])
def getData():

    bannedUsers = len(twitch.get_banned_users(broadcaster_id=126968602, user_id=None)['data'])
    bu = bannedUsers * 20
    numbers = f'font-size: {bu}px;'
    #f'<h3 id=BannedUsers>{bannedUsers}</h3>'
    data = {'bannedUsers' : numbers}

    return jsonify(**data)

@app.route("/")
def helloworld():


    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=3000, debug=True)

