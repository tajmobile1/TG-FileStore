# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "9738903"))
	API_HASH = os.environ.get("API_HASH", "d05599b2b23fd03e208ca54a2ff93445")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "5994563810:AAFRy9X_0NK2YHRrsBZoMYeGnpCZSlpMVF0")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "tajlinkfilestore_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001648402512"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1030188110"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://tgfilestore:tgfilestore@cluster0.ippxmby.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001256648377")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001871743751")
	HOME_TEXT = """
Hello [{}](tg://user?id={}), I am a file or media store bot. Send me any file or media I will give you a permanent sharable link. I support channel also.

- Send a file or media for sharable link
- Just add me in your channel as admin with edit other messages permission

Made by @FayasNoushad
"""
