from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    
name='Analysis-Model',
version='0.1.0',
packages=find_packages(),
author_email = 'eg244916@engug.ruh.ac.lk',
author = 'eg244916',
install_requires=get_requirements('requirements.txt')
)