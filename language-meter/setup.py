from setuptools import setup, find_packages

setup(name='language-meter',
    description='Twitter API Pipeline',
    url='https://github.com/justinschuster/twitter-pipeline',
    author='Justin Schuster',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    license='MIT',
    python_requires='>3.3',
    packages=find_packages(),
    scripts=['lambda_function/fetch_tweets.py']
)