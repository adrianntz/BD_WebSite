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

@app.route("/index/")
def index():
	return render_template("index.html")


@app.route('/createBloodbank', methods =['GET', 'POST'])
def createBloodbank():
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
	return render_template('createBloodbank.html', msg = msg)

@app.route('/createDonor', methods =['GET', 'POST'])
def createDonor():
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
	return render_template('createDonor.html', msg = msg)

@app.route('/createSeeker', methods =['GET', 'POST'])
def createSeeker():
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
	return render_template('createSeeker.html', msg = msg)

@app.route('/createBloodstock', methods =['GET', 'POST'])
def createBloodstock():
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
	return render_template('createBloodstock.html', bloodBankIdDisplay = bloodBankIdDisplay,bloodDonorIdDisplay=bloodDonorIdDisplay,msg=msg)


@app.route('/createRequest', methods=['GET', 'POST'])
def createRequest():
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
	return render_template('createRequest.html', seekerIdDisplay=seekerIdDisplay,   bloodBankIdDisplay=bloodBankIdDisplay, msg=msg)


@app.route('/readDonors')
def readDonors():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM blooddonationsystemdb.tbl_donor")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('readDonors.html',displayVector=displayVector)

@app.route('/readSeekers')
def readSeekers():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM blooddonationsystemdb.tbl_seeker")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('readSeekers.html',displayVector=displayVector)

@app.route('/readBloodBanks')
def readBloodBanks():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM blooddonationsystemdb.tbl_bloodbank")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('readBloodBanks.html',displayVector=displayVector)

@app.route('/readBloodstock')
def readBloodstock():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT bb.name, bs.bloodGroup, bs.quantity, bs.expirationDate, concat(concat(d.firstName,' '),d.lastName) FROM blooddonationsystemdb.tbl_bloodbank bb inner join blooddonationsystemdb.tbl_bloodstock bs on bs.idBloodBank = bb.idBloodbank inner join blooddonationsystemdb.tbl_donor d on bs.donorId=d.idDonor;")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('readBloodstock.html',displayVector=displayVector)

@app.route('/readRequests')
def readRequests():
    cursor = mysql.connection.cursor()
    users=cursor.execute("select r.requestDate, concat(concat(s.firstName,' '), s.lastName),r.quantity,bb.name,r.approved from tbl_request r inner join tbl_seeker s on r.idSeeker = s.idSeeker inner join tbl_bloodbank bb on r.idBloodBank=bb.idBloodbank;")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('readRequests.html',displayVector=displayVector)

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

@app.route('/updateDonor', methods=['GET','POST'])
def updateDonor():
	msg=''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT firstName,lastname FROM blooddonationsystemdb.tbl_donor")
	if users > 0:
		selectedDonorNameVect = cursor.fetchall()

	if request.method == 'POST' and 'firstName' in request.form and 'lastName' in request.form and 'dateBirth' in request.form and 'address' in request.form and 'bloodGroup' in request.form and 'cnp' in request.form:
		var_selectedName=request.form['donorName']
		var_selectedName=var_selectedName.split()
		users = cursor.execute("SELECT idDonor FROM blooddonationsystemdb.tbl_donor where firstName=%s and lastName=%s", (var_selectedName[0], var_selectedName[1]))
		if users > 0:
			donorId = cursor.fetchall()
		var_firstName = request.form['firstName']
		var_lastName = request.form['lastName']
		var_dateBirth = request.form['dateBirth']
		var_address = request.form['address']
		var_bloodGroup = request.form['bloodGroup']
		var_cnp = request.form['cnp']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE blooddonationsystemdb.tbl_donor SET firstName=%s,lastName=%s,date_of_birth=%s,location=%s,bloodGroup=%s,cnp=%s WHERE idDonor=%s;",(var_firstName, var_lastName, var_dateBirth, var_address, var_bloodGroup,var_cnp,donorId))
		mysql.connection.commit()
		msg = 'You have successfully updated !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('updateDonor.html', msg = msg,selectedDonorNameVect=selectedDonorNameVect)


@app.route('/updateSeekers', methods=['GET','POST'])
def updateSeekers():
	msg=''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT firstName,lastname FROM blooddonationsystemdb.tbl_seeker")
	if users > 0:
		selectedDonorNameVect = cursor.fetchall()

	if request.method == 'POST' and 'firstName' in request.form and 'lastName' in request.form and 'dateBirth' in request.form and 'address' in request.form and 'bloodGroup' in request.form and 'cnp' in request.form:
		var_selectedName=request.form['donorName']
		var_selectedName=var_selectedName.split()
		users = cursor.execute("SELECT idSeeker FROM blooddonationsystemdb.tbl_seeker where firstName=%s and lastName=%s", (var_selectedName[0], var_selectedName[1]))
		if users > 0:
			donorId = cursor.fetchall()
		var_firstName = request.form['firstName']
		var_lastName = request.form['lastName']
		var_dateBirth = request.form['dateBirth']
		var_address = request.form['address']
		var_bloodGroup = request.form['bloodGroup']
		var_cnp = request.form['cnp']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE blooddonationsystemdb.tbl_seeker SET firstName=%s,lastName=%s,date_of_birth=%s,location=%s,blodGroup=%s,cnp=%s WHERE idSeeker=%s;",(var_firstName, var_lastName, var_dateBirth, var_address, var_bloodGroup,var_cnp,donorId))
		mysql.connection.commit()
		msg = 'You have successfully updated !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('updateSeekers.html', msg = msg,selectedDonorNameVect=selectedDonorNameVect)

@app.route('/updateBloodBanks', methods=['GET','POST'])
def updateBloodBanks():
	msg=''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT name FROM blooddonationsystemdb.tbl_bloodbank")
	if users > 0:
		selectedBankNameVect = cursor.fetchall()

	if request.method == 'POST' and 'name' in request.form and 'address' in request.form and 'email' in request.form and 'phone' in request.form:
		var_selectedBank=request.form['bankName']
		var_name = request.form['name']
		var_address = request.form['address']
		var_email = request.form['email']
		var_phone = request.form['phone']
		users = cursor.execute("SELECT idBloodbank FROM blooddonationsystemdb.tbl_bloodbank where name=%s", (var_selectedBank,))
		if users > 0:
			bankId = cursor.fetchall()
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE blooddonationsystemdb.tbl_bloodbank SET name=%s,address=%s,email=%s,phone_number=%s WHERE idBloodbank=%s;",(var_name, var_address, var_email, var_phone, bankId))
		mysql.connection.commit()
		msg = 'You have successfully updated !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('updateBloodBanks.html', msg = msg,selectedBankNameVect=selectedBankNameVect)


@app.route('/updateBloodstock', methods=['GET', 'POST'])
def updateBloodstock():
	msg = ''
	cursor = mysql.connection.cursor()
	users=cursor.execute("select idBloodBag from blooddonationsystemdb.tbl_bloodstock")
	if users>0:
		bloodBagIdDisplay= cursor.fetchall()
	users = cursor.execute("SELECT name FROM blooddonationsystemdb.tbl_bloodbank")
	if users > 0:
		bloodBankIdDisplay = cursor.fetchall()

	users = cursor.execute("SELECT * FROM blooddonationsystemdb.tbl_donor")
	if users > 0:
		bloodDonorIdDisplay = cursor.fetchall()

	if request.method == 'POST' and 'donorId' in request.form and 'bloodBankId' in request.form and 'quantity' in request.form and 'expirDate' in request.form:
		var_bloodBagId=request.form['bloodBagId']
		var_donorName = request.form['donorId']
		var_bloodBankName = request.form['bloodBankId']
		var_quantity = request.form['quantity']
		var_expirDate = request.form['expirDate']
		var_donorNameSplitted = var_donorName.split()
		users0 = cursor.execute("SELECT idDonor FROM blooddonationsystemdb.tbl_donor where firstName = %s and lastName=%s",(var_donorNameSplitted[0], var_donorNameSplitted[1]))
		if users0 > 0:
			var_bloodDonorId = cursor.fetchall()

		users1 = cursor.execute("SELECT idBloodbank FROM blooddonationsystemdb.tbl_bloodbank where name=%s",(var_bloodBankName,))
		if users1 > 0:
			var_bloodBankId = cursor.fetchall()

		users2 = cursor.execute("SELECT bloodGroup FROM blooddonationsystemdb.tbl_donor where idDonor=%s",(var_bloodDonorId,))
		if users2 > 0:
			var_bloodGroup = cursor.fetchall()

		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE blooddonationsystemdb.tbl_bloodstock SET idBloodBank=%s,bloodGroup=%s,quantity=%s,expirationDate=%s,donorId=%s WHERE idBloodBag=%s;",(var_bloodBankId, var_bloodGroup, var_quantity, var_expirDate, var_bloodDonorId,var_bloodBagId))
		mysql.connection.commit()
		msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('updateBloodstock.html', bloodBankIdDisplay=bloodBankIdDisplay,bloodDonorIdDisplay=bloodDonorIdDisplay, bloodBagIdDisplay=bloodBagIdDisplay,msg=msg)

@app.route('/updateRequests', methods=['GET', 'POST'])
def updateRequests():
	msg = ''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT idRequest FROM blooddonationsystemdb.tbl_request")
	if users > 0:
		requestIdDIsplay = cursor.fetchall()

	users = cursor.execute("SELECT * FROM blooddonationsystemdb.tbl_seeker")
	if users > 0:
		seekerIdDisplay = cursor.fetchall()

	users = cursor.execute("SELECT name FROM blooddonationsystemdb.tbl_bloodbank")
	if users > 0:
		bloodBankIdDisplay = cursor.fetchall()

	if request.method == 'POST' and 'seekerId' in request.form and 'bloodBankId' in request.form and 'approval' in request.form and 'reqDate' in request.form:
		var_selectedId=request.form['requestId']
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
			cursor.execute("UPDATE blooddonationsystemdb.tbl_request SET `requestDate`=%s, `idSeeker`=%s, `quantity`=%s, `idBloodBank`=%s, `Approved`=%s where idRequest=%s",(var_reqDate, var_seekerId, var_bloodQuantity, var_bloodBankId, var_approval,var_selectedId))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
		else:
			flash('No blood bag with requiered blood group in stock!')


	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('updateRequests.html', seekerIdDisplay=seekerIdDisplay,   bloodBankIdDisplay=bloodBankIdDisplay,requestIdDIsplay=requestIdDIsplay, msg=msg)


@app.route('/deleteDonor', methods=['GET','POST'])
def deleteDonor():
	msg=''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT firstName,lastname FROM blooddonationsystemdb.tbl_donor")
	if users > 0:
		selectedDonorNameVect = cursor.fetchall()

	if request.method == 'POST' and 'donorName' in request.form:
		var_selectedName=request.form['donorName']
		var_selectedName=var_selectedName.split()
		users = cursor.execute("SELECT idDonor FROM blooddonationsystemdb.tbl_donor where firstName=%s and lastName=%s", (var_selectedName[0], var_selectedName[1]))
		if users > 0:
			donorId = cursor.fetchall()
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("delete from blooddonationsystemdb.tbl_donor WHERE idDonor=%s;",(donorId,))
		mysql.connection.commit()
		msg = 'You have successfully updated !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('deleteDonor.html', msg = msg,selectedDonorNameVect=selectedDonorNameVect)


@app.route('/deleteSeekers', methods=['GET','POST'])
def deleteSeekers():
	msg=''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT firstName,lastname FROM blooddonationsystemdb.tbl_seeker")
	if users > 0:
		selectedDonorNameVect = cursor.fetchall()

	if request.method == 'POST' and 'firstName' in request.form and 'lastName' in request.form and 'dateBirth' in request.form and 'address' in request.form and 'bloodGroup' in request.form and 'cnp' in request.form:
		var_selectedName=request.form['donorName']
		var_selectedName=var_selectedName.split()
		users = cursor.execute("SELECT idSeeker FROM blooddonationsystemdb.tbl_seeker where firstName=%s and lastName=%s", (var_selectedName[0], var_selectedName[1]))
		if users > 0:
			donorId = cursor.fetchall()
		var_firstName = request.form['firstName']
		var_lastName = request.form['lastName']
		var_dateBirth = request.form['dateBirth']
		var_address = request.form['address']
		var_bloodGroup = request.form['bloodGroup']
		var_cnp = request.form['cnp']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE blooddonationsystemdb.tbl_seeker SET firstName=%s,lastName=%s,date_of_birth=%s,location=%s,blodGroup=%s,cnp=%s WHERE idSeeker=%s;",(var_firstName, var_lastName, var_dateBirth, var_address, var_bloodGroup,var_cnp,donorId))
		mysql.connection.commit()
		msg = 'You have successfully updated !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('deleteSeekers.html', msg = msg,selectedDonorNameVect=selectedDonorNameVect)

@app.route('/deleteBloodBanks', methods=['GET','POST'])
def deleteBloodBanks():
	msg=''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT name FROM blooddonationsystemdb.tbl_bloodbank")
	if users > 0:
		selectedBankNameVect = cursor.fetchall()

	if request.method == 'POST' and 'name' in request.form and 'address' in request.form and 'email' in request.form and 'phone' in request.form:
		var_selectedBank=request.form['bankName']
		var_name = request.form['name']
		var_address = request.form['address']
		var_email = request.form['email']
		var_phone = request.form['phone']
		users = cursor.execute("SELECT idBloodbank FROM blooddonationsystemdb.tbl_bloodbank where name=%s", (var_selectedBank,))
		if users > 0:
			bankId = cursor.fetchall()
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE blooddonationsystemdb.tbl_bloodbank SET name=%s,address=%s,email=%s,phone_number=%s WHERE idBloodbank=%s;",(var_name, var_address, var_email, var_phone, bankId))
		mysql.connection.commit()
		msg = 'You have successfully updated !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('deleteBloodBanks.html', msg = msg,selectedBankNameVect=selectedBankNameVect)


@app.route('/deleteBloodstock', methods=['GET', 'POST'])
def deleteBloodstock():
	msg = ''
	cursor = mysql.connection.cursor()
	users=cursor.execute("select idBloodBag from blooddonationsystemdb.tbl_bloodstock")
	if users>0:
		bloodBagIdDisplay= cursor.fetchall()
	users = cursor.execute("SELECT name FROM blooddonationsystemdb.tbl_bloodbank")
	if users > 0:
		bloodBankIdDisplay = cursor.fetchall()

	users = cursor.execute("SELECT * FROM blooddonationsystemdb.tbl_donor")
	if users > 0:
		bloodDonorIdDisplay = cursor.fetchall()

	if request.method == 'POST' and 'donorId' in request.form and 'bloodBankId' in request.form and 'quantity' in request.form and 'expirDate' in request.form:
		var_bloodBagId=request.form['bloodBagId']
		var_donorName = request.form['donorId']
		var_bloodBankName = request.form['bloodBankId']
		var_quantity = request.form['quantity']
		var_expirDate = request.form['expirDate']
		var_donorNameSplitted = var_donorName.split()
		users0 = cursor.execute("SELECT idDonor FROM blooddonationsystemdb.tbl_donor where firstName = %s and lastName=%s",(var_donorNameSplitted[0], var_donorNameSplitted[1]))
		if users0 > 0:
			var_bloodDonorId = cursor.fetchall()

		users1 = cursor.execute("SELECT idBloodbank FROM blooddonationsystemdb.tbl_bloodbank where name=%s",(var_bloodBankName,))
		if users1 > 0:
			var_bloodBankId = cursor.fetchall()

		users2 = cursor.execute("SELECT bloodGroup FROM blooddonationsystemdb.tbl_donor where idDonor=%s",(var_bloodDonorId,))
		if users2 > 0:
			var_bloodGroup = cursor.fetchall()

		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("UPDATE blooddonationsystemdb.tbl_bloodstock SET idBloodBank=%s,bloodGroup=%s,quantity=%s,expirationDate=%s,donorId=%s WHERE idBloodBag=%s;",(var_bloodBankId, var_bloodGroup, var_quantity, var_expirDate, var_bloodDonorId,var_bloodBagId))
		mysql.connection.commit()
		msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('deleteBloodstock.html', bloodBankIdDisplay=bloodBankIdDisplay,bloodDonorIdDisplay=bloodDonorIdDisplay, bloodBagIdDisplay=bloodBagIdDisplay,msg=msg)

@app.route('/deleteRequest', methods=['GET', 'POST'])
def deleteRequest():
	msg = ''
	cursor = mysql.connection.cursor()
	users = cursor.execute("SELECT idRequest FROM blooddonationsystemdb.tbl_request")
	if users > 0:
		requestIdDIsplay = cursor.fetchall()

	users = cursor.execute("SELECT * FROM blooddonationsystemdb.tbl_seeker")
	if users > 0:
		seekerIdDisplay = cursor.fetchall()

	users = cursor.execute("SELECT name FROM blooddonationsystemdb.tbl_bloodbank")
	if users > 0:
		bloodBankIdDisplay = cursor.fetchall()

	if request.method == 'POST' and 'seekerId' in request.form and 'bloodBankId' in request.form and 'approval' in request.form and 'reqDate' in request.form:
		var_selectedId=request.form['requestId']
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
			cursor.execute("UPDATE blooddonationsystemdb.tbl_request SET `requestDate`=%s, `idSeeker`=%s, `quantity`=%s, `idBloodBank`=%s, `Approved`=%s where idRequest=%s",(var_reqDate, var_seekerId, var_bloodQuantity, var_bloodBankId, var_approval,var_selectedId))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
		else:
			flash('No blood bag with requiered blood group in stock!')


	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('deleteRequest.html', seekerIdDisplay=seekerIdDisplay,   bloodBankIdDisplay=bloodBankIdDisplay,requestIdDIsplay=requestIdDIsplay, msg=msg)

app.debug = True

toolbar = DebugToolbarExtension(app)

if __name__ == "__main__":
	app.run(host ="localhost", port = int("5000"),debug=True)
