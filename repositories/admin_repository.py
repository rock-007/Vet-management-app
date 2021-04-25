from db.run_sql import run_sql

# Return_admin_email_that_is_logged_in
def get_status():
    sql= "SELECT email FROM admins WHERE login_status = %s"
    values= [True]

    result = run_sql(sql, values)
    if (len(result) == 0):
        return None
    else:
        return result[0][0]


# Set_admin_email_that_is_logging_in
def set_status(email):
    if(get_status() == None):
        sql= "UPDATE admins SET login_status=%s RETURNING email"
        values=[True]
        result = run_sql(sql, values)
        print(result)
        return result[0]



