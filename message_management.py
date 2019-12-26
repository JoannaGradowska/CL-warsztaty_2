import argparse
from datetime import datetime

from hash import check_password
from models.User import User
from models.Message import Message
from connect import connecting

cur = connecting()

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='User login, email')
parser.add_argument('-p', '--password', help='User password, min. 8 characters')
parser.add_argument('-l', '--list', help='List every statement', action="store_true")
parser.add_argument('-t', '--to', help='User mail to whom you would like to send message', action="store")
parser.add_argument('-s', '--send', help='Sending message', action="store")

args = parser.parse_args()

if args.list:
    if args.username is not None and args.password is not None:
        user = User.load_user_by_email(cur, args.username)
        hashed = user.hashed_password
        if check_password(args.password, hashed):
            messages = Message.load_all_messages_for_user(cur, user.id)
            if not messages:
                print("There is no messages to this user")
            else:
                for message in messages:
                    print(
                        f"From:{User.load_user_by_id(cur, message.from_id).username}\n Date: {message.creation_date}\n Message: {message.text}")

        else:
            print("Password incorrect")
elif args.send:
    if args.username is not None and args.password is not None:
        user = User.load_user_by_email(cur, args.username)
        hashed = user.hashed_password
        if check_password(args.password, hashed):
            if args.to is not None:
                recipient = User.load_user_by_email(cur, args.to)
                if recipient is not None:
                    if args.send is not None:
                        new_message = Message()
                        new_message.to_id = recipient.id
                        new_message.from_id = user.id
                        new_message.text = args.send
                        new_message.creation_date = datetime.now()
                        new_message.save_to_db(cur)
                        print(f"You send a message to {recipient.username}")
                    else:
                        print("Please enter a message")
                else:
                    print("There is no user with this mail")
        else:
            print("Password incorrect")
else:
    parser.print_help()
