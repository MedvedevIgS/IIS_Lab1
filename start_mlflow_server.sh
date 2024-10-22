export $(cat ./.env | xargs)

export MLFLOW_S3_ENDPOINT_URL=https://my.mlflow.storage.ru
export AWS ACCESS KEY _ID=$AWS ACCESS KEY ID
export AWS SECRET ACCESS KEY=$AWS SECRET ACCESS KEY
export AWS BUCKET NAME=$S3_BUCKET NAME

mlflow server \
    --registry-store-uri  postgresql://$DB_DESTINATION_USER:$DB_DESTINATION_PASSWORD@$DB_DESTINATION_HOST:$DB_DESTINATION_PORT/$DB_DESTINATION_NAME \
    --backend-store-uri postgresql://$DB_DESTINATION_USER:$DB_DESTINATION_PASSWORD@$DB_DESTINATION_HOST:$DB_DESTINATION_PORT/$DB_DESTINATION_NAME \
    --default-artifact-root s3://$AWS_BUCKET_NAME \
    --no-serve-artifacts \
    --host 0.0.0.0
    --port 5555