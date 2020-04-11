import sys
import os
import hashlib
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv('FILEPATH')
username = os.getenv('UNAME')
password = os.getenv('PASSWORD')



projectName = str(sys.argv[1])
os.mkdir(f'{path}{projectName}')
user = Github(username, password).get_user()
repo = user.create_repo(projectName)
print(f'Successfully Created Repo {projectName}')


