from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# setup() is the main function used to define your Python package metadata and dependencies
setup(
    # Name of the package
    name='Customer segmentation',
    author='Samuel K C',
    author_email='samuelsam2k27@gmail.com',
    
    # Automatically find all packages (folders containing __init__.py)
    # In my project, 'src' folder contains __init__.py, so it will be included as a package
    packages=find_packages(),
    
    # External dependencies required for this package
    install_requires=get_requirements('requirements.txt')
)
