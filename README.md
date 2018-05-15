psql --host=postgressql-cryptocurrency.cibilq8azida.us-east-2.rds.amazonaws.com --port=5432 --username=acms_user --password --dbname=CryptocurrencyDb

Commands in Localhost:

~/Cryptocurrency_DataLoader/redis-3.2.1/src/redis-server

~/.virtualenvs/celery_env/bin/celery beat -A app.celery --schedule=/tmp/celerybeat-schedule --loglevel=INFO --pidfile=/tmp/celerybeat.pid

~/.virtualenvs/celery_env/bin/celery worker -A app.celery --loglevel=INFO


Data Loader (AWS Server)

ssh -i "pythonkeypair.pem" ec2-user@ec2-18-188-185-99.us-east-2.compute.amazonaws.com

source ~/.virtualenvs/celery_env/bin/activate

scp -i pythonkeypair.pem CryptoCurrency_Dataloader.tar.gz ec2-user@ec2-18-188-185-99.us-east-2.compute.amazonaws.com:~/.

nohup ~/.virtualenvs/celery_env/bin/celery worker -A app.celery --loglevel=INFO &

nohup ~/.virtualenvs/celery_env/bin/celery beat -A app.celery --schedule=/tmp/celerybeat-schedule --loglevel=INFO --pidfile=/tmp/celerybeat.pid &

nohup ~/Cryptocurrency_DataLoader/redis-3.2.1/src/redis-server &

Api

ssh -i "pythonkeypair.pem" ec2-user@ec2-18-218-241-79.us-east-2.compute.amazonaws.com

scp -i pythonkeypair.pem ~/flask_app/flask-env/acms/requirements.txt ec2-user@ec2-18-218-241-79.us-east-2.compute.amazonaws.com:~/.

scp -i pythonkeypair.pem ~/flask_app/flask-env/acms/api.py ec2-user@ec2-18-218-241-79.us-east-2.compute.amazonaws.com:~/.

API 
http://ec2-18-218-241-79.us-east-2.compute.amazonaws.com/login
method : post
parameter
{
 "email":"urja123@gmail.com",
 "password":"12345"
}
{
 "userid":2,
 "type":"MARKETCAP_ALERT",
 "currency_symbol":"BTC",
 "conversion_symbol":"USD",
 "marketcap":1235,
 "marketcap_inc_by":11.33,
 "marketcap_dec_by":11.22
}


http://ec2-18-218-241-79.us-east-2.compute.amazonaws.com/registeration
method:post
{
    "email":"urjakothari5@gmail.com",
    "password":"12345",
    "name":"urja"
}
