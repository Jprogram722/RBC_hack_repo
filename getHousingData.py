import requests
from pprint import pprint
import json


def main() -> None:
    url = "https://www.houseful.ca/api/search/?path=%2Fns"

    res = requests.get(url)
    data = json.loads(res.content)

    pprint(data)


if __name__ == "__main__":
    main()
