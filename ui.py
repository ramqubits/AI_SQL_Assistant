import streamlit as st
from services.ai_service import generate_sql, explain_sql
from services.sql_executor import execute
from services.validator import validate


# ---------------------------------
# Streamlit Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------
# Sidebar - Application Settings
# ---------------------------------

st.sidebar.header("⚙️ Settings")

DEMO_MODE = st.sidebar.toggle(
    "🧪 Demo Mode",
    value=True,
    help="When enabled, Gemini API is not called. Dummy SQL is used for testing."
)

if DEMO_MODE:
    st.sidebar.success("Demo Mode ON")
    st.sidebar.caption("Gemini API is not being used.")
else:
    st.sidebar.info("Real AI Mode")
    st.sidebar.caption("Queries will be sent to Gemini.")


# ---------------------------------
# Application Title
# ---------------------------------

st.title("🤖 AI SQL Assistant")

st.markdown(
    "### Convert plain English questions into SQL using AI"
)

st.caption(
    "Ask a question in natural language and get SQL, "
    "query results, an explanation, and downloadable data."
)

if DEMO_MODE:
    st.info(
        "🧪 Demo Mode is ON — using test SQL. "
        "No Gemini API calls are being made."
    )
else:
    st.success(
        "🤖 AI Mode is ON — SQL will be generated using Gemini."
    )

# ---------------------------------
# Initialize Session State
# ---------------------------------

if "sql" not in st.session_state:
    st.session_state.sql = None

if "result" not in st.session_state:
    st.session_state.result = None

if "history" not in st.session_state:
    st.session_state.history = []


# ---------------------------------
# User Question
# ---------------------------------

with st.form("sql_form"):

    question = st.text_input(
        "Ask your question"
    )

    generate_clicked = st.form_submit_button(
        "Generate SQL"
    )


# ---------------------------------
# Read Prompt and Schema
# ---------------------------------

with open("prompts/system_prompt.txt") as f:
    system_prompt = f.read()

with open("schema/schema.txt") as f:
    schema = f.read()


# ---------------------------------
# Generate SQL
# ---------------------------------

if generate_clicked:

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

        st.stop()


    # ---------------------------------
    # Build Gemini Prompt
    # ---------------------------------

    full_prompt = f"""
{system_prompt}

Database Schema:

{schema}

User Question:

{question}
"""


    try:

        # ---------------------------------
        # Demo Mode
        # ---------------------------------

        if DEMO_MODE:

            if "south" in question.lower():

                sql = """
SELECT *
FROM sales_transactions
WHERE region = 'South';
""".strip()


            elif "total" in question.lower():

                sql = """
SELECT SUM(total_amount) AS total_sales
FROM sales_transactions;
""".strip()


            else:

                sql = """
SELECT *
FROM sales_transactions;
""".strip()


        # ---------------------------------
        # Real Gemini Mode
        # ---------------------------------

        else:

            with st.spinner(
                "Generating SQL..."
            ):

                sql = generate_sql(
                    full_prompt
                )


        # ---------------------------------
        # Store SQL
        # ---------------------------------

        st.session_state.sql = sql


        # ---------------------------------
        # Store Query History
        # ---------------------------------

        st.session_state.history.append(
            {
                "question": question,
                "sql": sql
            }
        )


    except Exception as e:
    
        error_message = str(e)
    
        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
    
            st.error(
                "⚠️ AI service quota has been reached."
            )
    
            st.info(
                "Please try again later or switch ON "
                "Demo Mode from the sidebar to continue testing."
            )
    
        else:
    
            st.error(
                "⚠️ Something went wrong while generating SQL."
            )
    
            st.caption(
                f"Technical details: {error_message}"
            )
    
        st.stop()


# ---------------------------------
# Display Generated SQL
# ---------------------------------

if st.session_state.sql:

    st.subheader(
        "Generated SQL"
    )

    st.code(
        st.session_state.sql,
        language="sql"
    )


    # ---------------------------------
    # Validate SQL
    # ---------------------------------

    if validate(
        st.session_state.sql
    ):

        st.success(
            "SQL validation successful."
        )

    else:

        st.error(
            "Invalid SQL generated."
        )

        st.stop()


    # ---------------------------------
    # Execute SQL
    # ---------------------------------

    try:

        result = execute(
            st.session_state.sql
        )

        st.session_state.result = result


    except Exception as e:

        st.error(
            f"SQL execution error: {e}"
        )

        st.stop()


    # ---------------------------------
    # Query Results
    # ---------------------------------

    if st.session_state.result is not None:

        st.subheader(
            "Query Results"
        )

        st.dataframe(
            st.session_state.result
        )


        # ---------------------------------
        # Download CSV
        # ---------------------------------

        csv = (
            st.session_state.result
            .to_csv(index=False)
        )

        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="query_results.csv",
            mime="text/csv"
        )


    # ---------------------------------
    # Explain SQL
    # ---------------------------------

    col1, col2 = st.columns([1, 5])


    with col1:

        explain_clicked = st.button(
            "Explain SQL"
        )


    with col2:

        st.caption(
            "This feature will explain the generated SQL using AI."
        )


    if explain_clicked:

        with st.spinner(
            "Analyzing SQL..."
        ):

            # ---------------------------------
            # Demo Explanation
            # ---------------------------------

            if DEMO_MODE:

                explain_text = """
This query retrieves all records from the
sales_transactions table.

It returns the following columns:

- transaction_id
- customer_id
- transaction_date
- total_amount
- region

There is no filtering, grouping, or sorting
being performed.
"""


            # ---------------------------------
            # Real Gemini Explanation
            # ---------------------------------

            else:

                try:

                    explain_text = explain_sql(
                        st.session_state.sql
                    )

                except Exception as e:

                    error_message = str(e)

                    if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:

                        st.error(
                            "⚠️ AI service quota has been reached."
                        )

                        st.info(
                            "Please try again later or switch ON "
                            "Demo Mode from the sidebar."
                        )

                        explain_text = None

                    else:

                        st.error(
                            "⚠️ Unable to explain the SQL right now."
                        )

                        st.caption(
                            f"Technical details: {error_message}"
                        )

                        explain_text = None
        if explain_text:

            st.subheader("SQL Explanation")
            st.write(explain_text)


# ---------------------------------
# Query History
# ---------------------------------

if st.session_state.history:

    st.subheader(
        "🕘 Query History"
    )


    # ---------------------------------
    # Clear History
    # ---------------------------------

    if st.button("🗑️ Clear History"):

        st.session_state.history = []

        st.rerun()


    # ---------------------------------
    # Display History
    # ---------------------------------

    for i, item in enumerate(
        reversed(
            st.session_state.history
        ),
        start=1
    ):

        with st.expander(
            f"{i}. {item['question']}"
        ):

            st.code(
                item["sql"],
                language="sql"
            )



#How to Run the Streamlit App
# 1. Save this code in a file named `ui.py`.    
# 2. Open a terminal and navigate to the directory where `ui.py` is located.
# 3. Run the command: `streamlit run ui.py`.