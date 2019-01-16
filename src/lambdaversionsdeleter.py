"""Lambda function handler."""

# must be the first import in files with lambda function handlers
import lambdainit  # noqa: F401

import lambdalogging

import core

LOG = lambdalogging.getLogger(__name__)


def handler(event, context):
    """Delete lambda function versions for the lambda function mentioned in environment variables."""
    LOG.info('Received event: %s', event)
    function_versions = core.list_function_versions()

    if not function_versions:
        LOG.info("Skipping...")
        return

    versions_to_delete = core.versions_to_delete(function_versions)

    if versions_to_delete:
        for version_num in versions_to_delete:
            core.delete_function_version(version_num)
