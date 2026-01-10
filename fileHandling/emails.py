import re

def read_email():
    with open('email.txt', 'r') as file:
        return file.read()


def email_sender():
    text = read_email()
    match = re.search(r'^From:.*<([^>]+)>', text, re.MULTILINE)
    return match.group(1) if match else None


def email_recipient():
    text = read_email()
    match = re.search(r'^To:.*<([^>]+)>', text, re.MULTILINE)
    return match.group(1) if match else None


def email_subject():
    text = read_email()
    match = re.search(r'^Subject:\s*(.+)', text, re.MULTILINE)
    return match.group(1) if match else None


def email_body():
    text = read_email()
    match = re.search(r'\n\n(.*)', text, re.DOTALL)
    return match.group(1).strip() if match else None