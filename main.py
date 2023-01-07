# Store this code in 'app.py' file

from __future__ import print_function # In python 2.7
from flask import Flask, render_template, request,flash, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_debugtoolbar import DebugToolbarExtension
import re
import sys



app = Flask(__name__)


app.secret_key = 'your secret key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blooddonationsystemdb'


mysql = MySQL(app)


@app.route('/')

@app.route("/index")
def index():
	return render_template("index.html")


@app.route('/bloodbankCreate', methods =['GET', 'POST'])
def bloodbankCreate():
	msg = ''
	if request.method == 'POST' and 'name' in request.form and 'address' in request.form and 'email' in request.form and 'phone' in request.form:
		var_name = request.form['name']
		var_address = request.form['address']
		var_email = request.form['email']
		var_phone = request.form['phone']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("INSERT INTO `blooddonationsystemdb`.`tbl_bloodbank` (`name`, `address`, `email`, `phone_number`) VALUES (%s,%s,%s,%s)",(var_name, var_address, var_email, var_phone))
		mysql.connection.commit()
		msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('bloodbankCreate.html', msg = msg)

@app.route('/donorCreate', methods =['GET', 'POST'])
def donorCreate():
	msg = ''
	if request.method == 'POST' and 'firstName' in request.form and 'lastName' in request.form and 'dateBirth' in request.form and 'address' in request.form and 'bloodGroup' in request.form  and 'cnp' in request.form:
		var_firstName = request.form['firstName']
		var_lastName = request.form['lastName']
		var_dateBirth = request.form['dateBirth']
		var_address = request.form['address']
		var_bloodGroup = request.form['bloodGroup']
		var_cnp=request.form['cnp']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("INSERT INTO `blooddonationsystemdb`.`tbl_donor` (`firstName`, `lastName`, `date_of_birth`, `location`, `bloodGroup`,`cnp`) VALUES (%s,%s,%s,%s,%s,%s)",(var_firstName, var_lastName, var_dateBirth, var_address, var_bloodGroup,var_cnp))
		mysql.connection.commit()
		msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('donorCreate.html', msg = msg)

@app.route('/seekerCreate', methods =['GET', 'POST'])
def seekerCreate():
	msg = ''
	if request.method == 'POST' and 'firstName' in request.form and 'lastName' in request.form and 'dateBirth' in request.form and 'address' in request.form and 'bloodGroup' in request.form  and 'cnp' in request.form:
		var_firstName = request.form['firstName']
		var_lastName = request.form['lastName']
		var_dateBirth = request.form['dateBirth']
		var_address = request.form['address']
		var_bloodGroup = request.form['bloodGroup']
		var_cnp=request.form['cnp']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("INSERT INTO `blooddonationsystemdb`.`tbl_seeker` (`firstName`, `lastName`, `date_of_birth`, `location`, `blodGroup`,`cnp`) VALUES (%s,%s,%s,%s,%s,%s)",(var_firstName, var_lastName, var_dateBirth, var_address, var_bloodGroup,var_cnp))
		mysql.connection.commit()
		msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('seekerCreate.html', msg = msg)

@app.route('/bloodstockCreate', methods =['GET', 'POST'])
def bloodstockCreate():
	msg = ''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT name FROM blooddonationsystemdb.tbl_bloodbank")
	if users > 0:
		bloodBankIdDisplay = cursor.fetchall()

	users=cursor.execute("SELECT * FROM blooddonationsystemdb.tbl_donor")
	if users > 0:
		bloodDonorIdDisplay = cursor.fetchall()

	if request.method == 'POST' and 'donorId' in request.form and 'bloodBankId' in request.form and 'quantity' in request.form and 'expirDate' in request.form:
		var_donorName = request.form['donorId']
		var_bloodBankName= request.form['bloodBankId']
		var_quantity = request.form['quantity']
		var_expirDate = request.form['expirDate']
		
		var_donorNameSplitted=var_donorName.split()
		users0 = cursor.execute("SELECT idDonor FROM blooddonationsystemdb.tbl_donor where firstName = %s and lastName=%s", (var_donorNameSplitted[0],var_donorNameSplitted[1]))
		if users0 > 0:
			var_bloodDonorId = cursor.fetchall()

		users1 = cursor.execute("SELECT idBloodbank FROM blooddonationsystemdb.tbl_bloodbank where name=%s", (var_bloodBankName,))
		if users1 > 0:
			var_bloodBankId = cursor.fetchall()

		users2 = cursor.execute("SELECT bloodGroup FROM blooddonationsystemdb.tbl_donor where idDonor=%s",(var_bloodDonorId,))
		if users2 > 0:
			var_bloodGroup = cursor.fetchall()

		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("INSERT INTO `blooddonationsystemdb`.`tbl_bloodstock` (`idBloodBank`, `bloodGroup`, `quantity`, `expirationDate`, `donorId`) VALUES (%s,%s,%s,%s,%s)",( var_bloodBankId, var_bloodGroup, var_quantity, var_expirDate,var_bloodDonorId))
		mysql.connection.commit()
		msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('bloodstockCreate.html', bloodBankIdDisplay = bloodBankIdDisplay,bloodDonorIdDisplay=bloodDonorIdDisplay,msg=msg)


@app.route('/requestCreate', methods=['GET', 'POST'])
def requestCreate():
	msg = ''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT * FROM blooddonationsystemdb.tbl_seeker")
	if users > 0:
		seekerIdDisplay = cursor.fetchall()

	users = cursor.execute("SELECT name FROM blooddonationsystemdb.tbl_bloodbank")
	if users > 0:
		bloodBankIdDisplay = cursor.fetchall()

	if request.method == 'POST' and 'seekerId' in request.form and 'bloodBankId' in request.form and 'approval' in request.form and 'reqDate' in request.form:
		var_seekerName = request.form['seekerId']
		var_bloodBankName = request.form['bloodBankId']
		var_approval = request.form['approval']
		var_reqDate = request.form['reqDate']
		var_seekerNameSplitted = var_seekerName.split()
		users0 = cursor.execute("SELECT idSeeker FROM blooddonationsystemdb.tbl_seeker where firstName = %s and LastName=%s",(var_seekerNameSplitted[0],var_seekerNameSplitted[1]))
		if users0 > 0:
			var_seekerId = cursor.fetchall()

		users1 = cursor.execute("SELECT idBloodbank FROM blooddonationsystemdb.tbl_bloodbank where name=%s",(var_bloodBankName,))
		if users1 > 0:
			var_bloodBankId = cursor.fetchall()

		users2 = cursor.execute("SELECT blodGroup FROM blooddonationsystemdb.tbl_seeker where idSeeker=%s",(var_seekerId,))
		if users2 > 0:
			var_bloodGroup = cursor.fetchall()

		users3 = cursor.execute("SELECT quantity FROM blooddonationsystemdb.tbl_bloodstock where bloodGroup=%s order by expirationDate desc",(var_bloodGroup,))
		if users3 > 0:
			var_bloodQuantity = cursor.fetchall()
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute("INSERT INTO `blooddonationsystemdb`.`tbl_request` (`requestDate`, `idSeeker`, `quantity`, `idBloodBank`, `Approved`) VALUES (%s,%s,%s,%s,%s)",(var_reqDate, var_seekerId, var_bloodQuantity, var_bloodBankId, var_approval))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
		else:
			flash('No blood bag with requiered blood group in stock!')


	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('requestCreate.html', seekerIdDisplay=seekerIdDisplay,   bloodBankIdDisplay=bloodBankIdDisplay, msg=msg)


@app.route('/categoriesdisplay')
def categoriesdisplay():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM categories_movies.category")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('categoriesdisplay.html',displayVector=displayVector)

@app.route('/moviesdisplay')
def moviesdisplay():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM categories_movies.movie")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('moviesdisplay.html',displayVector=displayVector)

@app.route('/screeningdisplay')
def screeningdisplay():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM categories_movies.screening")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('screeningdisplay.html',displayVector=displayVector)

@app.route('/categorydelete', methods =['GET', 'POST'])
def categorydelete():
	msg = ''
	if request.method == 'POST' and 'idcat' in request.form:
		idcat=request.form['idcat']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("delete from categories_movies.category where idCategory=%s;", (idcat,))
		mysql.connection.commit()
		msg = 'You have successfully deleted'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template("categorydelete.html",msg=msg)

@app.route('/moviedelete', methods =['GET', 'POST'])
def moviedelete():
	msg = ''
	if request.method == 'POST' and 'idmovie' in request.form:
		idmovie=request.form['idmovie']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("delete from categories_movies.movie where idMovie=%s;", (idmovie,))
		mysql.connection.commit()
		msg = 'You have successfully deleted'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template("moviedelete.html",msg=msg)

@app.route('/screeningdelete', methods =['GET', 'POST'])
def screeningdelete():
	msg = ''
	if request.method == 'POST' and 'idscreening' in request.form:
		idscreening=request.form['idscreening']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("delete from categories_movies.screening where idScreening=%s;", (idscreening,))
		mysql.connection.commit()
		msg = 'You have successfully deleted'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template("screeningdelete.html",msg=msg)

@app.route('/categoryupdate', methods=['GET','POST'])
def categoryupdate():
	msg=''
	if request.method == 'POST' and 'idcat' in request.form and 'name' in request.form and 'target_audience' in request.form and 'setting' in request.form and 'theme' in request.form and 'production' in request.form:
		idcat=request.form['idcat']
		name = request.form['name']
		target_audience = request.form['target_audience']
		setting = request.form['setting']
		theme = request.form['theme']
		production = request.form['production']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE categories_movies.category SET name=%s,target_audience=%s,setting=%s,theme=%s,production=%s WHERE idCategory=%s;",(name, target_audience, setting, theme, production,idcat))
		mysql.connection.commit()
		msg = 'You have successfully updated !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('categoryupdate.html', msg = msg)


@app.route('/movieupdate', methods =['GET', 'POST'])
def movieupdate():
	msg = ''
	if request.method == 'POST' and 'idmovie' in request.form and 'title' in request.form and 'pg_rating' in request.form and 'budget' in request.form and 'director' in request.form and 'language' in request.form and 'release_date' in request.form and 'avg_reviews' in request.form and 'length' in request.form:
		idmovie=request.form['idmovie']
		title = request.form['title']
		pg_rating = request.form['pg_rating']
		budget = request.form['budget']
		director = request.form['director']
		language = request.form['language']
		release_date = request.form['release_date']
		avg_reviews = request.form['avg_reviews']
		length = request.form['length']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE `categories_movies`.`movie` SET `Title` = %s, `pg_rating` = %s, `budget` = %s, `Director` = %s, `Language` = %s, `release_date` = %s, `average_reviews` = %s, `length` = %s WHERE (`idMovie` = %s);",(title, pg_rating, budget, director, language, release_date, avg_reviews, length,idmovie))
		mysql.connection.commit()
		msg = 'You have successfully updated !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('movieupdate.html', msg = msg)

@app.route('/screeningupdate', methods =['GET', 'POST'])
def screeningupdate():
	msg = ''
	if request.method == 'POST' and 'idScreening' in request.form and 'idmovie' in request.form and 'idcat' in request.form and 'cinema' in request.form and 'ticket_price' in request.form and 'date' in request.form and 'time' in request.form and 'location' in request.form and 'seats_left' in request.form:
		idscreening=request.form['idScreening']
		idMovie = request.form['idmovie']
		idCat = request.form['idcat']
		cinema = request.form['cinema']
		ticket_price = request.form['ticket_price']
		date = request.form['date']
		time = request.form['time']
		location = request.form['location']
		seats_left = request.form['seats_left']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE `categories_movies`.`screening` SET `idMovie` = %s, `idCategory` = %s, `cinema`= %s, `ticket_price` = %s, `date` = %s, `time` = %s, `location` = %s, `seats_left` = %s WHERE (`idScreening` = %s);",(idMovie, idCat, cinema, ticket_price, date, time, location, seats_left,idscreening))
		mysql.connection.commit()
		msg = 'You have successfully updated !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('screeningupdate.html', msg = msg)


@app.route('/moviesANDscreeningdisplay')
def moviesANDscreeningdisplay():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT m.Title, m.pg_rating, m.Language,m.length,s.cinema,s.location,s.date,s.time,s.ticket_price, s.seats_left FROM categories_movies.movie m inner join categories_movies.screening s using (idMovie);")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('moviesANDscreeningdisplay.html',displayVector=displayVector)

app.debug = True

toolbar = DebugToolbarExtension(app)

if __name__ == "__main__":
	app.run(host ="localhost", port = int("5000"),debug=True)
