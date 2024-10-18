import requests
import os


def get_data() -> None:

    folder = "data"

    try:
        if not os.path.isdir(folder):
            os.mkdir(folder)
            print(f"{folder} has just been created")
        else:
            print(f"{folder} exsists already")

        url = "https://housing-infrastructure.canada.ca/gmap-gcarte/download-gmap-data-eng.html"

        data = {
            "AllData": "Download All Data"
        }

        res = requests.post(url, data)

        if res.status_code == 200:
            with open(f"{folder}/download_data.csv", "wb") as file:
                file.write(res.content)
                print("CSV downloaded")
        else:
            print("Somthing went wrong")

    except Exception as err:
        print(err)


if __name__ == "__main__":
    get_data()
