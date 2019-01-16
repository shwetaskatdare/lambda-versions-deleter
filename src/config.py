"""Environment configuration values used by lambda functions."""

import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
FUNCTION_ARN = os.getenv('FUNCTION_ARN')
