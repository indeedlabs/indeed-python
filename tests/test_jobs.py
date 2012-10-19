from nose.tools import *
import json
from xml.dom.minidom import parseString
from indeed import IndeedClient, IndeedClientException

class TestJobs:

    def setup(self):
        self.client = IndeedClient("YOUR_PUBLISHER_NUMBER")
        self.params = {
            'jobkeys' : ("5898e9d8f5c0593f", "c2c41f024581eae5"),
        }

    def teardown(self):
        self.client = None
        self.params = None

    @with_setup(setup, teardown)
    def test_jobs(self):
        jobs_response = self.client.jobs(**self.params)
        assert type(jobs_response) is dict

    @with_setup(setup, teardown)
    @raises(IndeedClientException)
    def test_missing_jobkeys(self):
        del self.params['jobkeys']
        jobs_response = self.client.jobs(**self.params)

    @with_setup(setup, teardown)
    def test_raw_json(self):
        self.params['raw'] = True
        jobs_response = self.client.jobs(**self.params)
        assert isinstance(jobs_response, basestring)
        assert type(json.loads(jobs_response)) is dict

    @with_setup(setup, teardown)
    def test_raw_xml_with_paramter(self):
        self.params['format'] = "xml"
        self.params['raw'] = True
        jobs_response = self.client.jobs(**self.params)
        assert isinstance(jobs_response, basestring)
        assert parseString(jobs_response)

    @with_setup(setup, teardown)
    def test_raw_xml_without_paramter(self):
        self.params['format'] = "xml"
        jobs_response = self.client.jobs(**self.params)
        assert isinstance(jobs_response, basestring)
        assert parseString(jobs_response)