__all__ = ["config"]

import os
import yaml

this_dir = os.path.dirname(os.path.realpath(__file__))
config_file_path = os.path.join(this_dir, "config.yml")

#Access to API
ENVIRONMENT = os.getenv("ENV_KEY_ACCES",
                         config_file_path
)

with open(ENVIRONMENT, 'r') as file_in:
    config = yaml.safe_load(file_in)