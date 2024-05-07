def is_user_authenticated():
    return True


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print('User is authenticated')
            return fn(*args, **kwargs)
        raise Exception('User is NOT authenticated')
    return wrapper


@check_user_auth
def do_sensitive_jobs():
    # Do something only if user is authenticated
    print("Results of some sensitive tasks")


try:
    do_sensitive_jobs()
except Exception as e:
    print(e)
