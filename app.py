


import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 

# loading in the model to predict on the data 
pickle_in = open('logreg.pkl', 'rb') 
classifier = pickle.load(pickle_in) 

def welcome(): 
	return 'welcome all'

# defining the function which will make the prediction using 
# the data which the user inputs 
def prediction(gender,race_ethnicity,parental_level_of_education,lunch,test_preperation_course,math_score,reading_score,writing_score,pass_math,pass_reading,pass_writing,total_score,percentage,status): 

	prediction = classifier.predict( 
		[[gender,race_ethnicity,parental_level_of_education,lunch,test_preperation_course,math_score,reading_score,writing_score,pass_math,pass_reading,pass_writing,total_score,percentage,status]]) 
	print(prediction) 
	return prediction 
	

# this is the main function in which we define our webpage 
def main(): 
	# giving the webpage a title 
	st.title("Student Grade Prediction") 
	
	# here we define some of the front end elements of the web page like 
	# the font and background color, the padding and the text to be displayed 
	html_temp = """ 
	<div style ="background-color:yellow;padding:13px"> 
	<h1 style ="color:black;text-align:center;">Student Grade Classifier ML App </h1> 
	</div> 
	"""
	
	# this line allows us to display the front end aspects we have 
	# defined in the above code 
	st.markdown(html_temp, unsafe_allow_html = True) 
	
	# the following lines create text boxes in which the user can enter 
	# the data required to make the prediction 
	gender1 = st.text_input("gender") 
	race_ethnicity = st.text_input("race/ethnicity") 
	parental_level_of_education = st.number_input("parental level of education") 
	lunch = st.text_input("lunch") 
	test_preperation_course=st.text_input("test preperation course")
	math_score = st.number_input("math_score1") 
	reading_score = st.number_input("reading_score1") 
	writing_score = st.number_input("writing_score1") 
	# math_score=int(math_score1)
	# reading_score=int(reading_score1)
	# writing_score=int(writing_score1)
	if(gender1=='female'):
		gender=0
	else:
		gender=1
	if(race_ethnicity=='group A'):
		race_ethnicity=1
	elif(race_ethnicity=='group B'):
		race_ethnicity=2
	elif(race_ethnicity=='group C'):
		race_ethnicity=3
	elif(race_ethnicity=='group D'):
		race_ethnicity=4
	elif(race_ethnicity=='group E'):
		race_ethnicity=5
	if(test_preperation_course=='none'):
		test_preperation_course=1
	else:
		test_preperation_course=0

		
	if(lunch=='standard'):
		lunch=1
	else:
		lunch=0
	
	

	pass_mark=40
	if reading_score<40:
		pass_reading=0
	else:
		pass_reading=1
	if math_score<40:
		pass_math=0
	else:
		pass_math=1
	if writing_score<40:
		pass_writing=0
	else:
		pass_writing=1
	total_score=math_score+reading_score+writing_score
	percentage=total_score/3
	if (pass_math==0) or (pass_reading==0) or (pass_writing==0):
		status=0
	else:
		status=1
	result ="" 
	
	# the below line ensures that when the button called 'Predict' is clicked, 
	# the prediction function defined above is called to make the prediction 
	# and store it in the variable result 
	if st.button("Predict"): 
		result = prediction(gender,race_ethnicity,parental_level_of_education,lunch,test_preperation_course,math_score,reading_score,writing_score,pass_math,pass_reading,pass_writing,total_score,percentage,status) 
	st.success('The output is {}'.format(result)) 
	
if __name__=='__main__': 
	main() 

