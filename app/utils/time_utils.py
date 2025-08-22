import datetime as dt


def utcnow():
    return dt.datetime.now(dt.UTC)
