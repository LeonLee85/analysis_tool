# analysis_tool
An analysis tool to print the 3 results for Udacity full-stack training project 3. This project is running in linux system with PostgreSQL database.
## db_method.py
Include 5 functions to select the results from database news. Below are the preparation before you want to invoke those functions:
* Before invoke function get_pop_authors_id() and get_author_name(author_id), make sure create below views first:
  * create view articles_new as select author, '/article/'||slug as slug from articles;
  * create view author_views as select * from articles_new, (select path, count(time) as count from log where path like '/article/%' and status = '200 OK' group by path) as subq where slug = path;
* Before inboke function get_error_all_status(), make sure create below view first:
  * create view not_OK as select count(status) as not_OK, to_char(time, 'yyyy-mm-dd') as date from log where not status='200 OK' group by date order by date;
## report_format.py
This file include 3 functions to get the finnal selected result and format them to the requested layout.
## reports.py
This file is the main function, to print the result, please run this file in the linux system. Bolow are the descriptions for 3 parts in the main function:
* REPORT ONE(Top 3 articles): Get the selected results from table log and capture useful (begin with 9th character) slug as condition to select the titles from table articles, store the titles and views in the list to call the function print_top3_articles to print the report.
* REPORT TWO(popular authors): First to create 2 views in database to get the valuable data(author id and total views for each id), then get the author's name from table authors by author id, store the names and views for each author in the list to call function print_pop_authors to print the report.
* Report THREE(error percentage): First to create 1 view in database to get the counted error status for each day, the join the view with another table witch include the all counted status for each day, compute the percentage and call function print_error_percentage to print the report.
