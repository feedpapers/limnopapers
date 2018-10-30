import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--tweet', default = False,
                    action='store_true')
parser.add_argument('--interactive', default = False,
                    action='store_true')
args = parser.parse_args()
print(args.tweet)
print(args.interactive)
