import os
os.environ.setdefault('IP', '0.0.0.0')
os.environ.setdefault('PORT', '5000')
os.environ.setdefault('SECRET_KEY', '0510') # insert your own secret key
os.environ.setdefault('MONGO_URI', 'mongodb+srv://<Admin1>:<Password2>@bellab1.qpb5aqq.mongodb.net/?retryWrites=true&w=majority') # insert connection string from the steps above
os.environ.setdefault('MONGO_DBNAME', 'BellaB1') # insert your database name

# Further info on setting email server below
os.environ.setdefault('MAIL_SERVER', 'smtp.gmail.com')
os.environ.setdefault('MAIL_PORT', '587')
os.environ.setdefault('MAIL_USERNAME', 'wodoyoailab@gmail.com')
os.environ.setdefault('MAIL_PASSWORD', 'onyango74ai;;;')
os.environ.setdefault('USER_EMAIL_SENDER_EMAIL', 'wodoyoailab@gmail.com')

os.environ.setdefault('DEBUG', 'True') # set to False when deploying to Heroku