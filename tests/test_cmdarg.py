import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--tweet', help="Publish limnopapers tweets? Boolean \
                                    defaults to False.",
                    type = bool, default = False)
args = parser.parse_args()
print(args.tweet)
