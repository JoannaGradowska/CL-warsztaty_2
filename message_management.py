import argparse
from hash import check_password
from models.User import User
from connect import connecting

cur = connecting()

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='User login, email')
parser.add_argument('-p', '--password', help='User password, min. 8 characters')
parser.add_argument('-l', '--list', help='List every statement', action="store_true")
parser.add_argument('-t', '--to', help='User mail to whom you would like to send message', action="store_true")
parser.add_argument('-s', '--send', help='Sending message', action="store_true")

args = parser.parse_args()

if args.list:
    if args.username is not None and args.password is not None:
        user = User.load_user_by_email(cur, args.username)
        hashed = user.hashed_password
        if check_password(args.password, hashed):
            #list every message from newest to oldest
            pass
        else:
            print("Password incorrect")
