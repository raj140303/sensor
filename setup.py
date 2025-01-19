from setuptools import find_packages,setup # setuptools  is a package that basically provide a tools for pyhton projects 
from typing import List 

HYPEN_E_DOT="-e."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
    if HYPEN_E_DOT in requirements: 
        requirements.remove(HYPEN_E_DOT)
    return requirements 

setup(
     name = "Fault detection" ,
     version="0.0.1" , 
     author="raj140303" ,
     author_email="=ayush091003@gmail.com" , 
     install_requirements=get_requirements("requirements.txt") , 
     packages=find_packages()
)
# koi bhi package install karna ho to python setup.py install 
