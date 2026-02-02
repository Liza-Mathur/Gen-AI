from email import policy
from email.parser import BytesParser

def load_email_from_eml(path):
    with open(path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_content()
    else :
        return msg.get_content()
