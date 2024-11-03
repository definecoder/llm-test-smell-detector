import pandas as pd
repo_df = pd.read_csv('./resources/projects_with_default_branch.csv')
repo_list = repo_df[['url', 'default_branch']].values.tolist()

print(repo_list)