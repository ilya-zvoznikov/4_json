# Prettify JSON

The script accepts a path to a file with arbitrary data in JSON format and outputs its contents to the console in readable form.

# Quickstart

The script requires for its operation installed Python interpreter version 3.5.
The path to the file in JSON format is specified when running after the script name

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py akco_shops.json
{
    "geometry": {
        "coordinates": [
            37.39703804817934,
            55.740999719549094
        ],
        "type": "Point"
    },
    "type": "Feature",
    "properties": {
        "RowId": "79742784-9ef3-4543-bc98-a219a8903c18",
        "VersionNumber": 1,
        "Attributes": {
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "Address": "улица Академика Павлова, дом 10",
            "ClarificationOfWorkingHours": null,
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "среда",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "четверг",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "пятница",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "суббота",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "воскресенье",
                    "Hours": "09:30-22:30"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "global_id": 14371450,
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "OperatingCompany": "Ароматный Мир",
            "AdmArea": "Западный административный округ",
            "District": "район Кунцево"
        },
        "ReleaseNumber": 2,
        "DatasetId": 1854
    }
}
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
