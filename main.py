"""

    """

import json
from pathlib import Path
import subprocess

from giteasy.github_releases import \
    download_latest_release_of_public_github_repo
from giteasy import GitHubRepo


def main() :

    pass

    ##
    fp = 'conf.json'
    with open(fp) as f :
        js = json.load(f)

    rp_url = js['repo_url']
    ghr = GitHubRepo(rp_url)
    print(rp_url)

    ##
    download_latest_release_of_public_github_repo(rp_url)

    ##
    pyv = js['python-version']
    print("Python version:" , pyv)

    subprocess.run(['pyenv' , 'install' , '--skip-existing' , pyv])

    subprocess.run(['pyenv' , 'virtualenv' , pyv , ghr.repo_name])

    print(ghr.repo_name)

    ##

    ##

##


if __name__ == '__main__' :
    main()
    print(f'{Path(__file__).name} Done!')

##
import subprocess


subprocess.run(['pyenv' , 'virtualenv' , '3.10.5' , 'giteasy'])

##
