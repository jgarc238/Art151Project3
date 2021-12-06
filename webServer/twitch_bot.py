from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from pprint import pprint

#app = Flask(__name__)

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

#render_template("index.html", l = l)

#if __name__ == "__main__":
 #   app.run(host="0.0.0.0", port=80, debug=True)