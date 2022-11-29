#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app, storage
logging.basicConfig(filename="log.txt",level=logging.DEBUG)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iiitapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


basepath = os.path.abspath(os.path.dirname(__file__))

# Initialize Firestore DB
try:
    cred = credentials.Certificate(os.path.join(basepath,'config', 'serviceAccountKey.json'))
    firebase_admin.initialize_app(cred, {'storageBucket': 'iitm-f916f.appspot.com'})

    db = firestore.client()
    bucket = storage.bucket()
    print("---------------------------> IN <--------------------------")
except Exception as e:
    print(e)
    print("--------------------------------------> Not Logged in !")

if __name__ == '__main__':
    main()
