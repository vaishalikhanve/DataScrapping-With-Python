from github import Github #from PyGithub lib (pip install PyGithub)
g = Github("user_name", "password")
g = Github("access_token")
g = Github(base_url="url",token="access_token")
repos=g.search_repositories(query='game+engine+language:c++')
for repo in repos:
    print(repo) 
