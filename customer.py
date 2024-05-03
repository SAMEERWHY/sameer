from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox



class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #==========================variables=================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


        # ==================title=====================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS", font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # =======================logo====================
        img2=Image.open("C:/Users/mohds/Desktop/projects/hotel management/images/hotel images/logohotel.png")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # ================label frame===============
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

        # ===================label and entry=============
        # ========cust ref============
        lbl_cust_ref=Label(LabelFrameleft,text="Customer Ref",font=("times new roman",15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)


        entry_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_ref,width=29,state="readonly",font=("times new roman",13,))
        entry_ref.grid(row=0,column=1)

        # ============cust name==================
        cname=Label(LabelFrameleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_name,width=29,font=("arial",13,))
        txtcname.grid(row=1,column=1)

        # =============mother name============
        lblmname=Label(LabelFrameleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(LabelFrameleft,textvariable=self.var_mother,width=29,font=("times new roman",13,))
        txtmname.grid(row=2,column=1)

        # ===============gender combobox======================
        label_gender=Label(LabelFrameleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(LabelFrameleft,textvariable=self.var_gender,font=("arial",12,),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        # =======post code==========
        lblPostCode=Label(LabelFrameleft,text="Post Code",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(LabelFrameleft,textvariable=self.var_post,width=29,font=("times new roman",13,))
        txtPostCode.grid(row=4,column=1)

        # ========Mobile Number===============
        lblMobile=Label(LabelFrameleft,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(LabelFrameleft,textvariable=self.var_mobile,width=29,font=("times new roman",13,))
        txtMobile.grid(row=5,column=1)

        # =========e-mail===============
        lblEmail=Label(LabelFrameleft,text="e-mail:",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(LabelFrameleft,textvariable=self.var_email,width=29,font=("times new roman",13,))
        txtEmail.grid(row=6,column=1)

        # =======nationality==================
        lblNationality=Label(LabelFrameleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_nationality=ttk.Combobox(LabelFrameleft,textvariable=self.var_nationality,font=("arial",12,),width=27,state="readonly")
        combo_nationality["value"]=("Indian","American","Britist")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)


        # =====================idproof type combobox=====================
        lnlIdProof=Label(LabelFrameleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lnlIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(LabelFrameleft,textvariable=self.var_id_proof,font=("arial",12,),width=27,state="readonly")
        combo_id["value"]=("AdhaarCard","DrivingLicence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # ============id number==================
        lblIdNumber=Label(LabelFrameleft,text="Id Number :",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(LabelFrameleft,textvariable=self.var_id_number,width=29,font=("times new roman",13,))
        txtIdNumber.grid(row=9,column=1)

        # ========address===============
        lblAddress=Label(LabelFrameleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(LabelFrameleft,textvariable=self.var_address,font=("times new roman",13,),width=29,)
        txtAddress.grid(row=10,column=1)

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

        # ==============table frame search system=========================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and Search System",padx=2,font=("times new roman",12,"bold"))
        Table_frame.place(x=435,y=50,width=860,height=490)

        lblSearchby=Label(Table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Ref",)
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=("times new roman",13,))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,command=self.searchbox,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShow=Button(Table_frame,text="showall",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShow.grid(row=0,column=4,padx=1)

        # ================ShowDataTable======================
        Details_Table=Frame(Table_frame,bd=2,relief=RIDGE)
        Details_Table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)

        self.Cust_detail_Table=ttk.Treeview(Details_Table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_detail_Table.xview)
        scroll_y.config(command=self.Cust_detail_Table.yview)

        self.Cust_detail_Table.heading("ref",text="Refer no.")
        self.Cust_detail_Table.heading("name",text="Name")
        self.Cust_detail_Table.heading("mother",text="mother name")
        self.Cust_detail_Table.heading("gender",text="gender")
        self.Cust_detail_Table.heading("post",text="postCode")
        self.Cust_detail_Table.heading("mobile",text="mobile Number")
        self.Cust_detail_Table.heading("email",text="E-mail id.")
        self.Cust_detail_Table.heading("nationality",text="Nationality")
        self.Cust_detail_Table.heading("idproof",text="Id proof.")
        self.Cust_detail_Table.heading("idnumber",text="Id Number")
        self.Cust_detail_Table.heading("address",text="address.")

        self.Cust_detail_Table["show"]="headings"

        self.Cust_detail_Table.column("ref",width=100)
        self.Cust_detail_Table.column("name",width=100)
        self.Cust_detail_Table.column("mother",width=100)
        self.Cust_detail_Table.column("gender",width=100)
        self.Cust_detail_Table.column("post",width=100)
        self.Cust_detail_Table.column("mobile",width=100)
        self.Cust_detail_Table.column("email",width=100)
        self.Cust_detail_Table.column("nationality",width=100)
        self.Cust_detail_Table.column("idproof",width=100)
        self.Cust_detail_Table.column("idnumber",width=100)
        self.Cust_detail_Table.column("address",width=100)

        self.Cust_detail_Table.pack(fill=BOTH,expand=1)
        self.Cust_detail_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.var_ref.get(),
                                                                    self.var_cust_name.get(),
                                                                    self.var_mother.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_post.get(),
                                                                    self.var_mobile.get(),
                                                                    self.var_email.get(),
                                                                    self.var_nationality.get(),
                                                                    self.var_id_proof.get(),
                                                                    self.var_id_number.get(),
                                                                    self.var_address.get()              
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Waning",f"something went wrong:{str(es)}",parent=self.root)
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_detail_Table.delete(*self.Cust_detail_Table.get_children())
            for i in rows:
                self.Cust_detail_Table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    def get_cursor(self,event=""):
        cursor_row=self.Cust_detail_Table.focus()
        content=self.Cust_detail_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:    
         conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
         my_cursor=conn.cursor()
         my_cursor.execute("update customer set Name=%s,mother=%s,gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,idnumber=%s,Address=%s where Ref=%s",(
                                                                    
                                                                    self.var_cust_name.get(),
                                                                    self.var_mother.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_post.get(),
                                                                    self.var_mobile.get(),
                                                                    self.var_email.get(),
                                                                    self.var_nationality.get(),
                                                                    self.var_id_proof.get(),
                                                                    self.var_id_number.get(),
                                                                    self.var_address.get(),
                                                                    self.var_ref.get()

                                                                                       ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Customer detail has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()   

    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def searchbox(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sameer.2005",database="management")    
        my_cursor=conn.cursor() 

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")       
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_detail_Table.delete(*self.Cust_detail_Table.get_children())
            for i in rows:
                self.Cust_detail_Table.insert("",END,values=i)
            conn.commit()
        conn.close()        


            


if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()