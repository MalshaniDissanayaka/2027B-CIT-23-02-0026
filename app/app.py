from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "todo-db"),
        user=os.environ.get("DB_USER", "user"),
        password=os.environ.get("DB_PASSWORD", "password"),
        database=os.environ.get("DB_NAME", "todo")
    )

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        task = request.form["task"]
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        conn.commit()
        return redirect("/")

    cursor.execute("SELECT id, task, done FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    return render_template("index.html", tasks=tasks)

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done=1 WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
