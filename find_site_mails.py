import re
import os

try:
    import requests
    from colorama  import Fore, Back, Style
    import pyfiglet

except ImportError:
    os.system("python.exe -m pip install --upgrade pip")
    os.system("pip install requests")
    os.system("pip install colorama")

class color:
    red = Fore.RED
    green = Fore.GREEN
    bright_style= Style.BRIGHT


banner = pyfiglet.figlet_format("FIND - MAILS")
print(color.green+color.bright_style+banner)
print(color.green+color.bright_style+"TTF present\n")
print("- code by MR. Morningstar")


def find_emails(url):

    try:

        response = requests.get(url)
        response.raise_for_status()
        content = response.text
            
        email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        emails = email_pattern.findall(content)
        unique_emails = list(set(emails))
            
        return unique_emails
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []



url = input(color.red+color.bright_style+"Enter website link: ")
emails = find_emails(url)

for email in emails:
    print("Found emails: ", email)

print("\n\n")
