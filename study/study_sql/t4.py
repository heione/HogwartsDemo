from study.study_sql.sqldb import SQL

b = SQL.get_instance().select_sql('select * from users where login_state = 0 and vipLevel = 3')
print(b)
