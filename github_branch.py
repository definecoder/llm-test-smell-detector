import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv('.env.local')
PERSONAL_ACCESS_TOKEN = os.getenv('PERSONAL_ACCESS_TOKEN')




def get_default_branch(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {PERSONAL_ACCESS_TOKEN}"
    }

    # Make the GET request to the GitHub API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Get the default branch
        default_branch = data.get("default_branch")
        # print(f"The default branch for {owner}/{repo} is: {default_branch}")
        return default_branch
    else:
        print(response.content)
        print(f"Failed to get repository details. Status code: {response.status_code}")

repo_df = pd.read_csv('./../resources/projects.csv')
repo_list = repo_df['url'].tolist()
branch_list = []


print(get_default_branch("apache", "dubbo"))

# for repo in repo_list:
#     owner, name = repo.split('/')[-2:]
#     branch = get_default_branch(owner, name)
#     branch_list.append(branch)


# repo_df['default_branch'] = branch_list

# repo_df.to_csv('../resources/projects_with_default_branch.csv', index=False)