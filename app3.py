from tkinter import *

# create root window
root = Tk()
# root window title and dimension
root.title("HRMS")
# Set geometry(widthxheight)
root.geometry('500x300')

#---------------------------------------ENTRY AND RETRIEVE HEALTH DETAILS-----------------------------------------------------------
lbl1 = Label(root, text = "HEALTH DETAILS", font=6)   
lbl1.grid(column = 4 , row = 0)

#==============================================================Address details===================================================
lbl2 = Label(root, text = "Address")
lbl2.grid()

txt = Entry(root, width=10)
txt.grid(column = 2, row =1)

#============================================================OUTCOME==============================================================

lbl3 = Label(root, text = "Outcome")
lbl3.grid(column = 0, row =3)

txt = Entry(root, width=10)
txt.grid(column = 2, row =3)

#==========================================================PREGNANCY DETAILS=======================================================
lbl4 = Label(root, text = "Pregnancy")
lbl4.grid(column = 0, row =5)

txt = Entry(root, width=10)
txt.grid(column = 2, row =5)

#======================================================Plasma Details=================================================
lbl5 = Label(root, text = "Plasma")
lbl5.grid(column = 0, row =7)

txt = Entry(root, width=10)
txt.grid(column =2, row =7)

#================================================Blood Pressure details=======================================================
lbl6 = Label(root, text = "Blood pressure")
lbl6.grid(column = 0, row =9)

txt = Entry(root, width=10)
txt.grid(column =2, row =9)

#==========================================Skin Thickness Details====================================================================
lbl7 = Label(root, text = "Skin Thickness")
lbl7.grid(column = 0, row =11)

txt = Entry(root, width=10)
txt.grid(column =2, row =11)

#==========================================Insulin Details=======================================================================
lbl8 = Label(root, text = "Insulin")
lbl8.grid(column = 0, row =13)

txt = Entry(root, width=10)
txt.grid(column =2, row =13)

#=================================================Body Mass Index details==========================================================
lbl9 = Label(root, text = "BMI")
lbl9.grid(column = 0, row =15)

txt = Entry(root, width=10)
txt.grid(column =2, row =15)
#==================================================Diabetes Pedigree Function====================================================
lbl10 = Label(root, text = "DPF")
lbl10.grid(column = 0, row =17)

txt = Entry(root, width=10)
txt.grid(column =2, row =17)

#=======================================================================Age========================================================
lbl11 = Label(root, text = "Age")
lbl11.grid(column = 0, row =19)

txt = Entry(root, width=10)
txt.grid(column =2, row =19)


#==========================================list of health details==============================================================
lbl=Label(root,text="Submit")

def get_health_details():

	res = txt.get()
	lbl.configure(text = res)

# button widget with blue color text inside
btn = Button(root, text = "Submit" ,
			fg = "blue", command=get_health_details)
# Set Button Grid
btn.grid(column=2, row=20)

# Execute Tkinter
root.mainloop()
