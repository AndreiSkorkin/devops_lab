import argparse
import getpass
import requests

user = input("Enter GitHub credentials: ")
password = getpass.getpass()

parser = argparse.ArgumentParser()
parser.add_argument('PR', help='pull request number')
parser.add_argument('--Version', action="store_true", help='program version')
parser.add_argument('--Comm', action="store_true", help='number of comments')
parser.add_argument('--UCreated', action="store_true", help='who opended PR')
parser.add_argument('--DCreated', action="store_true", help='when opened PR')
parser.add_argument('--Close', action="store_true", help='when closed PR')

args = parser.parse_args()
r = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls/' +
                 args.PR, auth=(user, password))
dict = r.json()

if args.Version:
    print('Version 1.0')
elif args.Comm:
    print('Number of comments:', dict['review_comments'])
elif args.UCreated:
    print('Created by:', dict['user']['login'])
elif args.DCreated:
    print('Created at:', dict['created_at'])
elif args.Close:
    print('Closed at:', dict['closed_at'])
else:
    print('ERROR')
