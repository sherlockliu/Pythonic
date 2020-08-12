# ！/usr/bin/python


class DistinctError(Exception):
    pass


class DistinctDict(dict):
    def __setitem__(self, key, value):
        try:
            if self.keys().__contains__(key):
                raise DistinctError(f'This key {key} exists for {self[key]}')
        except ValueError:
            pass
        super(DistinctDict, self).__setitem__(key, value)


distinct_dict = DistinctDict()
distinct_dict.__setitem__('name', 'sherlock')
# distinct_dict.__setitem__('name', 'sherlock')
