import pytest
import lambdaversionsdeleter


def test_handler(mocker):
    lambdaversionsdeleter.handler({}, None)
