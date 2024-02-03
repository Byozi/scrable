from Scrable.core.bot import Lipps
from Scrable.core.dir import dirr
from Scrable.core.git import git
from Scrable.core.userbot import Userbot
from Scrable.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Lipps()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
