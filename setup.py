from setuptools import find_packages,setup
from typing import List

# HYPEN_E_DOT ='- e .'

def get_requirements(file_path:str)->List[str]:
    ''' This Function will return the List of requirements   '''
    requirements = []  # it will store the all the list of libraries 
        
    with open(file_path) as file_obj:   # frist we have to read the file 
        requirements= file_obj.readlines() # line by line read the libraries 
        requirements = [req.replace('\n',"") for req in requirements]  # it will read the libraries line by line & then replace the /n value to "_blank"
    
        # if HYPEN_E_DOT in requirements:
        #     requirements.remove(HYPEN_E_DOT)    
    
    return requirements # then print the requirements in append then in empty requirements = [',',',']


setup(
    name = 'mlproject',
    version = '0.0.1',
    author =  'chetan',
    authoremail = 'chetanchaudhari90014@gmail.com',
    packages =  find_packages(),
    install_requires =  get_requirements('requirements.txt')
)