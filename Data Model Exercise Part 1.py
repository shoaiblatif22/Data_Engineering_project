#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('pip install psycopg2')


# In[3]:


import psycopg2


# In[4]:


try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password= ")
except psycopg2.Error as e:
    print ("Error: Could not make connection to the Postgres database")
    print(e)


# In[7]:


try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)


# In[6]:


conn.set_session(autocommit=True)


# In[9]:


try:
    cur.execute("create database myfirstdb")
except psycopg2.Error as e:
    print(e)


# In[19]:


try:
    conn.close()
except psycopg2.Error as e:
    print(e)
    
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=myfirstdb user=postgres password =")
except psycopg2.Error as e:
    print ("Error: Could not make connection to the Postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopgy2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)
    
conn.set_session(autocommit=True)


# In[20]:


try:
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar,     age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)


# In[23]:


try:   
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks)     VALUES (%s, %s, %s, %s, %s, %s)",     (1, "Raj", 23, "Male", "Python", 85))
    
    conn.commit()
    print("Row inserted successfully.")

except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)
    
try:   
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks)     VALUES (%s, %s, %s, %s, %s, %s)",     (2, "Priya", 22, "Female", "Python", 86))
    
    conn.commit()
    print("Row inserted successfully.")

except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)


# In[25]:


try:
      
    cur.execute("SELECT * FROM students;")
    
    row = cur.fetchone()
    while row:
        print(row)
        row = cur.fetchone()

except psycopg2.Error as e:
    print("Error: Selecting Rows")
    print(e)


# In[26]:


cur.close()
conn.close()


# In[ ]:




