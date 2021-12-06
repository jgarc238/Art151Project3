from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from pprint import pprint

#app = Flask(__name__)

client_id = 'j68jjce84wl6viql4ybagvokpg94wq'
secret = 'pvxumf8ijbw0p3f2ascv6ch46bo04b'

twitch = Twitch(client_id, secret)

target_scope = [AuthScope.MODERATION_READ]

Twitch(client_id, secret, target_app_auth_scope=target_scope) 

l = len(twitch.get_banned_users(broadcaster_id=126968602, user_id=None)['data'])
pprint(f'{l} sus peeps in chat.')