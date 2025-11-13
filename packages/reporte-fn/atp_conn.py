import os
import oracledb


def get_connection() -> oracledb.Connection:
    """
    Establishes and returns a connection to the Oracle database.

    Parameters:
        user (str): The username for the database connection.
        password (str): The password for the database connection.
        dsn (str): The Data Source Name for the database connection.

    Returns:
        oracledb.Connection: An active connection to the Oracle database.
    """
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    dsn = os.getenv("DB_DSN")

    if not all([user, password, dsn]):
        raise ValueError(
            "Database connection parameters are not fully set in environment variables."
        )

    connection = oracledb.connect(user=user, password=password, dsn=dsn)

    return connection
