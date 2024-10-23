import datetime
import re


def reformatDate(date: str) -> str:
    x = re.match(r"\d+(\w+)", date).groups()[0]
    t1 = datetime.datetime.strptime(date, f"%d{x} %b %Y")
    t2 = datetime.datetime.strftime(t1, "%Y-%m-%d")
    return t2


if __name__ == '__main__':
    Date = "20th Oct 2052"
    reformatDate(Date)
