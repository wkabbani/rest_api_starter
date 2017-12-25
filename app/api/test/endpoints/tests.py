import logging

from flask import request
from flask_restplus import Resource
from app.api.test.business import create_new_entry
from app.api.test.serializers import entry
from app.api.test.parsers import pagination_arguments
from app.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('tests', description='Operations related to health tests')


@ns.route('/')
class TestsCollection(Resource):

    def get(self):
        """
        Returns list of health tests
        """
        tests = ['database is ok', 'api-1 is ok', 'api-2 is ok']

        return tests

    @api.expect(entry)
    def post(self):
        """
        Creates a new entry
        """
        create_new_entry(request.json)
        return None, 201