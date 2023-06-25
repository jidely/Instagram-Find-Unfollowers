import instaloader
from tkinter import *
from tkinter.font import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

# Screen Settings
screen = Tk()
canvas = Canvas(screen, width=500,height=500)
"""
screen.title('Tab Widget')
tabControl = ttk.Notebook(screen)

tab1= ttk.Frame(tabControl)
tab2= ttk.Frame(tabControl)

tabControl.add(tab1, text ='Followers-Followees')
tabControl.add(tab2, text ='Images,Stories')

tabControl.pack(expand = 1, fill ="both")"""

canvas.pack()

def listfollowers():

    # Initialize the Instaloader
    L = instaloader.Instaloader()
    
    username = mail_field.get()
    password = password_field.get()

    # Login to Instagram
    L.login(username, password)

    # Get the profile of the logged-in user
    profile = instaloader.Profile.from_username(L.context, username)

    # Print the number of followers and following
    print("Followers: {}".format(profile.followers))
    print("Following: {}".format(profile.followees))

   
   #Erase the file 
    if os.path.exists("followers.txt"):
        os.remove("followers.txt")
    if os.path.exists("followees.txt"):
        os.remove("followees.txt")


    # Get the list of followers and following
    for followers in profile.get_followers():
        with open("followers.txt","a+") as f:
            file = f.write(followers.username+'\n')
        
        print("Writing followers...")
        print(file)
    
    for followees in profile.get_followees():
        with open("followees.txt","a+") as f:
            file = f.write(followees.username+'\n')
         
        print("Writing followees...")
        print(file)

    form = cmb.get()

    if form == 'Followers Doesnt Follow Back':
        # Find the users in the following list that are not in the followers list
        

        followers_file = set(open("followers.txt").readlines())
        followees_file = set(open("followees.txt").readlines())
        
        unfollowers_set = followees_file.difference(followers_file)
        unfollowers_file = open('unfollowers.txt','r+')

        for unfollowers in unfollowers_set:
            unfollowers_file.write(unfollowers)

    elif form == 'Followers I Dont Follow Back':
        followers_file = set(open("followers.txt").readlines())
        followees_file = set(open("followees.txt").readlines())
        
        notfollowing_set = followers_file.difference(followees_file)
        notfollowing_file = open('notfollowing.txt','r+')

        for notfollowing in notfollowing_set:
            notfollowing_file.write(notfollowing) 
    
    # Show the results in a message box

# Title image
screen.iconbitmap('İnstagram/instagramlogo.ico') #add your image path
title = screen.title('Instagram Follows')


# Open image
in_logo = Image.open('İnstagram/instagramlog.png') #add your image path

# Resize image
resized = in_logo.resize((200,100), Image.ANTIALIAS)
insta_logo = ImageTk.PhotoImage(resized)

canvas.create_image(250,0,anchor='n',image=insta_logo)
canvas.pack()


# Account Info  Entry
mail_field = Entry(screen,width=20)
mail_lable = Label(screen,text='Username or Mail:', font=('Helvetica',12,BOLD), fg ='#8c0a28')
password_field = Entry(screen,width=20)
password_lable = Label(screen,text='Password:', font=('Helvetica',12,BOLD), fg ='#8c0a28')

# Password mask
password_field.config(show='*')

# Account Info Location
canvas.create_window(250,175,window=mail_field)
canvas.create_window(220,150,window=mail_lable)
canvas.create_window(250,225,window=password_field)
canvas.create_window(220,200,window=password_lable)

# Password field mask-unmask
def unmaskpassword():
    if c_v1.get() == 1:
        password_field.config(show='')
    else :
        password_field.config(show='*')

c_v1 = IntVar(value=0)

unmaskbutton = Checkbutton(screen, text="Show password", variable=c_v1, onvalue=1,offvalue=0, command=unmaskpassword)
canvas.create_window(350,225, window=unmaskbutton)



# Cmb Create
followlist = [
    'Followers I Dont Follow Back',
    'Followers Doesnt Follow Back'
]

cmb = ttk.Combobox(screen, value= followlist, width=40)
canvas.create_window(140,300,window=cmb)
# Cmb label
cmb_label = Label(screen,text='Choose one:',font=('Helvetica',10),fg='black')
canvas.create_window(50,300,window=cmb_label)
    

# List Button
list_button = Button(screen,text='List', fg='white', bg='red',command=listfollowers)
canvas.create_window(250,270,window=list_button)

canvas.pack()
screen.mainloop()