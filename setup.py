# setup.py : 
''' It helps in automatically discovering and including 
    all packages (directories with an __init__.py file) 
    in your project for distribution.
'''

from setuptools import find_packages, setup


'''
Using find_packages simplifies the setup process, especially 
for projects with many packages, ensuring that all necessary 
code is included in the distribution package. It's a handy tool 
for automating the packaging process in Python.
'''

from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements in requirements.txt file
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
    
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'sumit',
    author_email = 'rsumit31@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    )

# instead of wiriting this:
# install_requires = get_requirements('requirements.txt')
# You can also write this:
# install_requires = ['numpy', 'pandas', 'scikit-learn', 'matplotlib']