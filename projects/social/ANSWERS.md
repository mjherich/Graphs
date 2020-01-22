# 3. Questions

1. To create 100 users with an average of 10 friends each, how many times would you need to call `add_friendship()`? Why?

- The number of times `add_friendship()` must be called is equal to `(num_users * avg_friendships) / 2`. We divide by two because `add_friendship()` in effect adds 2 friendships per call.

2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?

- Percentage of entire userbase in a user's extended network is ~99%
- The average degree of separation in a user's extended network is ~6. It's a well known phenomenom that entities in a network are six or fewer connections from each other (see https://en.wikipedia.org/wiki/Six_degrees_of_separation).