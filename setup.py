import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'ete_text_summerizer_k'
AUTHER_USER_NAME = 'XMan'
SRC_REPO = 'textSummarizer'
AUTHER_EMAIL = 'xman@gmail.com'


setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author = AUTHER_USER_NAME,
    author_email= AUTHER_EMAIL,
    description= 'A small python package for CNN app',
    long_description= long_description,
    long_description_content_type= 'text/markdown',
    url= f"https://github.com{AUTHER_USER_NAME}/{REPO_NAME}",
    project_url = {
        'Bug Tracker': f'https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir= {'': 'src'},
    packages = setuptools.find_packages(where='src')
)