from plyer import notification
import praw

title = 'New reddit post!'
message = 'A new post was made in the uvic sunbreddit'

# number of posts in a subreddit
number_of_subs = 0
#new posts
new_sub = 0


# creates the notification
def notify():
    notification.notify(title=title,
                        message=message,
                        app_icon=None,
                        timeout=10,
                        toast=False)


# api information
reddit = praw.Reddit(client_id='2qV03UbLMeEhV_kxjt4Y0A',
                     client_secret='3KKLd389WCp6hdt2EKZPXMBb9nEY9Q',
                     username='average_api',
                     password='api12345678',
                     user_agent='redditapiv1')

subreddit = reddit.subreddit('testingmyapi')

# limit of how many pots it can read
new_reddit = subreddit.new(limit=10)


# counts the submissions (posts)
def new_submission(subs):
    number_of_subs = 0
    for submission in new_reddit:
        number_of_subs = number_of_subs + 1


# recounts the posts
# if the posts are greater than old_sub send a notification
def send_notify(subs):

    for submission in new_reddit:
        new_sub = new_sub+ 1
    if new_sub > number_of_subs:
        notify()


new_submission(number_of_subs)
send_notify(number_of_subs)