def date_format(string_1):
    month, day, year = string_1.split('/')
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"