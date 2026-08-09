from services.ai_service import generate_sql
from services.sql_executor import execute
from services.validator import validate
from utils.file_reader import read_file

# Read files
schema = read_file("schema/schema.txt")
system_prompt = read_file("prompts/system_prompt.txt")

# Get user input
user_question = input("Enter your question: ")

# Build prompt
full_prompt = f"""
{system_prompt}

Database Schema:
{schema}

User Question:
{user_question}
"""

# Generate SQL
sql = generate_sql(full_prompt)

# Validate
if validate(sql):
    result = execute(sql)
    print(result)
else:
    print("Invalid SQL")

