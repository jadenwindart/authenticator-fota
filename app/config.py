class Config(object):
    POSTGRES_USER = "jlsrslgzboshqr"
    POSTGRES_PW = "95f1afd463ab357c001ce5eed50561f751612b63a6b06ad45c7292f728c3708"
    POSTGRES_DB = "dc2u0ijmqe41u3"
    POSTGRES_URL = "ec2-54-174-229-152.compute-1.amazonaws.com"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATION = False