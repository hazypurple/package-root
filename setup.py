from setuptools import setup, find_packages

setup(
    name='package-root',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    licence='MIT',
    description='My Function Package for Python',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/hazypurple/package-root',
    author='Shehaam Mahomed',
    author_email='shehaam@gmail.com'
)
