"""Core App logic."""
import boto3
from botocore.exceptions import ClientError

import lambdalogging

import config

LOG = lambdalogging.getLogger(__name__)
LAMBDA_CLIENT = boto3.client('lambda')

MAX_ITEMS = 100
NUMBER_OF_VERSIONS_TO_KEEP = 10
VERSIONS_KEY = 'Versions'
SORT_KEY = 'LastModified'
LATEST_VERSION = '$LATEST'


def list_function_versions():
    """List versions of function."""
    try:
        function_versions = LAMBDA_CLIENT.list_versions_by_function(
            FunctionName=config.FUNCTION_ARN,
            MaxItems=MAX_ITEMS
        )
    except ClientError as e:
        LOG.info('Following error occured. %s', e)
        return None
    return function_versions


def versions_to_delete(function_versions):
    """Identify versions to delete."""
    versions = function_versions[VERSIONS_KEY]
    versions_count = len(versions)
    LOG.info('Lambda function has %s versions', versions_count)

    if versions_count <= NUMBER_OF_VERSIONS_TO_KEEP:
        LOG.info('Ignoring since the function has less than %s versions', NUMBER_OF_VERSIONS_TO_KEEP)
        return None
    else:
        # Delete 10 versions or (Total Number of versions - 10 ) whichever is lower
        num_of_versions_to_delete = NUMBER_OF_VERSIONS_TO_KEEP
        if versions_count - NUMBER_OF_VERSIONS_TO_KEEP <= NUMBER_OF_VERSIONS_TO_KEEP:
            num_of_versions_to_delete = versions_count - NUMBER_OF_VERSIONS_TO_KEEP

        LOG.info('Deleting %s versions', num_of_versions_to_delete)
        # Fetch oldest versions to delete
        oldest_versions = sorted(versions, key=lambda version: version[SORT_KEY])
        # exclude latest version
        oldest_versions = [version for version in oldest_versions if version['Version'] != LATEST_VERSION]
        versions_to_delete = oldest_versions[:num_of_versions_to_delete]
        version_numbers_to_delete = [version['Version'] for version in versions_to_delete]
        return version_numbers_to_delete


def delete_function_version(version):
    """Delete versions of a function."""
    LOG.info('Deleting version number: %s', version)
    delete_response = LAMBDA_CLIENT.delete_function(
        FunctionName=config.FUNCTION_ARN,
        Qualifier=version
    )
    return delete_response
