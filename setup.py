from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    return requirements

requirements = get_requirements('requirements.txt')
dependency_links = [req for req in requirements if req.startswith(HYPEN_E_DOT)]
install_requires = [req for req in requirements if not req.startswith(HYPEN_E_DOT)]

setup(
    name='mlproject',
    version='0.0.1',
    author='Shubham Kumar',
    author_email='shubhamkumarbaranwal782@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=dependency_links
)
