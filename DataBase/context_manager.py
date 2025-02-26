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
            entities TEXT
        )
    """)
    
    conn.commit()
    conn.close()

# Function to store user context
def store_context_db(user_id, intent, entities):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO context (user_id, intent, entities)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            intent = excluded.intent,
            entities = excluded.entities
    """, (user_id, intent, str(entities)))
    
    conn.commit()
    conn.close()

# Function to retrieve user context
def get_context_db(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT intent, entities FROM context WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return {"intent": result[0], "entities": eval(result[1])}
    return None  # No context found

# Run this once to ensure the database is set up
create_database()

# Test code (remove or comment this out in production)
if __name__ == "__main__":

    test_user = "user123"
    
    # Store test context
    store_context_db(test_user, "Department_Query", {"department": "CSE"})

    # Retrieve and print test context
    context = get_context_db(test_user)
    print(context)