import pandas as pd
from repo_mapper import get_repo, get_repo_search_term
import logging
from githubfilepuller import get_file_url
from tqdm import tqdm
import sys

# Load dataset
df = pd.read_csv("./resources/RemainingTS.csv")

# Set up logging
logging.basicConfig(
    filename='error_log.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to get URLs
def get_response(project: str, test_case: str):
    try: 
        branch, owner, name = get_repo(get_repo_search_term(project))
        test_file_name, _ = test_case.split('.')[-2:]
        test_file_url = get_file_url(owner, name, test_file_name, branch)

        if name == 'timely' : actual_file_name =  test_file_name[:-2]
        else : actual_file_name = test_file_name.replace('test', '')

        actual_file_url = get_file_url(owner, name, actual_file_name, branch)
        return test_file_url, actual_file_url
    except Exception as e:
        logging.error(f"Error processing project '{project}' and test case '{test_case}': {e}")
        return None, None

# Set up tqdm
tqdm.pandas()

# Parameters for chunking
num_chunks = 20
chunk_size = len(df) // num_chunks
output_file = './resources/remaining_ts_output.csv'

# Initialize output CSV with headers from the first chunk if the file doesn't exist
try:
    open(output_file, 'x').close()
    df.iloc[:0].to_csv(output_file, index=False)
except FileExistsError:
    pass  # Skip if file already exists


# Get the starting row from command-line arguments
start_row = int(sys.argv[1]) if len(sys.argv) > 1 else 0

# Calculate the chunk to start from
start_chunk = start_row // chunk_size


# Process each chunk and append results
for i in range(start_chunk, num_chunks):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_chunks - 1 else len(df)  # Last chunk may be slightly larger

    # Slice the DataFrame chunk
    df_chunk = df.iloc[start:end].copy()

    # Process the chunk
    df_chunk[['test_file_url', 'actual_file_url']] = df_chunk.progress_apply(
        lambda row: get_response(row['idProject'], row['testCase']),
        axis=1,
        result_type='expand'
    )

    # Append chunk to the CSV file
    df_chunk.to_csv(output_file, mode='a', header=False, index=False)

    print(f"Completed and saved chunk {i+1}/{num_chunks}")