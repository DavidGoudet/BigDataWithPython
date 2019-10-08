#Part of a Course from Hezion Studios on Big Data: Trinity

from twitterscraper import query_tweets
from twitterscraper import query_user_info

sum_of_users=0
users_reached = 0

for tweet in query_tweets("Trump", 100, poolsize=1)[:100] :
    user = query_user_info(user= tweet.username)
    if user is not None:
      sum_of_users += user.followers
      users_reached += 1
      
print("Average followers: "+str(sum_of_users/users_reached))