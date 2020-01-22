import random
import names
import itertools
from util import Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        if num_users < avg_friendships:
            raise Exception("num_users must be greater than avg_friendships")
        # Add users
        for _ in range(num_users):
            # Add a user with a random name
            self.add_user(names.get_full_name())
            
        # Create friendships
        combos = list(itertools.combinations(self.users.keys(), 2))
        # Shuffle all potential friendships
        random.shuffle(combos)
        i = 0
        combo_i = 1
        while i <= (num_users * avg_friendships)/2:
            user_id, friend_id = combos[combo_i]
            if friend_id not in self.friendships[user_id]:
                self.add_friendship(user_id, friend_id)
                i += 1
            combo_i += 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # The shortest path to the input is trivial
        visited[user_id] = [user_id]
        # Create a queue for storing user_ids to traverse
        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            user_path = q.dequeue()
            last_user = user_path[-1]
            for friend in self.friendships[last_user]:
                if friend not in visited:
                    new_path = list(user_path) + [friend]
                    q.enqueue(new_path)
                    visited[friend] = new_path
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f"Friendships: {sg.friendships}")
    connections = sg.get_all_social_paths(1)
    print(f"Connections: \n {connections}")
