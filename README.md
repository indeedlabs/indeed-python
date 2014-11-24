# indeed-python

A client library for using the Indeed Jobsearch API

## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    $ pip install indeed

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

## API Credentials

The Indeed API needs to be called with your Indeed publisher number. You must pass this
to the `IndeedClient` constructor.

```python
from indeed import IndeedClient

client = IndeedClient(publisher = YOUR_PUBLISHER_NUMBER)
```

If you do not have a publisher number, you can receive one by heading to the
[Indeed Publisher Portal](https://ads.indeed.com/jobroll/xmlfeed).


## Performing a Job Search

```python
from indeed import IndeedClient

client = IndeedClient('YOUR_PUBLISHER_NUMBER')

params = {
    'q' : "python",
    'l' : "austin",
    'userip' : "1.2.3.4",
    'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
}

search_response = client.search(**params)
```

## Retrieving Job Details

```python
from indeed import IndeedClient

client = IndeedClient('YOUR_PUBLISHER_NUMBER')

job_response = client.jobs(jobkeys = ("5898e9d8f5c0593f", "c2c41f024581eae5"))
```

## API Paramaters

### Job Search

**q** - 
Query. By default terms are ANDed. To see what is possible, use our [advanced search](http://www.indeed.com/advanced_search) page to perform a search and then check the url for the q value.

**l** - 
Location. Use a postal code or a "city, state/province/region" combination.

**userip** - 
The IP number of the end-user to whom the job results will be displayed. *This field is required*.

**useragent** - 
The User-Agent (browser) of the end-user to whom the job results will be displayed. This can be obtained from the "User-Agent" HTTP request header from the end-user. *This field is required*.

**format** - 
Format. Which output format of the API you wish to use. The options are "xml" and "json.". Default is "json". The `IndeedClient` requests and parses a json repsonse by default. If you with to use the xml format, requests will be performed with the **raw** parameter set to `True`, see **raw**.

**raw** - 
A boolean. Receive the raw json/xml response from the Indeed API. Use in addition with *format* to specify which response format you would like. Default is `False`

**sort** - 
Sort by relevance or date. Default is relevance.

**radius** - 
Distance from search location ("as the crow flies"). Default is 25.

**start** - 
Start results at this result number, beginning with 0. Default is 0.

**limit** - 
Maximum number of results returned per query. Default is 10, Maximum is 25

**fromage** - 
Number of days back to search.

**highlight** - 
Setting this value to 1 will bold terms in the snippet that are also present in q. Default is 0.

**filter** - 
Filter duplicate results. 0 turns off duplicate job filtering. Default is 1.

**latlong** - 
If latlong=1, returns latitude and longitude information for each job result. Default is 0.

**co** - 
Search within country specified. Default is *us*.


### Job Details

**jobkeys** - 
Job keys. A list of job keys specifying the jobs to look up. *This parameter is required*.

**format** - 
Format. Which output format of the API you wish to use. The options are "xml" and "json.". Default is "json". The `IndeedClient` requests and parses a json repsonse by default. If you with to use the xml format, requests will be performed with the **raw** parameter set to `True`, see **raw**.

**raw** - 
A boolean. Receive the raw json/xml response from the Indeed API. Use in addition with *format* to specify which response format you would like. Default is `False`
