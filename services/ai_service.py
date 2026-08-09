#from google import genai
#
#class AIService:
#
#    def __init__(self, api_key):
#        self.client = genai.Client(api_key=api_key)
#
#    def generate_sql(self, prompt):
#
#        response = self.client.models.generate_content(
#            model="models/gemini-3-flash-preview",
#            contents=prompt
#        )
#
#        return response.text

import os
import re
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
#print(f"Client initialized: {client}")  # Debugging

def clean_sql(response_text):
    """
    Removes markdown and explanation from Gemini response.
    Returns only the SQL statement.
    """

    # Remove markdown code blocks
    response_text = response_text.replace("```sql", "")
    response_text = response_text.replace("```", "")

    # Extract only the SQL statement ending with ;
    match = re.search(
        r"(SELECT.*?;)",
        response_text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return response_text.strip()


def generate_sql(prompt):

    response = client.models.generate_content(
        model="models/gemini-3-flash-preview",
        contents=prompt
    )

    sql = clean_sql(response.text)
    print(f"Generated SQL: {sql}")  # Debugging

    return sql


def explain_sql(sql_query):
    explain_prompt = f"""
Explain the following SQL query in simple English.

SQL Query:

{sql_query}

Explain:
1. What the query does
2. Which table it uses
3. Which columns it uses
4. Any filtering, grouping or sorting being performed

Keep the explanation beginner-friendly.
"""
    response = client.models.generate_content(
        model="models/gemini-3-flash-preview",
        contents=explain_prompt
    )

    explain_text = response.text
    print(f"Explanation: {explain_text}")  # Debugging

    return explain_text
    
    