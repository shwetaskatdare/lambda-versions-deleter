# lambda-versions-deleter

A serverless app could have multiple lambda functions. With continuous deployments, new versions of lambda functions get created, and there is a possibility that certain functions in your app could hit AWS Lambda's [function memory allocation limit](https://docs.aws.amazon.com/lambda/latest/dg/limits.html) causing deployment failures. To prevent this from happening, here is a Serverless App that you can nest in your existing app which will clean up older versions of a lambda function on a custom schedule.

## App Architecture

![Lambda-Versions-Deleter](https://github.com/shwetaskatdare/lambda-versions-deleter/raw/master/images/lambda-versions-deleter-new.png)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login
1. Go to the app's page on the [Serverless Application Repository](TODO) and click "Deploy"
1. Provide the required app parameters (see parameter details below) and click "Deploy"

## App Parameters

1. `LogLevel` (optional) - Log level for Lambda function logging, e.g., ERROR, INFO, DEBUG, etc. Default: INFO
1. `FunctionArn` (required) - Specify ARN of a Lambda function for which you want the versions to be deleted
1. `LambdaExectionSchedule` (required) - Specify the schedule expression to invoke LambdaVersionsDeleter using https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html. Default: Scheduled to run once everyday at 12 pm UTC.

## App Outputs

1. `LambdaVersionsDeleter` - Lambda Versions deleter.
1. `LambdaVersionsDeleterArn` - Lambda Versions deleter ARN.

## License Summary

This code is made available under the TODO license. See the LICENSE file.
