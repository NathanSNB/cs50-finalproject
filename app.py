# ====== < IMPORTATIONS ET CONFIGURATION > ======
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
import markdown

app = Flask(__name__)
db = SQL("sqlite:///nataboards.db")

@app.template_filter('render_markdown')
def render_markdown(text):
    return markdown.markdown(text)


# ====== < NAVIGATION PRINCIPALE > ======
@app.route("/")
def index():
    rows = db.execute("SELECT * FROM boards")
    return render_template("index.html", boards=rows)

@app.route("/board/<int:board_id>")
def board(board_id):
    rows = db.execute("SELECT name FROM boards WHERE id = ?", board_id)
    board_name = rows[0]["name"]

    columns = db.execute("SELECT * FROM columns WHERE board_id = ? ORDER BY position", board_id)

    items = db.execute(
        "SELECT * FROM items WHERE column_id IN (SELECT id from columns WHERE board_id = ?)", board_id)

    return render_template("board.html", board_id=board_id, board_name=board_name, columns=columns, items=items)


# ====== < GESTION DES BOARDS > ======
@app.route("/add_board", methods=["POST"])
def add_board():
    name = request.form.get("board")
    db.execute("INSERT INTO boards (name) VALUES (?)", name)
    return redirect("/")

@app.route("/remove_board", methods=["POST"])
def remove_board():
    board_id = request.form.get("board_id")
    if board_id:
        db.execute("DELETE FROM items WHERE column_id IN (SELECT id FROM columns WHERE board_id = ?)", board_id)
        db.execute("DELETE FROM columns WHERE board_id = ?", board_id)
        db.execute("DELETE FROM boards WHERE id = ?", board_id)
    return redirect("/")


# ====== < GESTION DES COLONNES > ======
@app.route("/add_column", methods=["POST"])
def add_column():
    name = request.form.get("column")
    board_id = request.form.get("id")

    result = db.execute("SELECT MAX(position) AS max_pos FROM columns WHERE board_id = ?", board_id)
    current_max = result[0]["max_pos"]
    new_position = (current_max or 0) + 1

    db.execute("INSERT INTO columns (name, position, board_id) VALUES (?, ?, ?)", name, new_position, board_id)
    return redirect(f"/board/{board_id}")

@app.route("/remove_column", methods=["POST"])
def remove_column():
    column_id = request.form.get("column_id")
    board_id = request.form.get("board_id")
    if column_id:
        db.execute("DELETE FROM items WHERE column_id = ?", column_id)
        db.execute("DELETE FROM columns WHERE id = ?", column_id)
    return redirect(f"/board/{board_id}")


# ====== < GESTION DES ITEMS > ======
@app.route("/add_item", methods=["POST"])
def add_item():
    board_id = request.form.get("board_id")
    column_id = request.form.get("column_id")
    item_name = request.form.get("item_name")
    content = request.form.get("content")
    item_type = request.form.get("type")

    db.execute("INSERT INTO items (name, position, content, type, column_id) VALUES(?, ?, ?, ?, ?)",
               item_name, 0, content, item_type, column_id)
    return redirect(f"/board/{board_id}")

@app.route("/update_item", methods=["POST"])
def update_item():
    item_id = request.form.get("item_id")
    board_id = request.form.get("board_id")
    item_name = request.form.get("item_name")
    content = request.form.get("content")
    item_type = request.form.get("type")

    db.execute("UPDATE items SET name = ?, content = ?, type = ? WHERE id = ?",
               item_name, content, item_type, item_id)
    return redirect(f"/board/{board_id}")

@app.route("/remove_item", methods=["POST"])
def remove_item():
    item_id = request.form.get("item_id")
    board_id = request.form.get("board_id")
    db.execute("DELETE FROM items WHERE id = ?", item_id)
    return redirect(f"/board/{board_id}")
