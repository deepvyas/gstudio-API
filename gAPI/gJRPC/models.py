from django.db import models
from django_mongokit import connection
from django_mongokit.document import DjangoDocument
from datetime import datetime
from mongokit import IS
from mongokit import OR
from mongokit import INDEX_ASCENDING, INDEX_DESCENDING

@connection.register
class DataMe(DjangoDocument):
    collection_name = 'my_iol'
    structure = {
            'name':unicode,
            'surname':unicode,
            'ur_str':unicode,
            'date_creation':datetime,
    }
    required_fields = ['name','surname', 'date_creation']
    default_values = {'ur_str': 'qwerty', 'date_creation':datetime.utcnow}