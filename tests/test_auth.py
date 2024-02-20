from mastodon import Mastodon

try:
    import config
except:
    print("No twitter keys found")

# import twitter
# def test_auth_twitter():
#     api = twitter.Api(
#         consumer_key=config.consumer_key,
#         consumer_secret=config.consumer_secret,
#         access_token_key=config.access_token_key,
#         access_token_secret=config.access_token_secret,
#     )

#     creds = api.VerifyCredentials()
#     assert creds.screen_name == "limno_papers"

def test_auth_mastodon():
    mastodon = Mastodon(access_token="limnopapers_clientcred.secret")
    assert mastodon.app_verify_credentials()["name"] == "limnopapers"

