from nose.tools import *
import json
from xml.dom.minidom import parseString
from indeed import IndeedClient, IndeedClientException

class TestSearch:

    def setup(self):
        self.client = IndeedClient("YOUR_PUBLISHER_NUMBER")
        self.params = {
            'q' : "python",
            'l' : "austin",
            'userip' : "1.2.3.4",
            'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)",
        }

    def teardown(self):
        self.client = None
        self.params = None

    @with_setup(setup, teardown)
    def test_search(self):
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict

    @with_setup(setup, teardown)
    def test_missing_one_required(self):
        del self.params['l']
        search_response = self.client.search(**self.params)
        assert type(search_response) is dict

    @with_setup(setup, teardown)
    @raises(IndeedClientException)
    def test_missing_both_required(self):
        del self.params['q']
        del self.params['l']
        search_response = self.client.search(**self.params)

    @with_setup(setup, teardown)
    @raises(IndeedClientException)
    def test_missing_userip(self):
        del self.params['userip']
        search_response = self.client.search(**self.params)

    @with_setup(setup, teardown)
    @raises(IndeedClientException)
    def test_missing_useragent(self):
        del self.params['useragent']
        search_response = self.client.search(**self.params)

    @with_setup(setup, teardown)
    def test_raw_json(self):
        self.params['raw'] = True
        search_response = self.client.search(**self.params)
        assert isinstance(search_response, basestring)
        assert type(json.loads(search_response)) is dict

    @with_setup(setup, teardown)
    def test_raw_xml_with_paramter(self):
        self.params['format'] = "xml"
        self.params['raw'] = True
        search_response = self.client.search(**self.params)
        assert isinstance(search_response, basestring)
        assert parseString(search_response)

    @with_setup(setup, teardown)
    def test_raw_xml_without_paramter(self):
        self.params['format'] = "xml"
        search_response = self.client.search(**self.params)
        assert isinstance(search_response, basestring)
        assert parseString(search_response)
