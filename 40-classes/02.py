class Comment:
    total_comments = 0

    def __init__(self, comment, initial_votes=0):
        self.text = comment
        self.votes = initial_votes
        Comment.total_comments += 1

    def upvote(self, votes=1):
        self.votes += votes

    def reset_votes(self):
        self.votes = 0

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"


my_comment = Comment('Hello World', 10)

print(my_comment.text)
print(my_comment.votes)

my_comment.upvote()

print(my_comment.votes)

my_comment.upvote(5)
print(my_comment.votes)

print(my_comment)
print(type(my_comment))
print(my_comment.__dict__)
print(dir(my_comment))

my_comment.reset_votes()

print(my_comment.votes)

merged_comment = Comment.merge_comments('Great!', 'OK')
print(merged_comment)

merged_comment_2 = my_comment.merge_comments('Thanks!', 'Good!')
print(merged_comment_2)

second_comment = Comment('Hello World 2')

print(Comment.total_comments)
