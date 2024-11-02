import pandas as pd
from repo_mapper import get_repo, get_repo_search_term
import logging
from github_branch import get_default_branch
from githubfilepuller import get_file_url
from url_resolver import get_final_url
df = pd.read_csv("./resources/entireDataset.csv")

logging.basicConfig(
    filename='error_log.log',      # Log file name
    level=logging.ERROR,           # Log only ERROR level messages
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def get_response(project: str, test_case: str):
    try: 
        
        url, _, _ = get_repo(get_repo_search_term(project))
        url = get_final_url(url)
        owner, name = url.split('/')[-2:]
        branch = get_default_branch(owner, name)
        # print("owner:", owner)
        # print("name:", name)
        # print("branch:", branch)

        test_file_name, _ = test_case.split('.')[-2:]

        # print("test file name:", test_file_name)

        test_file_url = get_file_url(owner, name, test_file_name, branch)

        actual_file_name = test_file_name.replace('test', '')

        # print("actual file name:", actual_file_name)

        actual_file_url = get_file_url(owner, name, actual_file_name, branch)

        return test_file_url, actual_file_url
    except Exception as e:
        # write a log file
        logging.error(f"Error processing project '{project}' and test case '{test_case}': {e}")
        return None, None
    




# print(get_response(df.iloc[0]['idProject'], df.iloc[0]['testCase']))

from tqdm import tqdm

tqdm.pandas()
df[['test_file_url', 'actual_file_url']] = df.progress_apply(
    lambda row: get_response(row['idProject'], row['testCase']),
    axis=1,
    result_type='expand'
)

df.to_csv('./resources/entireDataset_with_urls.csv', index=False)





