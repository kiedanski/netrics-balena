rm -rf lambda_function.zip
rm -rf lib

python3 -m pip install -t lib aws-psycopg2
cd lib && zip ../lambda_function.zip -r . && cd ..
zip lambda_function.zip -u main.py ping.py speed.py utils.py latencyload.py
