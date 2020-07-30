import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("1087554051947069440-MzZp0mb7cdKlxp8pedkFfwjRpMNFXB")
auth.set_access_token("Rd79izcHNda1N7x9oWeHGy8doYrUMhUxUXAbPeqP5AuU6")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")