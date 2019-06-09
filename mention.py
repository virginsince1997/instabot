"""
instabot example

workflow:
    mention [@user] in comment section
"""
import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('user', type=str, help='user')
parser.add_argument('nfollowers', type=int, help='nfollowers')
args = parser.parse_args()

bot = Bot()
bot.login()

userID = bot.get_user_id_from_username(args.user)
someones_followers =  bot.api.get_total_followers_or_followings(userID,
                                                                amount=args.nfollowers,
                                                                filter_private=False,
                                                                filter_business=False,
                                                                filter_verified=False,
                                                                usernames=True,)

medias = bot.get_your_medias()
media_to_comment = medias[0]

for usr in someones_followers:
    comment = '@' + usr
    bot.api.comment(media_to_comment, comment)
    bot.console_print('{} media commented with text: {}'.format(media_to_comment, comment), 'green')
    bot.total['comments'] += 1
    bot.delay('comment')

'''
# get a list of users to mention and store in a text file
input(colored("what user followers do you want to scrape ? : ", 'red'))  # scrape users followers
with open('someones_followers_scrape.txt', 'w') as file:
    file.write(someones_followers)
pages_to_scrape = bot.read_list_from_file("someones_followers_scrape.txt")  # reading passed "someones followers to  scrape"
f = open("scrappedFOLLOWERS.txt", "w")  # stored list of "Someone's Followers"
for follower in pages_to_scrape:
    users = bot.get_user_followers(follower,30)
for userfollowers in users:
    f.write(userfollowers + "\n")
print(colored("\n" + "successfully written Someone's Followers , to textfile scrappedFOLLOWERS.txt", 'green'))
f.close()

# convert passed scrapped followers to usernames


print(colored("Converting scrappedFOLLOWERS.txt to usernames, MIGHT TAKE AWHILE!!!!", 'red'))
wusers = bot.read_list_from_file("scrappedFOLLOWERS.txt")
with open("usernamelist.txt", 'w+') as f:
	for list in wusers:
		usernames=bot.get_username_from_user_id(list) + '\n'
		f.write(usernames)
	print(colored("succesfully converted  " + str(wusers), 'green'))

# append '@' to scrapped list


print("adding '@' to usernames")
appendText = '@'
followlist = open("usernamelist.txt", 'r')
updatedList = open("mentionlist.txt", 'w')
for name in followlist:
    updatedList.write(appendText + name.rstrip() + '\n')
updatedList.close()
print(colored("succesfully appended '@' to usernames", 'green'))


# comment @users on last media post
medias=bot.get_your_medias()
while True:
	bot.comment_medias([medias[0]])
'''