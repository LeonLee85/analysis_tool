# !/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2


def get_pop_articles_path():
    """Get the top 3 articles' path from table log"""

    db = psycopg2.connect(database="news")
    db_cursor = db.cursor()
    db_cursor.execute("select path, count(time) as count from log where path\
    like '/article/%' and status = '200 OK' group by path order by count \
    desc limit 3;")
    results = db_cursor.fetchall()
    db.close()
    return results


def get_articles_title(slug):
    """Get the top articles' title from table articles"""

    db = psycopg2.connect(database="news")
    db_cursor = db.cursor()
    sql = "select title from articles where slug = '{slug}';"
    db_cursor.execute(sql.format(slug=slug))
    results = db_cursor.fetchall()
    db.close()
    return results


def get_pop_authors_id():
    """Get the author's ID and views from view author_views."""

    db = psycopg2.connect(database="news")
    db_cursor = db.cursor()
    db_cursor.execute("select author, sum(count) as views from author_views \
    group by author order by views desc;")
    results = db_cursor.fetchall()
    db.close()
    return results


def get_author_name(author_id):
    """Get the author's name from table authors."""

    db = psycopg2.connect(database="news")
    db_cursor = db.cursor()
    sql = "select name from authors where id = '{author_id}';"
    db_cursor.execute(sql.format(author_id=author_id))
    results = db_cursor.fetchall()
    db.close()
    return results


def get_error_all_status():
    """Get error status(not '200 OK') and all status from table log by date."""

    db = psycopg2.connect(database="news")
    db_cursor = db.cursor()
    db_cursor.execute("select * from not_OK join (select count(status) as \
    all_status, to_char(time, 'yyyy-mm-dd') as date from log group by date \
    order by date) as subq on not_OK.date = subq.date;")
    results = db_cursor.fetchall()
    db.close()
    return results
