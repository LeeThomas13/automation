from faker import Faker
import re

email_regex = 'r"(\w*?)(@\w*?)\.(\w{3})"gm'

phone_regex = 'r"\(?\d{3}\)?[-\s.]?\d{3}[-\s.]?\d{4}"gm'

fake = Faker('en_US')

def find_emails(input):
    x = re.search(open_file_get_string(email_regex))
    if x:
        #open email txt file and push regex matches into it

def find_phone_numbers(input):
    x = re.search(open_file_get_string(phone_regex))
    if x:
        #open phone numbers txt file and push regex matches into it

def open_file_get_string(regex_search)
with open("../potential-contacts.txt", 'w') as f:
    f.write(potential_contacts)

