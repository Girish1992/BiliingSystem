from Tkinter import *
import sqlite3
import tkMessageBox
username = ("Tom")
password = ("")
usernameguess1 = ("")
passwordguess1 = ("")


#ignore the file writing part,I'll sort this out later.

file = open("userlogondata.txt", "w")
file.write("User Data:\n")

file = open("userlogondata.txt", "r")

def trylogin():
   print ("Trying to login...")
   if usernameguess == username:
       print ("Complete sucsessfull!")
       tkMessageBox.showinfo("-- COMPLETE --", "You Have Now Logged In.",icon="info")
   else:
       print ("Error: (Incorrect value entered)")
       tkMessageBox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")



#Gui Things
root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.title("Log-In")
root.geometry("200x150")



#Creating the username & password entry boxes
usernametext = Label(root, text="Username:")
usernameguess = Entry(root)
passwordtext = Label(root, text="Password:")
passwordguess = Entry(root, show="*")

usernameguess1 = usernameguess

#attempt to login button
attemptlogin = Button(text="Login", command=trylogin)

usernametext.pack()
usernameguess.pack()
passwordtext.pack()
passwordguess.pack()
attemptlogin.pack()
#Main Starter
root.mainloop()