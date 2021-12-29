import json
import http.client as httplib


def internet():
    # https://stackoverflow.com/a/29854274/3362993
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


def save_dict_to_file(data, json_path):
    with open(json_path, "w") as f:
        json.dump(data, f)


def load_dict_from_file(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    return data


class dotdict(dict):
    # https://stackoverflow.com/a/9205155/3362993
    def __getattr__(self, name):
        return self[name]


def zip_to_dict(sub_zip, keys):
    dic = {key: value for (key, value) in sub_zip}
    dic = {key: dic[key] for key in keys}
    return dic


def has_q_mark(x):
    return x.find("?") > -1
