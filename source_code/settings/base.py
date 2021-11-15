import os

# Repo dir
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
SOURCE_CODE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

DOMAIN_DIR = os.path.join(SOURCE_CODE_DIR, '/domain')
INFRA_DIR = os.path.join(SOURCE_CODE_DIR, '/infrastructure/')
CONFIG_DIR = os.path.join(SOURCE_CODE_DIR, '/infrastructure/config')
APPLICATION_DIR = os.path.join(SOURCE_CODE_DIR, '/application')

TEST_DIR = os.path.join(SOURCE_CODE_DIR, '/test')
UNIT_TEST_DIR = os.path.join(SOURCE_CODE_DIR, '/test/unit')
FUNCTIONAL_TEST_DIR = os.path.join(SOURCE_CODE_DIR, '/test/functional')

#Data set columns
RAW_RANDOM_COL = 'RANDOM'

