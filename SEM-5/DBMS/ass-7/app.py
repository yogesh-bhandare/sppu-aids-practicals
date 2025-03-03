from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Database configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",  
    password="yogesh8",   
    database="flaskdb"
)

# Home route - Display all users
@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

# Add User route - Insert new user into the database
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']

        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
        db.commit()
        return redirect('/')
    
    return render_template('add_user.html')

# Edit User route - Update user data in the database
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']

        cursor = db.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s", (name, email, age, id))
        db.commit()
        return redirect('/')
    
    return render_template('edit_user.html', user=user)

# Delete User route - Remove a user from the database
@app.route('/delete/<int:id>')
def delete_user(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
