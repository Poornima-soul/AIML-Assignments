'''
Explanation (KNN in Real Life)

K-Nearest Neighbors (KNN) is a machine learning algorithm that works by finding the most similar data points (neighbors) and making predictions based on them.

In real life, platforms like Netflix or online shopping websites use similar techniques to recommend movies or products. If two users have similar watching history or ratings, the system recommends movies liked by one user to the other.

For example, if User A and User B both like action and thriller movies, and User A watches a new action movie, the system may recommend that movie to User B because their interests are similar.

Interpretation

The smaller distance means higher similarity.
Here, User2 is more similar to User1 than User3. Therefore, movies liked by User2 can be recommended to User1.
'''

#similar Example
# Example dataset of users and movie ratings

users = {
    "User1": [5, 4, 0, 3],
    "User2": [4, 5, 1, 2],
    "User3": [1, 2, 5, 4]
}

target_user = users["User1"]

# Calculate similarity using simple distance
for user, ratings in users.items():
    if user != "User1":
        distance = 0
        for i in range(len(ratings)):
            distance += (ratings[i] - target_user[i]) ** 2

        print("Distance between User1 and", user, "=", distance)