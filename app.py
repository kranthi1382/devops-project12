from flask import Flask, request, redirect

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Docker", "completed": True},
    {"id": 2, "title": "Build Jenkins Pipeline", "completed": False},
    {"id": 3, "title": "Deploy to AWS EC2", "completed": False}
    {"id": 3, "title": "Deploy to docker", "completed": False}
]


@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Task Manager</title>
        <style>
            body {
                font-family: Arial;
                max-width: 700px;
                margin: 50px auto;
                background: #f4f4f4;
            }

            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
            }

            h1 {
                text-align: center;
            }

            .task {
                padding: 12px;
                margin: 8px 0;
                background: #eee;
                border-radius: 5px;
            }

            .completed {
                text-decoration: line-through;
            }

            form {
                margin-top: 20px;
            }

            input {
                padding: 10px;
                width: 70%;
            }

            button {
                padding: 10px 15px;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <h1>DevOps Task Manager</h1>

            <h2>Tasks</h2>

            """

    for task in tasks:
        status = "completed" if task["completed"] else ""

        html += f"""
        <div class="task {status}">
            {task["title"]}
        </div>
        """

    html += """
            <form action="/add" method="POST">
                <input
                    type="text"
                    name="title"
                    placeholder="Enter a new task"
                    required
                >
                <button type="submit">Add Task</button>
            </form>

        </div>
    </body>
    </html>
    """

    return html


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)

    return redirect("/")


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "DevOps Task Manager"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)