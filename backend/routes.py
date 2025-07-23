from flask import Flask,request
from .qLinked import QlinkedList

app=Flask(__name__)
task_queue= QlinkedList()

@app.route("/")
def home():
    return "Task Manager app is running"

@app.route("/add_task",methods=["POST"])
def add_task():
    task = request.form.get("task")
    if not task:
        return "No task provided. ",400
    task_queue.enqueue(task)
    return f"Task '{task}' added to the queue."


if __name__ == "__main__":
    app.run(debug=True)