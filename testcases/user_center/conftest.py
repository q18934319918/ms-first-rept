from utils.log_util import logger
from utils.mysql_util import db


def delete_user(mobile):
    sql = f"delete from users_userprofile where username = {mobile}"
    db.execute_sql(sql)

def delete_code(mobile):
    sql = f"delete from users_verifycode where mobile = {mobile}"
    db.execute_sql(sql)