import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.


# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('I am a dumb bot', flush=True)

'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
	f_read = open(file_name,'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name,'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

def reply():
	last_seen_id = retrieve_last_seen_id(FILE_NAME)
	mentions=api.mentions_timeline()
	for mention in mentions:
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		print(str(mention.id) + ' - ' + mention.text)
		if '#apple' in mention.text:
			print('responding back...', flush=True)
			api.update_status('@' + mention.user.screen_name + '#pineapple', mention.id)


while True:
	reply()
	time.sleep(15)			