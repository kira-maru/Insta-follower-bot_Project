from follow_bot import FollowBot

INSTA_ACCOUNT = "https://www.instagram.com/yorushika_official_/"
INSTA_ACCOUNT_NAME = "yorushika_official_"

fb = FollowBot()

fb.logging_in(INSTA_ACCOUNT)
fb.cookies(INSTA_ACCOUNT_NAME)
fb.follow(INSTA_ACCOUNT_NAME)
