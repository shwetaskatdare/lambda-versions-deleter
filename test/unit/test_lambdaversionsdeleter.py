import pytest
import lambdaversionsdeleter

import core

def test_handler(mocker):
    mocker.patch.object(core, 'list_function_versions')
    mocker.patch.object(core, 'versions_to_delete', return_value=[1, 2, 3])
    mocker.patch.object(core, 'delete_function_version')

    lambdaversionsdeleter.handler({}, None)
    
    core.list_function_versions.assert_called_once()
    core.versions_to_delete.assert_called_once()

    core.delete_function_version.assert_any_call(1)
    core.delete_function_version.assert_any_call(2)
    core.delete_function_version.assert_any_call(3)

def test_handler_delete_not_called(mocker):
    mocker.patch.object(core, 'list_function_versions')
    mocker.patch.object(core, 'versions_to_delete', return_value=None)
    mocker.patch.object(core, 'delete_function_version')

    lambdaversionsdeleter.handler({}, None)
    
    core.list_function_versions.assert_called_once()
    core.versions_to_delete.assert_called_once()

    core.delete_function_version.assert_not_called()
    