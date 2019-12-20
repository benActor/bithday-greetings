import pandas as pd
import time


def get_csv_content(file_path):
    df = pd.read_csv(file_path,)
    if csv_validator(list(df.columns)):
        return df.to_dict()


def csv_validator(header):
    expected_header = ["last_name", "first_name", "date_of_birth", "email"]
    return expected_header == header


def has_birthday_today(data_oject):
    people_with_bday = []
    current_date = time.strftime("%Y/%m/%d")
    for val in data_oject["date_of_birth"]:
        if data_oject["date_of_birth"][val] == str(current_date):
            people_with_bday.append(val)
    return people_with_bday

def birthday_message(data_object):
    birthday_list = has_birthday_today(data_object)
    for person_id in birthday_list:
        subject = "subject: Happy Birthday"
        message = "Happy Birthday, dear {}".format(data_object["first_name"][person_id])
        print(subject)
        print(message)



print(get_csv_content("data.csv"))

birthday_message(get_csv_content("data.csv"))








