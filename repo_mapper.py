import pandas as pd
repo_df = pd.read_csv('../resources/projects_with_final_url.csv')
repo_list = repo_df[['url', 'default_branch']].values.tolist()

def get_repo_search_term(idProject: str):
    search_term = idProject.split('_')[-1]
    return search_term


def get_repo(search_term):
    for url, branch in repo_list:
        if search_term in url:
            owner, name = url.split('/')[-2:]
            return branch, owner, name
    return None


# print(get_repo(get_repo_search_term('21_incubator-dubbo')))


