from setuptools import setup,find_packages
from typing import List

HYPE='-e .'
def get_package(file_path: str) -> List[str]:
    """
    This code is getting the packages

    """
    requiremnets=[]
    with open(file_path) as file_obj:
        requiremnets=file_obj.readlines()
        requiremnets=[req.replace("/n",' ') for req in requiremnets]
    
        if HYPE in requiremnets:
            requiremnets.remove(HYPE)

    return requiremnets


setup(
    name='heartprediction',
    version='0.0.1',
    author_email='girishkrish1998yuv@gmail.com',
    author='Girish',
    packages=find_packages(),
    install_requires=get_package('requirements.txt')

    )