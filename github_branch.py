import requests

def get_default_branch(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        # "Authorization": "token your_token",  # Uncomment and replace with your token if you have one
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
        print(f"Failed to get repository details. Status code: {response.status_code}")
