from firebase import firebase

fb = firebase.FirebaseApplication('https://wawansample.firebaseio.com/',None)

def fedit(sname,semail,sschool,sgrade):
	data = {}
	data['email'] = semail
	data['school'] = sschool
	data['grade'] = sgrade

	g = fb.get('student_details', sname)

	if g == None:
		c1 = fb.put('student_details', name=sname, data=data)
		text0 = 'Success new student data created'		
		return text0

	elif g['email'] == semail and g['school'] == sschool and g['grade'] == sgrade:
		text = 'Student details already present, No changes were made'		
		return text

	else:	
		c2 = fb.put('student_details', name=sname, data=data)
		text1 = 'Student data has been updated'
		return text1

def fdelete(sname,semail):
	
	d = fb.get('student_details',sname)

	if d == None:
		text2 = 'Cannot delete please check the student name and email you entered'
		return text2

	elif d['email']==semail:
		d1 = fb.delete('student_details', sname)
		text3 = 'Student data deleted successfully'
		return text3
	
	else:
		text4 = 'Cannot delete please check the student name and email you entered'
		return text4

def fview(sname,semail):

	v = fb.get('student_details',sname)

	if v == None:
		text5 = 'Cannot find student please check the name and email you entered'
		return text5

	elif v['email']==semail:
		student_name = sname
		student_email = semail
		student_school = v['school']
		student_grade = v['grade']
		text6 =  'Student Name: '+student_name+', Student e-mail: '+student_email+', Student school: '+student_school+', Student grade: '+student_grade
		return text6

	else:
		text7 = 'Canot find student please check the name and email you entered'
		return text7