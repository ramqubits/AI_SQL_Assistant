
# 🤖 AI SQL Assistant

Convert plain English questions into SQL using AI.

🔗 **Live Demo:** https://aisqlassistant-aps5hdbrjzvqcrvathlk3e.streamlit.app/

🔗 **GitHub:** https://github.com/ramqubits/AI_SQL_Assistant

---

## 📌 About the Project

This is my first AI application, built as part of my AI learning journey.

The idea was simple:

> **Can I ask a question in plain English and let AI generate the SQL for me?**

For example:

**User:**
> Show me all sales from the South region.

**AI generates:**

```sql
SELECT *
FROM sales_transactions
WHERE region = 'South';
````

The application then validates the generated SQL, executes it against a database, and displays the results.

---

## 🚀 Features

* 💬 Convert plain English questions into SQL
* 🤖 AI-powered SQL generation using Gemini
* ✅ SQL validation before execution
* 🗄️ Execute SQL against SQLite database
* 📊 Display query results
* 📥 Download results as CSV
* 💡 Explain generated SQL using AI
* 🕘 Query history
* 🧪 Demo Mode for testing without consuming AI quota
* 🌐 Deployed using Streamlit Community Cloud

---

## 🏗️ How It Works

```text
                         User
                           │
                           ▼
                  ┌─────────────────┐
                  │  Streamlit UI   │
                  └────────┬────────┘
                           │
                    Plain English
                           │
                           ▼
                  ┌─────────────────┐
                  │   Gemini AI     │
                  │  SQL Generator  │
                  └────────┬────────┘
                           │
                      Generated SQL
                           │
                           ▼
                  ┌─────────────────┐
                  │ SQL Validator   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ SQLite Database │
                  └────────┬────────┘
                           │
                           ▼
                    Query Results
                     /          \
                    ▼            ▼
              CSV Download   Query History

                     Generated SQL
                           │
                           ▼
                    Explain SQL
                           │
                           ▼
                       Gemini AI
---

## 🛠️ Technology Stack

* **Python**
* **Streamlit**
* **Google Gemini API**
* **SQLite**
* **Pandas**
* **Git & GitHub**

---

## 📂 Project Structure

```text
AI_SQL_Assistant/
│
├── database/
│   └── create_db.py
│
├── prompts/
│   └── system_prompt.txt
│
├── schema/
│   └── schema.txt
│
├── services/
│   ├── ai_service.py
│   ├── sql_executor.py
│   └── validator.py
│
├── utils/
│   ├── file_reader.py
│   └── logger.py
│
├── app.py
├── config.py
├── ui.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ramqubits/AI_SQL_Assistant.git
```

### 2. Navigate to the project

```bash
cd AI_SQL_Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Gemini API Key

Set the following environment variable:

```text
GEMINI_API_KEY=your_api_key
```

Do not commit your API key to GitHub.

### 7. Run the application

```bash
streamlit run ui.py
```

---

## 🧪 Demo Mode

The application includes a Demo Mode that allows the application to be tested without calling the Gemini API.

This is useful for:

* Development
* Testing
* Demonstrations
* Avoiding unnecessary API quota usage

---

## 💡 Example Questions

Try questions such as:

```text
Show all sales from the South region.
```

```text
What is the total sales amount?
```

```text
Show all sales transactions.
```

---

## 🎯 What I Learned

This project helped me understand how different components of an AI application work together:

* Working with Large Language Models
* Prompt engineering
* Connecting Python applications with AI APIs
* Converting natural language into SQL
* SQL validation
* Database execution
* Session state in Streamlit
* Error handling
* Demo/testing strategies
* Git and GitHub
* Deploying an AI application

Most importantly, I learned that **building a small working application is a much better way to understand AI than only consuming tutorials and documentation.**

---

## 🔮 Future Improvements

Potential improvements include:

* Support for more database systems
* Better SQL validation and safety
* Improved SQL explanations
* More advanced query history
* Authentication
* Role-based access
* Improved error handling
* Support for more complex natural-language queries

---

## 👨‍💻 About

Built by **Ramkumar** as part of my journey from Data Engineering into AI.

With 15+ years of experience in Data Engineering, this project is one of my first steps toward building practical AI-powered applications.

---

## ⭐ Feedback

If you try the application and have suggestions or improvements, I'd love to hear them.

---

**Built with curiosity, learning, and a lot of experimentation. 🚀**

```