import pandas as pd
repo_df = pd.read_csv('./resources/projects.csv')
repo_list = repo_df['url'].tolist()
    

def get_repo_search_term(idProject: str):
    search_term = idProject.split('_')[-1]
    return search_term


def get_repo(search_term):
    
    for repo in repo_list:
        if search_term in repo:
            owner, name = repo.split('/')[-2:]
            return repo, owner, name
    return None


# print(get_repo(get_repo_search_term('21_incubator-dubbo')))


