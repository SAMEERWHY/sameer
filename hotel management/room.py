from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector
from time import strftime
from datetime import datetime
import random
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ==========variables===========
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        # ==================title=====================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS", font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # =======================logo====================
        img2=Image.open("C:/Users/mohds/Desktop/projects/hotel management/images/hotel images/logohotel.png")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # ================label frame===============
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",padx=2,font=("times new roman",12,"bold"))
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

        # ===================label and entry=============
        # ========cust contact============
        lbl_cust_contact=Label(LabelFrameleft,text="Customer contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(LabelFrameleft,textvariable=self.var_contact,width=29,font=("times new roman",13,))
        entry_contact.grid(row=0,column=1,sticky=W)

        # ===============fetch data  buttom==============
        btnFetchData=Button(LabelFrameleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)


        # ============check in date==================
        check_in_date=Label(LabelFrameleft,text="Check in date",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(LabelFrameleft,textvariable=self.var_checkin,width=29,font=("arial",13,))
        txtcheck_in_date.grid(row=1,column=1)

        # =============check out date============
        lbl_check_out=Label(LabelFrameleft,text="check out date",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out=ttk.Entry(LabelFrameleft,textvariable=self.var_checkout,width=29,font=("times new roman",13,))
        txt_check_out.grid(row=2,column=1)

        # ===============room type combobox======================
        label_roomtype=Label(LabelFrameleft,font=("arial",12,"bold"),text="Room type:",padx=2,pady=6)
        label_roomtype.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,font=("arial",12,),width=27,state="readonly")
        combo_roomtype["value"]=ide
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)


        # =======Available room==========
        lblAvailableroom=Label(LabelFrameleft,text="Available Room",font=("arial",12,"bold"),padx=2,pady=6)
        lblAvailableroom.grid(row=4,column=0,sticky=W)
        # txtAvailableroom=ttk.Entry(LabelFrameleft,textvariable=self.var_roomavailable,width=29,font=("times new roman",13,))
        # txtAvailableroom.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomavailable,font=("arial",12,),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        # ========Meal===============
        lblMeal=Label(LabelFrameleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(LabelFrameleft,textvariable=self.var_meal,width=29,font=("times new roman",13,))
        txtMeal.grid(row=5,column=1)

        # =========Number of days===============
        lblNumberofdays=Label(LabelFrameleft,text="Number of days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNumberofdays.grid(row=6,column=0,sticky=W)
        txtNumberofdays=ttk.Entry(LabelFrameleft,textvariable=self.var_noOfdays,width=29,font=("times new roman",13,))
        txtNumberofdays.grid(row=6,column=1)

        # =======Paid tax==================
        lblPaidtax=Label(LabelFrameleft,font=("arial",12,"bold"),text="Paid tax:",padx=2,pady=6)
        lblPaidtax.grid(row=7,column=0,sticky=W)
        txtNumberofdays=ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax,width=29,font=("times new roman",13,))
        txtNumberofdays.grid(row=7,column=1)



        # =====================Sub total=====================
        lblPaidtax=Label(LabelFrameleft,font=("arial",12,"bold"),text="Sub total:",padx=2,pady=6)
        lblPaidtax.grid(row=8,column=0,sticky=W)
        lblPaidtax=Label(LabelFrameleft,textvariable=self.var_actualtotal,font=("arial",12,"bold"),text="Paid tax:",padx=2,pady=6)
        lblPaidtax.grid(row=8,column=1,sticky=W)

        
        # ========total cost===============
        lblIdNumber=Label(LabelFrameleft,text="Total cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(LabelFrameleft,textvariable=self.var_total,font=("times new roman",13,),width=29,)
        txtIdNumber.grid(row=9,column=1)

        # =========bill button===============
        btnBill=Button(LabelFrameleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

          # =======================buttons==================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        # ==========right side image========================
        img3=Image.open("C:/Users/mohds/Desktop/projects/hotel management/images/hotel images/bed.jpg")
        img3=img3.resize((520,300))
        self.photoimg2=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)

        # ==============table frame search system=========================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and Search System",padx=2,font=("times new roman",12,"bold"))
        Table_frame.place(x=435,y=280,width=860,height=260)

        lblSearchby=Label(Table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room",)
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=("times new roman",13,))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",command=self.searchbox,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShow=Button(Table_frame,text="showall",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShow.grid(row=0,column=4,padx=1)

               # ================ShowDataTable======================
        Details_Table=Frame(Table_frame,bd=2,relief=RIDGE)
        Details_Table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)
        self.room_table=ttk.Treeview(Details_Table,column=("contact","checkinDate","checkoutDate","roomtype","roomavailable","meal","noOfdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkinDate",text="Check-in")
        self.room_table.heading("checkoutDate",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")
        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkinDate",width=100)
        self.room_table.column("checkoutDate",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)


        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
#==================add data=========================


    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try: 
              conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
              my_cursor=conn.cursor()
              my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.var_checkin.get(),
                                                                    self.var_checkout.get(),
                                                                    self.var_roomtype.get(),
                                                                    self.var_roomavailable.get(),
                                                                    self.var_meal.get(),
                                                                    self.var_noOfdays.get(),
                                                                    self.var_contact.get()

                                                                ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Waning",f"something went wrong:{str(es)}",parent=self.root) 

              #============================fetch data===========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()   
        #=================get cursor=========================  
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noOfdays.set(row[6])
#=====================update function=========================
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:    
         conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
         my_cursor=conn.cursor()
         my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                    
                                                                    self.var_checkin.get(),
                                                                    self.var_checkout.get(),
                                                                    self.var_roomtype.get(),
                                                                    self.var_roomavailable.get(),
                                                                    self.var_meal.get(),
                                                                    self.var_noOfdays.get(),
                                                                    self.var_contact.get()

                                                                                       ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","room detail has been updated successfully",parent=self.root)
    
    # ============================ Delete ==============
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # ================reset==========
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")



      
#====================ALL DATA FETCH==========================
    def Fetch_contact(self):
            if self.var_contact.get()=="":
              messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
                my_cursor=conn.cursor()
                query=("select Name from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                if row==None:
                    messagebox.showerror("Error","This number not found",parent=self.root)
                else:
                    conn.commit()
                    conn.close()

                    showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                    showDataFrame.place(x=450,y=55,width=300,height=180)      

                    lblName3=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                    lblName3.place(x=0, y=0)

                    lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                    lbl.place(x=90, y=0)

                    conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
                    my_cursor=conn.cursor()
                    query=("select Gender from customer where Mobile =%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()

                    lblGender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                    lblGender.place(x=0, y=30)
                    lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                    lbl2.place(x=90, y=30)

                    # ====================Email============
                    conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
                    my_cursor=conn.cursor()
                    query=("select Email from customer where Mobile =%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()

                    lblemail=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                    lblemail.place(x=0, y=60)
                    lbl3=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                    lbl3.place(x=90, y=60)

                    # ======================Nationality==============
                    conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
                    my_cursor=conn.cursor()
                    query=("select Nationality from customer where Mobile =%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()

                    lblNationality=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
                    lblNationality.place(x=0, y=90)
                    lbl4=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                    lbl4.place(x=90, y=90)

                    # ========================Address===============
                    conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
                    my_cursor=conn.cursor()
                    query=("select Address from customer where Mobile =%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()

                    lbladdress=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
                    lbladdress.place(x=0, y=120)
                    lbl1=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                    lbl1.place(x=90, y=120)
      
      #  search system
    def searchbox(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
      my_cursor=conn.cursor() 

      my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")       
      rows=my_cursor.fetchall()
      if len (rows)!=0:
          self.room_table.delete(*self.room_table.get_children())
          for i in rows:
              self.room_table.insert("",END,values=i)
          conn.commit()
      conn.close()             

    def total(self):
      inDate=self.var_checkin.get()
      outDate=self.var_checkout.get()   
      inDate=datetime.strptime(inDate, "%d/%m/%Y")
      outDate=datetime.strptime(outDate, "%d/%m/%Y")        
      self.var_noOfdays.set(abs(outDate-inDate).days)  
      if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
          q1=float(300)
          q2=float(700)
          q3= float(self.var_noOfdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.1))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

      elif (self.var_meal.get()=="lunch" and self.var_roomtype.get()=="Single"):
          q1=float(300)
          q2=float(700)
          q3= float(self.var_noOfdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.1))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT) 

      elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
          q1=float(500)
          q2=float(1000)
          q3= float(self.var_noOfdays.get())
          q4=float(q1+q2)
          q5=float(q3+q4)
          Tax="Rs."+str("%.2f"%((q5)*0.1))
          ST="Rs."+str("%.2f"%((q5)))
          TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)  


           









if __name__ == "__main__": 
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()