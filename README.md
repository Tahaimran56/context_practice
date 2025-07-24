 🤖 Agentic AI - User Data Retrieval Tool

This project demonstrates how to build an **Agentic AI assistant** using the OpenAI Agents SDK and Google's **Gemini API**. The assistant is able to fetch user context (like name and age) using a custom tool.

## 📁 File: `config.py`

The `config.py` script performs the following:

- Loads a Gemini API key from the `.env` file.
- Configures a Gemini-compatible model using OpenAI's SDK.
- Defines a context class (`user_data`) with user details.
- Defines a tool (`get_user_data`) to extract and return user context.
- Runs the agent and prints the assistant’s response.

## 🔧 Requirements

Make sure you have Python 3.9+ installed.

Install dependencies:

```bash
pip install -r requirements.txt
Your requirements.txt should include:

openai
python-dotenv
pydantic
🗝️ .env Setup
Create a .env file in the root directory with the following content:


GEMINI_API_KEY=your_gemini_api_key_here
You can get a Gemini API key from Google AI Studio.

🚀 How to Run
Use the following command in terminal:
uv run config.py
If you are not using uv, you can also run:

python config.py
🧠 What This Agent Does
This assistant uses:

A dataclass context (user_data) containing a user's name and age.

A @function_tool named get_user_data to expose that context to the agent.

The Gemini model to understand and respond to input queries like:

"What is the user's name and age?"

✅ Sample Output
{'name': 'taha', 'age': 20}
Or the assistant might say:

"The user's name is taha and they are 20 years old."

📌 Notes
The model used is gemini-2.0-flash, but you can switch to gemini-1.5-flash or others as needed.

Ensure your API key is valid and that your internet connection is active.

For better UX, consider integrating this logic into a Streamlit app.

