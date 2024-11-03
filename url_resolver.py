import requests

import pandas as pd

def get_final_url(url):
    response = requests.get(url, allow_redirects=True)
    return response.url

repo_df = pd.read_csv("../resources/projects_with_default_branch.csv")

from tqdm import tqdm

tqdm.pandas()

repo_df['url'] = repo_df['url'].progress_apply(get_final_url)

repo_df.to_csv("../resources/projects_with_final_url.csv", index=False)