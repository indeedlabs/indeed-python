from requests import Session

DEFAULT_FORMAT = "json"
API_ROOT = "http://api.indeed.com/ads"

API_SEARCH = dict(
    end_point=f"{API_ROOT}/apisearch",
    required_fields=["userip", "useragent", ['q', 'l']]
)

API_JOBS = dict(
    end_point=f"{API_ROOT}/apigetjobs",
    required_fields=["jobkeys"]
)

class IndeedClientException(Exception):
    pass

class IndeedClient(Session):
    def __init__(self, publisher, version = '2'):
        super(IndeedClient, self).__init__()
        self.publisher = publisher
        self.version = version

    def search(self, **args):
        return self.__process_request(
            API_SEARCH.get("end_point"),
            self.__valid_args(API_SEARCH.get("required_fields"), args))

    def jobs(self, **args):
        valid_args = self.__valid_args(API_JOBS.get("required_fields"), args)
        valid_args["jobkeys"] = ','.join(valid_args["jobkeys"])
        return self.__process_request(API_JOBS.get("end_point"), valid_args)

    def __process_request(self, endpoint, args):
        format_ = args.get("format", DEFAULT_FORMAT)
        if format_ == "xml":
            raw = True
        else:
            raw = args.get("raw", False)
        args.update({'v': self.version, "publisher": self.publisher, "format": format_})
        response = self.get(endpoint, params = args)
        return response.json() if not raw else response.content

    def __valid_args(self, required_fields, args):
        for field in required_fields:
            if isinstance(field, list):
                if not (True in [args.get(f) != None for f in field]):
                    raise IndeedClientException(f"You must provide one of the following {','.join(field)}")
            elif not args.get(field):
                raise IndeedClientException(f"The field {field} is required")
        return args


