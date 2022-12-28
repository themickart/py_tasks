import math
import pandas as pd


def convert_to_rur():
    """
    Метод для конвертации валюты csv файла с вакансиями
    :return: None
    """
    file_name = input("Введите название файла: ")
    currencyFile_name = "dataframe.csv"
    df = pd.read_csv(file_name)
    df_currency = pd.read_csv(currencyFile_name)
    df.insert(1, "salary", None)
    df.assign(salary=lambda x: x.salary_from)
    df["salary"] = df[["salary_from", "salary_to"]].mean(axis=1)
    df["salary"] = df["salary"].astype(str) + " " + + df["salary_currency"] + " " + df["published_at"]
    df["salary"] = df["salary"].apply(lambda x: converter(x, df_currency))

    df = df.drop(columns=['salary_from', 'salary_to', 'salary_currency'])
    df100 = df.head(100)
    df100.to_csv("converted_dataframe.csv", index=False)


def converter(x, df_currency):
    """
    Метод для конвертации валюты по строке
    :param x: Исходная строка с средним окладом, названием валюты и датой публикации вакансии
    :param df_currency: DataFrame с курсами валют по годам начиная с 2003 года
    :return: Целое число, конвертированную по курсу
    """
    if pd.isnull(x):
        return x
    values = x.split()
    if df_currency.columns.__contains__(values[1]):
        d = values[2]
        course = df_currency[df_currency["date"] == d[:7]][values[1]].values
        if not math.isnan(course[0]):
            return round(float(values[0]) * course[0])
    return values[0]


if __name__ == '__main__':
    convert_to_rur()