def validate(sql):

    if not sql:
        return False

    sql = sql.strip().upper()

    # Handle AI-generated invalid response
    if sql == "INVALID_SQL":
        return False

    # Only SELECT queries are allowed
    if not sql.startswith("SELECT"):
        return False

    blocked = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE",
        "CREATE",
        "REPLACE"
    ]

    for keyword in blocked:
        if keyword in sql:
            return False

    return True