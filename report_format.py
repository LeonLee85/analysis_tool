# !/usr/bin/env python
# -*- coding: utf-8 -*-


def print_top3_articles(titles, views):
    """Print report one(Top 3 articles and views)"""

    print("\nWhat are the most popular three articles of all time? \
    (title and view):\n")
    count = 0
    while count < 3:
        print(titles[count] + " ------ " + views[count] + " views")
        count += 1
    print("\n")


def print_pop_authors(names, views):
    """Print report two(Popular authors and total views for each author)"""

    print("\nWho are the most popular article authors of all time? \
    (name and view):\n")
    count = 0
    while count < len(names):
        print(names[count] + " ------ " + views[count] + " views")
        count += 1
    print("\n")


def print_error_percentage(percentage, date):
    """Format the date and print report three(On which days did more than 1%
    of requests lead to errors?)"""

    # Use dictionary to perform switch function
    month_dict = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
                  "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
                  "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
    day = date[8:]
    month = month_dict[date[5:7]]
    year = date[0:4]

    print("\nOn which days did more than 1% of requests lead to errors? \
    (date and error percentage):\n")
    print(month + " " + day + ", " + year + " ------ " +
          str(round(percentage, 3) * 100) + "%")
