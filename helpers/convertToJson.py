import csv
from pathlib import Path


def format_data(data: list) -> dict:
    next_item = {
        "DepartmentName": data[0],
        "ProgramName": data[1],
        "Category": data[2],
        "ExpectedResult": data[5],
        "FederalContribution": data[6],
        "Province": data[10],
        "Municipality": data[11],
        "Latitude": data[12],
        "Longitude": data[13],
        "ProjectStatus": data[17],
        "NumberOfUnits": data[21],
    }

    return next_item


def csv_to_json(file_path: str) -> dict:

    data_file = Path(file_path)

    # lsi for the 3 provinces
    provinces = ["Nova Scotia", "New Brunswick", "Prince Edward Island"]

    # create a dict for the data we are going to send back
    data = {"projects": []}

    if data_file.is_file():
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for line in reader:
                if (line[10] == provinces[0] or line[10] == provinces[1] or line[10] == provinces[2]) and \
                        line[1] == "Affordable Housing Fund":
                    data["projects"].append(format_data(line))

    return data


if __name__ == "__main__":
    csv_to_json()
