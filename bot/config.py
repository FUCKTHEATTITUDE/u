import os


class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN","6249559768:AAFmG1A7WucTp83nofzUk63HXJhzf9c-v3s")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("API_ID",'14782914'))

    API_HASH = os.environ.get("API_HASH","3aa2fabe1074632cf6e2b01da083a2c6")

    CLIENT_ID = os.environ.get("CLIENT_ID","956304545456-djmeuuuij3cjfjclkaogsoe88h7kcr04.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET","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")

    BOT_OWNER = int(os.environ.get("BOT_OWNER","1930954213"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "1930954213")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
