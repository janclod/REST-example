import io
import sys
import json
import requests


def main():
    file = 'municipalities_nl.geojson'
    url ='http://127.0.0.1:8000/municipalities/'
    return push(file, url)


def push(file, url):
    features = get_features(file)
    err = 0
    for f in features:
        if not post_request(f, url):
            err = 1
            break
        else:
            continue
    return err


def get_features(file):
    f = io.open(file, 'r')
    obj = json.load(f)
    return obj.get('features')


def post_request(payload, url):
    r = requests.post(url, json=payload)
    return r.status_code == 201


if __name__ == '__main__':
    sys.exit(main())
