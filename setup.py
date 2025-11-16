from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    This Function wil return the list of requirement 

    '''
    requirements = [] 
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    # return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
setup(
    name="mlproject",
    version="0.0.1",
    author="Aarav",
    author_email="aaravku7654@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
  