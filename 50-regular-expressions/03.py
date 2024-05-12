import re

def check_email(email):
    email_regexp = r'^[a-zA-Z0-9_\-.\+]+@[a-zA-Z0-9_\-.]+\.[a-zA-Z0-9_.]+$'
    email_check_pattern = re.compile(email_regexp)
    validation_result = 'valid' if email_check_pattern.fullmatch(email)\
        else 'invalid'
    return (email, validation_result)

email = 'test-test+122@example.sub.com'

print(check_email(email))

bad_email = '@example.sub.com'
print(check_email(bad_email))
