import os

PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'bitvid.db'),
    }
}

try:
	from awsinfo import AWS_ACCESS,AWS_SECRET
except:
	print "="*80
	print "WARNING: NO AWS CREDENTIALS GIVEN! Video Upload/View will not work"
	print "="*80
	AWS_ACCESS = ''
	AWS_SECRET = ''