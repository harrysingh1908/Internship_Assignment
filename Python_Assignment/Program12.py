import re

def extract_emails_and_phones(file_path):
   
    # Regular expression patterns for emails and Indian phone numbers
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+91[789]\d{9}'

    with open(file_path, 'r') as file:
        content = file.read()

    emails = re.findall(email_pattern, content)
    phones = re.findall(phone_pattern, content)

    return emails, phones

# Example usage
file_path = 'example.txt'  
emails, phones = extract_emails_and_phones(file_path)
print("Emails found:", emails)
print("Phone numbers found:", phones)
