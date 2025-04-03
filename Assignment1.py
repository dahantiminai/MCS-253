"""Assignment 1 - MCS253
Creating Python Objects ~ Lists, Tuples, Dictionaries"""

#Due Date - Submit no later than 4:10 pm on Thursday (3rd April 2025)

#Please type in your name in the next line by way of commenting

#Name: ___________
#Dahan Timinai

#----------------------------------------------------------------

#Quesiton 1

"""Create a python object to store all the courses you are taking this semester.
You may be required to change a course next week."""

# List of courses for the current semester
courses_this_semester = ["MCS 251 - Data Structures and Algorithm 1", "MCS 253 - Computer Programming 1", "MA 221 - Calculus 1", "MA 211 - Set Theory and Logic", "MA 241 - Discrete Mathematics"]



#Question 2

"""Store all MCS 253 students ID in a python object. These IDs will be
used for 4 years thus do not change IDs."""

# Tuple of MCS 253 student IDs (immutable to ensure IDs do not change)
mcs_253_ids = ("202412245", "202412236", "202412232", "2023314260", "2023314233", "202412253")


#Question 3
"""Since students IDs are a unique identifying number for each student, 

use it as a reference to point to students records. The students records
should consist of full names, gender, DOB,Province of origin & email addresses."""

# Each of these dictionaries (student_1, etc.) stores the details of a single student,
# including their full name, gender, date of birth, province of origin, and email address.
student_1 = {
    "full_name": "Margreth Kuri",
    "gender": "Female",
    "dob": "18/12/1998",
    "province": "Jiwaka",
    "email": "202412245@stu.unigoroka.ac.pg"
    }

student_2 = {
    "full_name": "Natasha Ricky",
    "gender": "Female",
    "dob": "05/07/1998",
    "province": "Eastern Highlands",
    "email": "202412236@stu.unigoroka.ac.pg"
    }

student_3 = {
    "full_name": "Dahan Timinai",
    "gender": "Male",
    "dob": "11/11/2001",
    "province": "Western",
    "email": "timinaidahan@gmail.com"
    }

student_4 = {
    "full_name": "Jonah Albert",
    "gender": "Male",
    "dob": "09/05/2004",
    "province": "Central",
    "email": "2023314260@stu.unigoroka.ac.pg"
    }

student_5 = {
    "full_name": "Rophie Nomoru",
    "gender": "Male",
    "dob": "19/10/2002",
    "province": "Morobe",
    "email": "2023314233@stu.unigoroka.ac.pg"
    }

student_6 = {
    "full_name": "Junior Robert",
    "gender": "Male",
    "dob": "12/10/2000",
    "province": "Jiwaka",
    "email": "202412253@stu.unigoroka.ac.pg"
    }

# This dictionary (student_records) maps each student ID from the mcs_253_ids tuple
# to the corresponding student record (inner dictionary) containing their details.
student_records = {
    mcs_253_ids[0]: student_1,
    
    mcs_253_ids[1]: student_2,
    
    mcs_253_ids[2]: student_3,
    
    mcs_253_ids[3]: student_4,
    
    mcs_253_ids[4]: student_5,
    
    mcs_253_ids[5]: student_6
    }


#Question 4
"""Using indexing, print out your favorite course for the sem (refer to Q1)"""

# print("My favorite course for this semester is", courses_this_semester[1], "\b.")



#Question 5
"""Print out only your student ID from Q2"""

# print("My student ID is", mcs_253_ids[2], "\b.")



#Question 6
"""Print out all students records (exclude the IDs)"""

# Loops through all student records (excluding IDs) and prints each record.
# Each record is printed with its details on separate lines.
# A blank line is added after each record for better readability.
"""
for record in student_records.values():
    print("Record:")
    for key, value in record.items():
        print(f"  {key}: {value}")
    print()
"""
# Alternatively, you can directly print all student records (excluding IDs) for quicker output and simplicity.
# print("Student Records:\n", list((student_records.values())))

#Question 7
"""Print out only your student record"""

# Retrieves and prints only my student record from the student_records dictionary.
# Each detail (e.g., full name, gender, etc.) is printed on a separate line for better readability.
"""
my_record = student_records["202412232"]

print("My Student Record:")
for key, value in my_record.items():
    print(f"  {key}: {value}")
"""

# Alternatively, you can directly print only my student record for quicker output and simplicity.
#print("My Student Record:\n", student_records.get(mcs_253_ids[2]))


#Question 8
"""Update the student ID in Q2.
What is the error here?
WHy do you think this happened"""

# mcs_253_ids[2] = "202412233"

# This code attempts to update the value at index 2 in the tuple mcs_253_ids to "202412233".
# This raises an error (a TypeError)
# This is because tuples are immutable in Python, meaning their elements cannot be changed after they are created.



#Question 9
"""Print out the data types for all the objects you have created so far"""
"""
print("Data type of course_this_semester:\n", type(courses_this_semester))
print()
print("Data type of mcs_253_ids:\n", type(mcs_253_ids))
print()
print("Data type of student_records:\n", type(student_records))
"""
#------end of Assignment
#UPLOAD your completed A1 to your GitHub account. Only share the link with me. 