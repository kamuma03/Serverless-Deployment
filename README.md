# Serverless Model Deployment

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- create-model.ipynb - Notebook to create, train and export model.
- classification_model.p - Exported model in pickle.
- model-deployment/code - Code for the application's Lambda function.
- model-deployment/template.yaml - A template that defines the application's AWS resources.
- test.json - json file to test the deployed model.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build your application for the first time, run the following in your shell from the model-deployment folder:

```bash
sam build 
```


To package and save to the given S3 bucket run the following in your shell from the model-deployment\.aws-sam\build folder:

```bash
sam package --template-file template.yaml --s3-bucket xxxxxs3bucket --output-template-file packaged.yaml
```
To deploy run the following in your shell from the model-deployment\.aws-sam\build folder:

```bash
sam deploy --template-file packaged.yaml --stack-name ClassifierLambdaStack --capabilities CAPABILITY_IAM
```

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

To test the deploed model run the following in your shell from the main folder:
```bash
curl -XPOST -g https://API Gateway Endpoint URL -H 'Content-Type:application/json' -d "@test.json"
```


## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.


## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name model-deployment
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
