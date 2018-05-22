# analysis_tool
An analysis tool to print the 3 results for Udacity full-stack training project 3
This project is running in linux system with PostgreSQL database
## db_method.py
Include 5 functions to select the results from database news. Below are the preparation before you want to invoke those functions
* Before invoke function get_pop_authors_id() and get_author_name(author_id), make sure create below views first:
  * create view articles_new as select author, '/article/'||slug as slug from articles;
  * create view author_views as select * from articles_new, (select path, count(time) as count from log where path like '/article/%' and status = '200 OK' group by path) as subq where slug = path;
* Before inboke function get_error_all_status(), make sure create below view first:
  * create view not_OK as select count(status) as not_OK, to_char(time, 'yyyy-mm-dd') as date from log where not status='200 OK' group by date order by date;
