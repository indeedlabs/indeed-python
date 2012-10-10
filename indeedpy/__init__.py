import requests

API_VERSION = "2"
API_ROOT = "http://api.indeed.com/ads"
API_SEARCH = {'end_point': "%s/apisearch" % API_ROOT, 'required_fields': ['userip', 'useragent', ['q', 'l']]}
API_JOBS = {'end_point': "%s/apigetjobs" % API_ROOT, 'required_fields': ['jobkeys']}

class Indeed:

    def __init__(self, publisher):
        self.publisher = publisher

    def search(self, **args):
        return self.__process_request(API_SEARCH.get('endpoint'), self.__valid_args(API_SEARCH.get('required_fields'), args))

    def jobs(self, **args):
        return self.__process_request(API_JOBS.get('endpoint'), self.__valid_jobs_args(API_JOBS.get('required_fields'), args))

    def __process_request(self, endpoint, args):
        args.update({'v': API_VERSION, 'publisher': self.publisher})
        r = requests.get(endpoint, params = args)
        return r.json if args.get('format', 'xml') == 'json' else r.content

    def __valid_args(self, required_fields, args):
        for field in required_fields:
            if type(field) is list:
                validation_list = [args.get(field) != None for f in field]
                if False in validation_list:
                    raise("You must provide one of the following %s" % ",".join(field))
            elif not args.get(field):
                raise("The field %s is required" % field)
        return args


    