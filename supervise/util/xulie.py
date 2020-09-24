import decimal
import json

from datetime import datetime, date


class DecimalEncoder(json.JSONEncoder):

    def default(self, o):

        if isinstance(o, decimal.Decimal):
            return float(o)

        super(DecimalEncoder, self).default(o)
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj,decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)
