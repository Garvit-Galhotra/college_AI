import sqlite3

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect("chatbot_context.db")  # Connects to SQLite
    return conn

# Function to create the database table (Run once)
def create_database():
    conn = connect_db()
    cursor = conn.cursor()
    
    # writing query to db to create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS context (
            user_id TEXT PRIMARY KEY,
            intent TEXT,
            entities TEXT,
            last_response TEXT
        )
    """)
    
    conn.commit()
    conn.close()

# Function to store user context
def store_context_db(user_id, intent, entities, last_response):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO context (user_id, intent, entities, last_response)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            intent = excluded.intent,
            entities = excluded.entities,
            last_response = excluded.last_response
    """, (user_id, intent, str(entities), last_response))
    
    conn.commit()
    conn.close()

# Function to retrieve user context
def get_context_db(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT intent, entities, last_response FROM context WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return {"intent": result[0], "entities": eval(result[1]), "last_response": result[2]}
    return None  # No context found

# Run this once to ensure the database is set up
create_database()

# Test code (remove or comment this out in production)
if __name__ == "__main__":

    test_user = "user123"
    
    # Store test context
    store_context_db(test_user, "Department_Query", {"department": "CSE"}, "Do you want to know about the faculty?")

    # Retrieve and print test context
    context = get_context_db(test_user)
    print(context)