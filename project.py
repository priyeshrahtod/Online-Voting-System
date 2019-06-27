from Tkinter import *
import MySQLdb as m

root = Tk()
root.title("Election 2018")
root.geometry("1295x745")
f=Frame(root, height = 745, width = 1295, bg = "white")
f.pack()

lb= Label(f, text = "Election 2018", width =50, height =1,font = ("Helvetica", 36, "bold italic"),fg="black",bg="gold")
lb.place(x=0,y=0)

db = m.connect(host="localhost", user="root", passwd="mysql98", db="election")
cur = db.cursor()   

def buttonClickadmin(self):
    fadmin=Frame(f, height = 400, width = 500, bg = "white")
    fadmin.place(x=400,y=250)

    lbuser=Label(fadmin, text = "Username : ", height = 1,font = ("", 22, "") ,bg = "white", fg="black")
    lbuser.place(x=0,y=60)
    
    euser=Entry(fadmin, width = 30)
    euser.place(x=250,y=70)
    
    lbpass=Label(fadmin, text = "Password : ",height = 1,font = ("", 22, "") ,bg = "white", fg="black")
    lbpass.place(x=0,y=160)
    epass=Entry(fadmin, width = 15,show="*")
    epass.place(x=250,y=170)
    
    def buttonClicklogin(self):
        fp = open("login.txt",'r')
        li = fp.readlines()
        flag = 0
        username = euser.get() + "\n"
        password = epass.get() + "\n"
        
        for i in range(0,len(li),2):
            if(li[i] == username and li[i+1] == password):
                flag=1
                break
        
        if(flag == 0):
            print("Invalid username or password")
            lbmsg=Label(fadmin,text="Invalid username or password!",font = ("", 12, ""),bg="white",fg="red")
            lbmsg.place(x=120,y=350)
    		
        else:
        	finfo = Frame(f, height=745, width=1295, bg="white")
        	finfo.pack()
        	xcor=100
        	ycor=50
        	cur.execute("SELECT * FROM results")
        	rows = cur.fetchall()
        	
        	lhead1 = Label(finfo,text="NAME",font=("",12,""),bg = "white", fg="black")
        	lhead1.place(x=xcor, y=ycor)
        	xcor+=350
        	
        	lhead2 = Label(finfo,text="AADHAR NUMBER",font=("",12,""),bg = "white", fg="black")
        	lhead2.place(x=xcor, y=ycor)
        	xcor+=200
        	
        	lhead3 = Label(finfo,text="AGE",font=("",12,""),bg = "white", fg="black")
        	lhead3.place(x=xcor, y=ycor)
        	xcor+=100
        	
        	lhead4 = Label(finfo,text="GENDER",font=("",12,""),bg = "white", fg="black")
        	lhead4.place(x=xcor, y=ycor)
        	xcor+=150
        	
        	lhead5 = Label(finfo,text="VOTE",font=("",12,""),bg = "white", fg="black")
        	lhead5.place(x=xcor, y=ycor)
        	ycor+=20
        	
        	for row in rows:
		    	ycor+=25
		    	xcor = 100
		    	
		    	l1 = Label(finfo,text=row[0],font=("",12,""),bg = "white", fg="black")
		    	l1.place(x=xcor,y=ycor)
		    	xcor+=350
		    	
		    	l2 = Label(finfo,text=row[1],font=("",12,""),bg = "white", fg="black")
		    	l2.place(x=xcor,y=ycor)
		    	xcor+=200
		    	
		    	l3 = Label(finfo,text=row[2],font=("",12,""),bg = "white", fg="black")
		    	l3.place(x=xcor,y=ycor)
		    	xcor+=100
		    	
		    	l4 = Label(finfo,text=row[3],font=("",12,""),bg = "white", fg="black")
		    	l4.place(x=xcor,y=ycor)
		    	xcor+=150
		    	
		    	l5= Label(finfo,text=row[4],font=("",12,""),bg = "white", fg="black")
		    	l5.place(x=xcor,y=ycor)
		    
        	def buttonClickstats(self):
        		fstats = Frame(finfo, height=745, width=1295, bg="white")
        		fstats.pack()
        		xcor=100
        		ycor=50
        		cur.execute("SELECT * FROM countvotes")
        		rows = cur.fetchall()
        		lhead1 = Label(fstats,text="PARTY",font=("",12,""),bg = "white", fg="black")
		    	lhead1.place(x=xcor, y=ycor)
		    	xcor+=350
		    	lhead2 = Label(fstats,text="VOTES",font=("",12,""),bg = "white", fg="black")
		    	lhead2.place(x=xcor, y=ycor)
		    	ycor+=20
		    	for row in rows:
		    		ycor+=25
		    		xcor = 100
		    		l1 = Label(fstats,text=row[0],font=("",12,""),bg = "white", fg="black")
		    		l1.place(x=xcor,y=ycor)
		    		xcor+=350
		    		l2 = Label(fstats,text=row[1],font=("",12,""),bg = "white", fg="black")
		    		l2.place(x=xcor,y=ycor)
		    		xcor+=200
		    	
		    	def buttonClickexit(self):
		    		fstats.destroy()
		    	
		    	bexit = Button(fstats, text="BACK", width=5, height=1, font=("",16,""), bg="gold", fg="black",activeforeground = "white", activebackground = "grey")
		    	bexit.place(x=600,y=650)
		    	bexit.bind('<Button-1>', buttonClickexit)
					
        	bstats = Button(finfo, text="STATS", width=5, height=1, font = ("", 16, ""),bg ="gold", fg = "black", activeforeground = "white", activebackground = "grey")
        	bstats.place(x=510,y=650)
        	bstats.bind('<Button-1>',buttonClickstats)
        	
        	def buttonClickback(self):
        		finfo.destroy()
        		fadmin.destroy()
        	
        	bback = Button(finfo, text="LOGOUT", width=7, height=1, font = ("", 16, ""),bg ="gold", fg = "black", activeforeground = "white", activebackground = "grey")
        	bback.place(x=640,y=650)
        	bback.bind('<Button-1>',buttonClickback)
		    
    blogin= Button(fadmin, text = "LOGIN", width = 5, height = 1, font = ("", 16, ""),bg ="gold", fg = "black", activeforeground = "white", activebackground = "grey")
    blogin.place(x=200,y=280)
    blogin.bind('<Button-1>',buttonClicklogin)
    
badmin= Button(f, text = "ADMIN", width = 8, height = 2, font = ("", 16, ""),bg ="gold", fg = "black", activeforeground = "white", activebackground = "grey")
badmin.place(x=200,y=150)
badmin.bind('<Button-1>',buttonClickadmin)

	    

def buttonClickuser(self):
	
    fuser=Frame(f, height = 400,width =500, bg = "white")
    fuser.place(x=400,y=250)

    lbname = Label(fuser, text = "Name : ", height = 1,font = ("", 22, "") ,bg = "white", fg="black")
    lbname.place(x=10, y=60)

    ename = Entry(fuser,width = 25)
    ename.place(x=250, y=70)

    lbage = Label(fuser, text = "Age : ", height = 1,font = ("", 22, "") ,bg = "white", fg="black")
    lbage.place(x=10, y=120)

    eage = Entry(fuser,width = 3)
    eage.place(x=250, y=130)

    lbgen = Label(fuser, text = "Gender : ", height = 1,font = ("", 22, "") ,bg = "white", fg="black")
    lbgen.place(x=10, y=180)

    varg = IntVar()
    rmale = Radiobutton(fuser,variable = varg, value = 1, text = " Male",font = ("", 12, ""), bg = "White",fg = "Black")    
    rmale.place(x=250, y=190)

    rfem = Radiobutton(fuser,variable = varg, value = 2, text = " Female",font = ("", 12, ""), bg = "White",fg = "Black")    
    rfem.place(x=350, y=190)

    lbadh = Label(fuser, text = "Aadhar no. : ", height = 1,font = ("", 22, "") ,bg = "white", fg="black")
    lbadh.place(x=10, y=240)

    eadh = Entry(fuser,width = 12)
    eadh.place(x=250, y=250)
	
    def buttonClicksub(self):
        name = ename.get()
        age = eage.get()
        adh = eadh.get()
        vote = "None"
        
        if(varg.get() == 1):
            gender = "Male"
        else:
            gender = "Female"
        
        check = 1
        
        if(len(adh) < 12):
            check = 0
        
        if(age < "18"):
            check = 0
        
        try:
            tmp = float(eadh.get())
        except ValueError:
            check = 0
        
        try:
            tmp = int(eage.get())
        except ValueError:
            check = 0   
            
        if(check == 0):
        	lbmsg=Label(fuser,text="Invalid details!",font = ("", 12, ""),bg="white",fg="red")
        	lbmsg.place(x=190,y=370)
            
        else:
		    fvote=Frame(f,height=745,width=1295,bg="white")
		    fvote.pack()

		    lb= Label(fvote,text = "Election 2018", width =50, height =1,font = ("Helvetica", 36, "bold italic"),fg="black",bg="gold")
		    lb.place(x=0,y=0)

		    lbtitle= Label(fvote,text="Candidate List",height = 1,font = ("", 22, "bold underline") ,bg = "white", fg="black")
		    lbtitle.place(x=180,y=100)

		    lbvote= Label(fvote,text="Vote",height = 1,font = ("", 22, "bold underline") ,bg = "white", fg="black")
		    lbvote.place(x=950,y=100)

		    vargv = IntVar()
		    
		    lb1= Label(fvote,text="Rajneesh Kumar",height = 1,font = ("", 16, "") ,bg = "white", fg="black")
		    lb1.place(x=200,y=180)
		    
		    r1 = Radiobutton(fvote,variable = vargv, value = 1, bg = "white",fg = "Black")    
		    r1.place(x=970, y=180)

		    lb2= Label(fvote,text="Abhishek Mulchandani",height = 1,font = ("", 16, "") ,bg = "white", fg="black")
		    lb2.place(x=200,y=260)

		    r2 = Radiobutton(fvote,variable = vargv, value = 2, bg = "white",fg = "Black")    
		    r2.place(x=970, y=260)

		    lb3= Label(fvote,text="Esha Pabari",height = 1,font = ("", 16, "") ,bg = "white", fg="black")
		    lb3.place(x=200,y=340)

		    r3 = Radiobutton(fvote,variable = vargv, value = 3, bg = "white",fg = "Black")    
		    r3.place(x=970, y=340)

		    lb4= Label(fvote,text="Rutuja Pawar",height = 1,font = ("", 16, "") ,bg = "white", fg="black")
		    lb4.place(x=200,y=420)

		    r4 = Radiobutton(fvote,variable = vargv, value = 4, bg = "white",fg = "Black")    
		    r4.place(x=970, y=420)

		    lb5= Label(fvote,text="Aadil Mukhi",height = 1,font = ("", 16, "") ,bg = "white", fg="black")
		    lb5.place(x=200,y=500)

		    r5 = Radiobutton(fvote,variable = vargv, value = 5, bg = "white",fg = "Black")    
		    r5.place(x=970, y=500)

		    lb6= Label(fvote,text="Samvit Patankar",height = 1,font = ("", 16, "") ,bg = "white", fg="black")
		    lb6.place(x=200,y=580)

		    r6 = Radiobutton(fvote,variable = vargv, value = 6, bg = "white",fg = "Black")    
		    r6.place(x=970, y=580)
		    
		    img1 = PhotoImage(file = "rajneesh.png")
		    lbimg1 = Label(fvote,image = img1)
		    lbimg1.image = img1
		    lbimg1.place(x=100,y=180)

		    img2 = PhotoImage(file = "abhishek.png")
		    lbimg2 = Label(fvote,image = img2)
		    lbimg2.image = img2
		    lbimg2.place(x=100,y=260)

		    img3 = PhotoImage(file = "esha.png")
		    lbimg3 = Label(fvote,image = img3)
		    lbimg3.image = img3
		    lbimg3.place(x=100,y=340)

		    img4 = PhotoImage(file = "rutuja.png")
		    lbimg4 = Label(fvote,image = img4)
		    lbimg4.image = img4
		    lbimg4.place(x=100,y=420)

		    img5 = PhotoImage(file = "aadil.png")
		    lbimg5 = Label(fvote,image = img5)
		    lbimg5.image = img5
		    lbimg5.place(x=100,y=500)

		    img6 = PhotoImage(file = "samvit.png")
		    lbimg6 = Label(fvote,image = img6)
		    lbimg6.image = img6
		    lbimg6.place(x=100,y=580)

		    
		    def buttonClickcast(self):
		    	try:
		    		val = vargv.get()
		    	except UnboundLocalError:
		    		val = 7
		    	
		    	if(val == 1):
		    		vote = "Shiv Sena"
		    
		    	elif(val == 2):
		    		vote = "Bhartiya Janata Party"
		    	
		    	elif(val == 3):
		    		vote = "Indian National Congress"
		    
		    	elif(val == 4):
		    		vote = "Nationalist Congress Party"
		    
		    	elif(val == 5):
		    		vote = "Maharashtra Navnirman Sena"
		    	
		    	elif(val == 6):
		    		vote = "Bahujan Samaj Party"
		    	
		    	else:
		    		vote = "NOTA"
		    	
		    	cur.execute("Insert into results (name,adh,age,gender,vote) Values(%s,%s,%s,%s,%s)",(name,adh,age,gender,vote))
		    	cur.execute("commit;")
		    	cur.execute("UPDATE countvotes SET count=count+1 WHERE name='%s'"%(vote))
		    	cur.execute("commit;")
		    	fvote.destroy()
		    	fuser.destroy()
		    	
		
		    bcast = Button(fvote, text="SUBMIT", width=5, height=1, font = ("", 16, ""),bg ="gold", fg = "black", activeforeground = "white", activebackground = "grey")
		    bcast.place(x=600,y=650)
		    bcast.bind('<Button-1>',buttonClickcast)

    bsub= Button(fuser, text = "SUBMIT", width = 5, height = 1, font = ("", 16, ""),bg ="gold", fg = "black", activeforeground = "white", activebackground = "grey")
    bsub.place(x=200,y=320)
    bsub.bind('<Button-1>',buttonClicksub)
    
buser= Button(f, text = "VOTER", width = 8, height = 2,font = ("", 16, ""), bg ="gold", fg = "black", activeforeground = "white", activebackground = "grey")
buser.place(x=950,y=150)
buser.bind('<Button-1>',buttonClickuser)

root.mainloop()
