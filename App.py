from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyecto_pa'
mysql = MySQL(app)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
  if request.method == 'POST':
      nombre = request.form['nombre']
      telefono = request.form['telefono']
      email = request.form['email']
      cur = mysql.connection.cursor()
      cur.execute('INSERT INTO contacts (nombre, telefono, email) VALUES (%s, %s, %s)',
      (nombre, telefono, email))
      mysql.connection.commit()
      return 'received'


if __name__ == '__main__':
 app.run(port = 3000, debug = True)
