# !/usr/bin/env python
# -*- coding: utf-8 -*-

from db_method import *
from report_format import *


def main():
    """print the analyzed report"""

    """REPORT ONE(Top 3 articles): Get the selected results from table log and
    capture useful (begin with 9th character) slug as condition to select the
    titles from table articles, store the titles and views in the list to call
    the function print_top3_articles to print the report."""
    # pop_articles_titles -- list, to store the titles for each article
    pop_articles_titles = []
    # pop_articles_views -- list, to store total views for each article
    pop_articles_views = []

    log_results = get_pop_articles_path()
    for result in log_results:
        title_results = get_articles_title(result[0][9:])
        for title_result in title_results:
            pop_articles_titles.append(title_result[0])
        pop_articles_views.append(str(result[1]))

    print_top3_articles(pop_articles_titles, pop_articles_views)

    """REPORT TWO(popular authors): First to create 2 views in database to get
    the valuable data(author id and total views for each id), then get the
    author's name from table authors by author id, store the names and views
    for each author in the list to call function print_pop_authors to print the
    report."""
    # pop_author_names -- list, to store authors' name
    pop_author_names = []
    # pop_author_views -- list, to store total views for each author
    pop_author_views = []

    authors_results = get_pop_authors_id()
    for result in authors_results:
        author_names = get_author_name(result[0])
        for name in author_names:
            pop_author_names.append(name[0])
        pop_author_views.append(str(result[1]))

    print_pop_authors(pop_author_names, pop_author_views)

    """Report THREE(error percentage): First to create 1 view in database to
    get the counted error status for each day, the join the view with another
    table witch include the all counted status for each day, compute the
    percentage and call function print_error_percentage to print the report."""
    status_results = get_error_all_status()
    for result in status_results:
        percentage = round(result[0], 3) / round(result[2], 3)
        if percentage > 0.01:
            print_error_percentage(percentage, result[1])


if __name__ == "__main__":
    main()
