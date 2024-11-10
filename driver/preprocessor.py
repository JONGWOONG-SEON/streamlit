from collections import defaultdict

class preprocess:
    def __init__(self,fetch):
        if fetch[0] == None:
            assert("No Data Check table")
        else:
            self.fetch = fetch

    def return_dict(self):
        data_dict = {}
        for key, value in self.fetch:
            if key in data_dict:
                data_dict[key].append(value)
            else:
                data_dict[key] = [value]
        return data_dict