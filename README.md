## About

sample app to set up asynchronous lambda for Amazon API Gateway.

## Deploy

```
$ serverless install -u https://github.com/quiver/aws-api-gateway-async-lambda-sample
$ cd aws-api-gateway-async-lambda-sample
$ serverless deploy
```

## Measure response time

```
# sync invocation
$ time curl -s -o /dev/null https://XXX.execute-api.ap-northeast-1.amazonaws.com/dev/sync
curl -s -o /dev/null   0.01s user 0.01s system 0% cpu 3.166 total

# async invocation
$ time curl -s -o /dev/null https://XXX.execute-api.ap-northeast-1.amazonaws.com/dev/async
curl -s -o /dev/null   0.02s user 0.01s system 15% cpu 0.153 total
```

## Requirements

- [serverless framework](https://serverless.com/)

## Ref

- [Set up asynchronous invocation of the backend Lambda function - Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-integration-async.html)
