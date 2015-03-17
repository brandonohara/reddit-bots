import sys
import getopt
import getpass
import time
import praw

__author__ = "Brandon O'Hara"
__version__ = '1.0.0'

class KriegerBot(object):
	def __init__(self, upvote, target):
		self.username = 'dr-krieger-bot'
		self.version = '1.0.0'
		self.password = getpass.getpass('Password for <%s>:' %self.username)
		
		self.r = praw.Reddit(user_agent= self.username + ' v' + self.version)
		self.r.login(self.username,self.password)
		
		self.upvoted = 0
		self.downvoted = 0
		
		self.upvote = upvote
		self.redditor = self.r.get_redditor(target, fetch=False)
		
	def run(self, limit):
		print('Limit: %d', limit)
		for post in self.redditor.get_overview(limit = limit):
			try:
				if self.upvote:
					#post.upvote()
					print "upvote"
					self.upvoted += 1
				else:
					#post.downvote()
					print "downvote"
					self.downvoted += 1
			except:
				exception('something went wrong upvoting/downvoting')
			time.sleep(2)
	

def main(argv):
	limit = 10
	help = 'bot.py -h -d-u <reddit-username> -l <limit>'
	try:
		opts, args = getopt.getopt(argv,"d:u:l:")
	except getopt.GetoptError:
		print help
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print help
			sys.exit()
		elif opt in ("-d", "--downvote"):
			upvote = False	
			target = arg
		elif opt in ("-u", "--upvote"):
			upvote = True
			target = arg
		elif opt in ("-l", "--limit"):
			limit = int(arg)
        	
	bot = KriegerBot(upvote, target)
	try:
		bot.run(limit)
	except:
		raise
	finally:
		print('All done! Upvoted %d, Downvoted %d!' %(bot.upvoted, bot.downvoted))
	
if __name__ == '__main__':
	target = sys.argv[1:]
	sys.exit(main(target))
