# S3 to SQL using AWS Lambda

We created a set of lambda functions that are triggered whenever a new .json file is added to
one of the storage buckets. The function transforms the experiment result and stores it on an postgres database.

# Installation

1. Follow the instructions to create a lambda function for S3 triggers. [Link](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html)
2. For the S3 path, choose the subfolder of the experiment: `ping`, `speed`, etc.
3. Build the local code and get a `lambda_function.zip` file.
4. Replace the default function with the zip file.
5. Edit the handler to use `main.<experiment>_handler` with experiment = ping, speed, etc.
6. Set the following environment variables:
    - `DB_USERNAME=`
    - `DB_HOST=<path-to-aws-database>`
    - `DB_PASSWORD=`
    - `DB_PORT=`
    - `DB_NAME`

