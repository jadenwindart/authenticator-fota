class Config(object):
    SECRET_KEY = "niIqWeKnYIijFfmp5LDJDkKJoC_eYEwJ6RTckojWl3E"
    POSTGRES_USER = "jlsrslgzboshqr"
    POSTGRES_PW = "995f1afd463ab357c001ce5eed50561f751612b63a6b06ad45c7292f728c3708"
    POSTGRES_DB = "dc2u0ijmqe41u3"
    POSTGRES_URL = "ec2-54-174-229-152.compute-1.amazonaws.com"
    POSTGRES_PORT = "5432"
    SQLALCHEMY_DATABASE_URI = 'postgres://{user}:{pw}@{url}:{port}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB,port=POSTGRES_PORT)
    # SQLALCHEMY_DATABASE_URI = 'postgres://jlsrslgzboshqr:995f1afd463ab357c001ce5eed50561f751612b63a6b06ad45c7292f728c3708@ec2-54-174-229-152.compute-1.amazonaws.com:5432/dc2u0ijmqe41u3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False