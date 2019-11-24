import argparse
from hash import check_password
from models.User import User
from connect import connecting

cur = connecting()

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help='User login, email')
parser.add_argument('-p', '--password', help='User password, min. 8 characters')
parser.add_argument('-n', '--new-pass', help='New user password, min. 8 characters')
parser.add_argument('-l', '--list', help='List every user', action="store_true")
parser.add_argument('-d', '--delete', help='User login to delete', action="store_true")
parser.add_argument('-e', '--edit', help='User login to edit', action="store_true")

args = parser.parse_args()

if args.list:
    for user in User.load_all_users(cur):
        print(user.username)

elif args.username is not None and args.password is not None:
    if args.delete:
        user = User.load_user_by_email(cur, args.username)
        hashed = user.hashed_password
        if check_password(args.password, hashed):
            user.delete(cur)
            print("User: ", user.username, "deleted")
        else:
            print("Password incorrect")

    elif args.edit:
        user = User.load_user_by_email(cur, args.username)
        hashed = user.hashed_password
        if check_password(args.password, hashed):
            if args.new_pass is not None:
                if len(args.new_pass) >= 8:
                    user.set_password(args.new_pass)
                    print("Password changed")
                else:
                    print("Password too short")
            else:
                print("No new password entered")
        else:
            print("Wrong password")

    elif User.load_user_by_email(cur, args.username):
        print("User with this email exist")

    elif User.load_user_by_email(cur, args.username) is None:
        if len(args.password) >= 8:
            new_user = User()
            new_user.email = args.username
            new_user.username = args.username
            new_user.set_password(args.password)
            new_user.save_to_db(cur)
            print("You created new user with mail: ", new_user.email)
        else:
            print("Password is too short")

    else:
        print("I really don't know how did you get here")
else:
    parser.print_help()
