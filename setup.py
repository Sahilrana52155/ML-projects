from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of requirements.

    Args:
        file_path (str): Path to the requirements file.

    Returns:
        List[str]: A list of package requirements.
    """
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            # Clean up requirements by stripping newlines and whitespaces
            requirements = [req.strip() for req in requirements]
            # Remove the editable install flag if present
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please provide a valid requirements file.")
        raise
    return requirements

setup(
    name='ML project',
    version='0.0.1',
    author='Sahil Rana',
    author_email='rana52155@gmail.com',
    packages=find_packages(),  # Corrected argument name
    install_requires=get_requirements('requirements.txt')  # Fixed typo
)
