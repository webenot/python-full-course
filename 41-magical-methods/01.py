class Comment:
    total_comments = 0

    def __init__(self, comment, initial_votes=0):
        self.text = comment
        self.votes = initial_votes
        Comment.total_comments += 1

    def __add__(self, other):
        return {
            'text': f"{self.text} {other.text}",
            'total_votes': self.votes + other.votes
        }

    def __eq__(self, other):
        return self.text == other.text and self.votes == other.votes

    def upvote(self, votes=1):
        self.votes += votes


first_comment = Comment("First comment")
first_comment.upvote()
second_comment = Comment("Second comment")
second_comment.upvote()

print(first_comment + second_comment)
print(first_comment == second_comment)
