import requests


DEFAULT_FORMAT = 'json'
API_ROOT = 'http://api.indeed.com/ads'
API_SEARCH = {
    'end_point': '{base}/apisearch'.format(base=API_ROOT),
    'required_fields': ['userip', 'useragent', ['q', 'l']]
}
API_JOBS = {
    'end_point': '{base}/apigetjobs'.format(base=API_ROOT),
    'required_fields': ['jobkeys']
}


class IndeedClientException(Exception):
    pass


class IndeedClient:
    def __init__(self, publisher, version='2'):
        self.publisher = publisher
        self.version = version

    def search(self, **args):
        return self.__process_request(API_SEARCH.get('end_point'), self.__valid_args(API_SEARCH.get('required_fields'), args))

    def jobs(self, **args):
        valid_args = self.__valid_args(API_JOBS.get('required_fields'), args)
        valid_args['jobkeys'] = ','.join(valid_args['jobkeys'])

        return self.__process_request(API_JOBS.get('end_point'), valid_args)

    def __process_request(self, endpoint, args):
        format = args.get('format', DEFAULT_FORMAT)
        raw = True if format == 'xml' else args.get('raw', False)
        args.update({'v': self.version, 'publisher': self.publisher, 'format': format})
        r = requests.get(endpoint, params=args)

        return r.json() if not raw else r.content

    def __valid_args(self, required_fields, args):
        for field in required_fields:
            if type(field) is list:
                validation_list = [args.get(f) is not None for f in field]

                if not (True in validation_list):
                    raise IndeedClientException('You must provide one of the following {fields}'.format(fields=','.join(field)))

            elif not args.get(field):
                raise IndeedClientException('The field {field} is required'.format(field=field))

        return args
