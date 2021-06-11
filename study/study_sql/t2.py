from study.study_sql.sqldb import SQL

b = SQL().select_sql('select * from users')
print(b)
