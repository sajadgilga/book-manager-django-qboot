import datetime
import json

from books.models import Book


class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {'id': obj.id, 'name': obj.name, 'created_date': obj.created_date,
                    'modified_date': obj.modified_date}
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)
