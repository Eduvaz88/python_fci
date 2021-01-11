from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'proyecto_pa'
mysql = MySQL(app)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/ad_pelicula')
def Pelicula():
    return render_template('ad_pelicula.html')

@app.route('/ad_rating')
def Rating():
    return render_template('ad_rating.html')


@app.route('/ad_cliente', methods=['POST'])
def ad_cliente():
  if request.method == 'POST':
      cedula = request.form['cedula']
      nombre = request.form['nombre']
      apellido = request.form['apellido']
      cur = mysql.connection.cursor()
      cur.execute('INSERT INTO cliente (cedula, nombre, apellido) VALUES (%s, %s, %s)',
      (cedula, nombre, apellido))
      mysql.connection.commit()
      return redirect(url_for('Index'))

@app.route('/ad_pelicula', methods=['POST'])
def ad_pelicula():
  if request.method == 'POST':
      nombre = request.form['nombre']
      duracion = request.form['duracion']
      cur = mysql.connection.cursor()
      cur.execute('INSERT INTO pelicula (nombre, duracion) VALUES (%s, %s)',
      (nombre, duracion))
      mysql.connection.commit()
      return redirect(url_for('Pelicula'))

@app.route('/ad_rating', methods=['POST'])
def ad_rating():
  if request.method == 'POST':
      idpelicula = request.form['idpelicula']
      idcliente = request.form['idcliente']
      rating = request.form['rating']
      cur = mysql.connection.cursor()
      cur.execute('INSERT INTO rating (idpelicula, idcliente, rating) VALUES (%s, %s, %s)',
      (idpelicula, idcliente, rating))
      mysql.connection.commit()
      return redirect(url_for('Rating'))


if __name__ == '__main__':
 app.run(port = 3000, debug = True)
