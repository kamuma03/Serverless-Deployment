import json
import sklearn
import boto3
import os
import pickle
from sklearn.ensemble import RandomForestClassifier

# Setting up the environment for the model and appropriate paths
s3 = boto3.client('s3')
s3_bucket = os.environ['s3_bucket']
classifier_model = os.environ['model_name']
temp_path = '/tmp/' + classifier_model

# definition of the lambda handler function
def lambda_handler(event, context):
    
    print(event)

    # Parse input
    body = event['body']
    print(body)

    data = json.loads(body)['data']
    data = float(data)
    print(data)
    
    # Download pickled model from S3 and unpickle
    s3.download_file(s3_bucket, classifier_model, temp_path)
    with open(temp_path, 'rb') as f:
        classifier = pickle.load(f)

    # Prediction of the class 
    class_prediction = classifier.predict([[data]])[0]
    print(class_prediction)

    # Return json message
    return {
        "statusCode": 200,
        "body": json.dumps({
            "prediction": str(class_prediction),
        }),
    }
