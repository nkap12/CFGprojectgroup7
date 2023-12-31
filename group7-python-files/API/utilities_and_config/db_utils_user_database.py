import mysql.connector
from config_users_database import USER, PASSWORD, HOST
import re


class DbConnectionError(Exception):
    pass


def _connect_to_db(database_name: str) -> object:
    """Establish connection to database"""

    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=database_name
    )
    return connection


def verify_email(email:str) -> bool:
    """Verify that user email is in the correct format"""

    email_pattern = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z.]{1,5}$"
    return True if re.match(email_pattern, email) else False


def verify_password(password:str) -> bool:
    """Verify that password is in the correct format"""

    permissable_characters = [letter for letter in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+"]
    if len(password) < 8:
        return False
    for character in password:
        if character not in permissable_characters:
            return False
    return True


def verify_email_and_password(email_status: bool, password_status: bool):
    """Check overall status of the user and show the cause of any failure"""

    if email_status and password_status:
        return True
    if not email_status and password_status:
        return "Your email format is incorrect. Please check and try again."
    if email_status and not password_status:
        return "Your password does not fulfill the requirements. Please check and try again."
    else:
        return "Neither your email nor password fulfill the requirements. Please check and try again."


def add_user(email: str, password: str):
    """Add a user to the database"""

    try:
        database_name = "user"
        database_con = _connect_to_db(database_name)
        cursor = database_con.cursor(buffered="True")
        query = f"""
        INSERT INTO user_information (user_email, user_password) VALUES ("{email}", "{password}");"""
        cursor.execute(query)
        result = cursor.fetchall()
        database_con.commit()
        cursor.close()
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if database_con:
            database_con.close()


def retrieve_user(email:str) -> list:
    """Retrieve an email and password from our database"""

    try:
        database_name = "user"
        database_con = _connect_to_db(database_name)
        cursor = database_con.cursor(buffered="True")
        query = f"""
        SELECT user_email, user_password FROM user_information WHERE user_email = "{email}";"""
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if database_con:
            database_con.close()
        return result


def check_user(result: list, password_check: str) -> str:
    """Check if email exists in database"""

    if not result:
        return "This email address does not exist in our database. Please create an account."
    email, password = result[0]
    return "Sign-In Complete" if password == password_check else "Incorrect Password. Please try again."

