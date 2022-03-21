#I could have just used the date function built into PRAW but that seemed to simple
#In practice use has to call new_submission() once to populate the array after that only send_notify() is needed
from plyer import notification
import praw

title = 'New reddit post!'
message = 'A new post was made in the uvic sunbreddit'

#array of submission titles
titles = []

# creates the notification
def notify():
    notification.notify(title=title,
                        message=message,
                        app_icon=None,
                        timeout=10,
                        toast=False)
    print("You have now been notified")


# api information
reddit = praw.Reddit(client_id='2qV03UbLMeEhV_kxjt4Y0A',
                     client_secret='3KKLd389WCp6hdt2EKZPXMBb9nEY9Q',
                     username='average_api',
                     password='api12345678',
                     user_agent='redditapiv1')

subreddit = reddit.subreddit('testingmyapi')

# limit of how many posts it can read
new_reddit = subreddit.new(limit=10)


# creates an array of post titles
def new_submission():
    for submission in new_reddit:
        titles.append(submission.title)

posts = subreddit.new(limit = 1)

# gets the first title
# if the title is not in the array notifies of a new post
#then adds title to the array
def send_notify():
    #keeps track of the title of a new submission
    title1 = ''
    for submission in posts:
        title1 = submission.title
    if title1 in titles:
        return True
    else:
        titles.append(title1)
        notify()
       


#new_submission()
send_notify()
