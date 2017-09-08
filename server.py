from flask import Flask,render_template,redirect,session,request,flash
import re
# from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z.+_-]+$')
app=Flask(__name__)
app.secret_key="regform"
@app.route('/')
def form():
	return render_template('form.html')
@app.route('/submit',methods=['post'])
def validation():
	# session['first'] = request.form['first']
	# session['last'] = request.form['last']
	# session['email'] = request.form['email']
	# session['password'] = request.form['password']
	
	if request.form['first'] and request.form['last'] and request.form['date'] and request.form['email'] and request.form['password'] and request.form['confirm']:
		
		if not NAME_REGEX.match(request.form['first']):
			flash("Invalid First Name")
		elif not NAME_REGEX.match(request.form['last']):
			flash("Invalid Last Name")
		elif not EMAIL_REGEX.match(request.form['email']):
			flash("Invalid Email Adsress")
		elif len(request.form['password']) < 8:
			flash("Password Should Be Longer Than 8 Characters")
		elif request.form['password'] != request.form['confirm']:
			flash("Please Confirm Your Password Again")
		else:
			# try:
			#     if request.form['date'] != datetime.strptime(request.form['date'], "%Y-%m-%d").strftime('%Y-%m-%d'):
			#         raise ValueError
			#     else:
			    	
			# 		else:
			# 			flash("Password must contain at least one uppercase and one number")
		 #    except ValueError:
			#     flash("Please enter birthdate correctly")
			counter = [0,0]
			for i in request.form['password']:
				if i.isdigit():
					counter[0]+=1
				elif i.isupper():
					counter[1]+=1
			if counter[0] and counter[1]:
				flash("Registrate Successfully!")
				session['first'] = request.form['first']
				session['last'] = request.form['last']
				session['date'] = request.form['date']
				session['email'] = request.form['email']
				session['password'] = request.form['password']
	else:
		# print request.form['first']
		# print request.form['last']
		# print request.form['email']
		# print request.form['password']
		flash("Please complete the full form")
	return redirect('/')

app.run(debug=True)