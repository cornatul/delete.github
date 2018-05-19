#Welcome to multiple delete python
import os
import requests
from github import Github

# using username and password
github = Github("username","token")

token = '' # token needs delete_repo permission
organization = '' # or user
url = 'https://api.github.com/repos/{}'.format(organization)
headers = {'Accept': 'application/vnd.github.v3+json',
           'Authorization': 'token {}'.format(token)}



# list with repositories that you dont want to delete
dont_delete = [

];




def delete(dont_delete):

   	repositories =[];

   	for repo in github.get_user().get_repos():
   		repositories.append(repo.name)
   		
   	for name in repositories:
   		
   		if name not in dont_delete:
   			myrequest = requests.delete(os.path.join(url, name), headers=headers)




# Start the program
delete(dont_delete)