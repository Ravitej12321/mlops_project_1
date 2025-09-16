from setuptools import setup,find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name = 'MLops_project_1',
    version = "0.1",
    author = 'Ravi Teja',
    package = find_packages(),
    install_requires = requirements

)