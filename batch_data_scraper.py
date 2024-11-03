import pandas as pd
import logging
from concurrent.futures import ThreadPoolExecutor
from repo_mapper import get_repo, get_repo_search_term
from githubfilepuller import get_file_url
from tqdm import tqdm

# Set up error logging configuration
logging.basicConfig(
    filename='error_log.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

df = pd.read_csv("./resources/entireDataset.csv")

def get_response(project: str, test_case: str):
    try: 
        branch, owner, name = get_repo(get_repo_search_term(project))
        test_file_name, _ = test_case.split('.')[-2:]

        test_file_url = get_file_url(owner, name, test_file_name, branch)
        actual_file_name = test_file_name.replace('test', '')
        actual_file_url = get_file_url(owner, name, actual_file_name, branch)

        return test_file_url, actual_file_url
    except Exception as e:
        logging.error(f"Error processing project '{project}' and test case '{test_case}': {e}")
        return None, None

# Define a function to apply get_response in parallel
def process_row(row):
    return get_response(row['idProject'], row['testCase'])

# Run parallel processing with a progress bar
with ThreadPoolExecutor() as executor:
    results = list(tqdm(executor.map(process_row, [row for _, row in df.iterrows()]), total=len(df)))

# Add the results back to the DataFrame
df[['test_file_url', 'actual_file_url']] = pd.DataFrame(results, columns=['test_file_url', 'actual_file_url'])

# Save the DataFrame with URLs
df.to_csv('./resources/entireDataset_with_urls.csv', index=False)
