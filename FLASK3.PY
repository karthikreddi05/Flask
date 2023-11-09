from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create a SQLite database file.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"

# Create a Flask-SQLAlchemy model class to represent the list of items.
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), not_null=True)

# Define a route for creating an item.
@app.route("/create", methods=["POST"])
def create_item():
    # Get the item name from the request.
    item_name = request.form["item_name"]

    # Create a new item object.
    item = Item(name=item_name)

    # Add the item object to the database.
    db.session.add(item)
    db.session.commit()

    # Return a success message.
    return "Item created successfully!"

# Define a route for reading all items.
@app.route("/read", methods=["GET"])
def read_items():
    # Get all items from the database.
    items = Item.query.all()

    # Return the items.
    return render_template("items.html", items=items)

# Define a route for updating an item.
@app.route("/update/<int:item_id>", methods=["POST"])
def update_item(item_id):
    # Get the updated item name from the request.
    item_name = request.form["item_name"]

    # Get the item object from the database.
    item = Item.query.get(item_id)

    # Update the item object.
    item.name = item_name

    # Commit the changes to the database.
    db.session.commit()

    # Return a success message.
    return "Item updated successfully!"

# Define a route for deleting an item.
@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    # Get the item object from the database.
    item = Item.query.get(item_id)

    # Delete the item object from the database.
    db.session.delete(item)
    db.session.commit()

    # Return a success message.
    return "Item deleted successfully!"

# Start the Flask app.
if __name__ == "__main__":
    app.run(debug=True)
