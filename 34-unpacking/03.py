user_data = ['Bob', 23]


def user_info(name, comments=0):
    if not comments:
        return f"{name} has no comments"

    return f"{name} has {comments} comments"


print(user_info(*user_data))
