from flask_restplus import fields
from app.api.restplus import api

entry = api.model('entry', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an entry'),
    'title': fields.String(required=True, description='title'),
    'body': fields.String(required=True, description='content')
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_entries = api.inherit('Page of blog entries', pagination, {
    'items': fields.List(fields.Nested(entry))
})
