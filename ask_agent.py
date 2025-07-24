import sqlite3
import ollama

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

print("Ask a question about the E-commerce data (or type 'exit'):")

while True:
    question = input(">> ")

    if question.lower() in ['exit', 'quit']:
        break

    try:
        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant and data analyst. Your job is to generate correct SQL queries ONLY. Do not add explanations. The database has these tables: ad_sales, total_sales, eligibility."
                },
                {
                    "role": "user",
                    "content": f"Convert this to SQL: {question}"
                }
            ]
        )

        sql_query = response['message']['content'].strip()
        print(f"\nSQL Generated:\n{sql_query}\n")

        if not sql_query.lower().startswith("select"):
            print("⚠️ No valid SELECT SQL query was generated.")
            continue

        cursor.execute(sql_query)
        result = cursor.fetchall()

        if not result:
            print("No results found.\n")
        else:
            print("Answer:")
            for row in result:
                print(row)
            print()

    except Exception as e:
        print("SQL ERROR:", e)
