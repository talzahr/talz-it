import praw
import webbrowser

try:
    from auth import client_id, client_secret, username, password, user_agent
except ImportError:
    print("Authentication details not found in 'auth.py' file.")
    exit()

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent,
)
print(f"Logged into Reddit as: {reddit.user.me()}")

subreddit_name = input("Enter subreddit name: ")
subreddit = reddit.subreddit(subreddit_name)

submissions = list(subreddit.top('day', limit=10))

for index, submission in enumerate(submissions, start=1):
    print(f"{index}. {submission.title}   ({submission.score})")
    print(f"        -> ({submission.url})")

link_number = int(input("Enter the number of the link to open, '99' to go back, or '0' or exit: "))

if link_number == 0:
    exit()
else:
    webbrowser.open_new_tab(submissions[link_number - 1].url)