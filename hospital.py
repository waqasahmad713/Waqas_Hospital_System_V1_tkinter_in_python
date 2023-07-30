from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import numpy as np
import mysql.connector
with open('medicine_name.txt','r') as file_obj:
    medicine_name_list = np.array(file_obj.readlines())
new_medicine_name_list = [x.strip() for x in medicine_name_list]
new_medicine_name_list.sort()
medicine_name =("N/A",) + tuple(new_medicine_name_list)

class Hospital:      #creating hospital class 
    def __init__(self,root):         #initaliz window name
        self.root=root    
        self.root.title("Waqas Hospital system")      #tital 
        self.root.geometry("1500x800+0+0")           #make a display size 

         #make variables to take data from text file this line write after 204 line
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.BloodPrusser=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivinguseingMachaine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.CnicNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.Address=StringVar()

       #after variable making put this varibale in text feild        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Waqas Hospital System",fg="red",bg="white",font=("times new roman",50,"bold"))
        #bd is a boder fg = foreground color mean text color :bg= back ground color 
        lbltitle.pack(side=TOP,fill=X)
        # ===================== Data Fram ===========================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                                    font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                                    font=("times new roman",12,"bold"),text="Patient Perscription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        #======================button frame =======================================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1520,height=70)


        #======================Details frame =======================================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=610,width=1390,height=120)
        #========================== Data farme Left =================================
        lblNameTablet=Label(DataframeLeft,text="Name of tablets",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        #create combobox
        comNameTablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",
                                                        font=("tiems new roman",12,"bold"),width=33)
        comNameTablet["values"]=medicine_name
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refernce No :",padx=2,pady=6)
        lblref.grid(row=1,column=0, sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arail",12,"bold"),text="Dose",padx=2,pady=4)
        lblDose.grid(row=2,column=0, sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)


        lblNooftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No of tablets",padx=2,pady=6)
        lblNooftablets.grid(row=3 ,column=0, sticky=W)
        txtNooftablets=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNooftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="LOT",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtlblLot=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtlblLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)
        

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date",padx=2,pady=6)
        lblExpDate.grid(row=6, column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial,",13,"bold"),textvariable=self.Expdate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEfect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFutherInformation=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information",padx=2)
        lblFutherInformation.grid(row=0,column=2,sticky=W)
        txtFutherInformation=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFutherInformation.grid(row=0,column=3)

        lblBloodPreusser=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Presure",padx=2,pady=6)
        lblBloodPreusser.grid(row=1,column=2,sticky=W)
        txtBloodPreusser=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.BloodPrusser,width=35)
        txtBloodPreusser.grid(row=1,column=3)

        lblstorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice",padx=2,pady=6)
        lblstorage.grid(row=2,column=2,sticky=W)
        txtstorage=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        txtstorage.grid(row=2,column=3)

        lblMediciene=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication",padx=2,pady=6)
        lblMediciene.grid(row=3,column=2,sticky=W)
        txtMediciene=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMediciene.grid(row=3,column=3)


        lblPatientID=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient ID",padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        txtPatientID.grid(row=4,column=3)


        lblPatientName=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name",padx=2,pady=6)
        lblPatientName.grid(row=5,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=5,column=3)


        lblPatientCnic=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Cnic No",padx=2,pady=6)
        lblPatientCnic.grid(row=6,column=2,sticky=W)
        txtPatientCnic=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.CnicNumber,width=35)
        txtPatientCnic.grid(row=6,column=3)

        lblPatientDoB=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient DoB",padx=2,pady=6)
        lblPatientDoB.grid(row=7,column=2,sticky=W)
        txtPatientDoB=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
        txtPatientDoB.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Adress",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Address,width=35)
        txtPatientAddress.grid(row=8,column=3)

        #============================= data frame right===========================
        self.txtPrecscription=Text(DataframeRight,font=("arial",12,"bold"),width=35,height=16,padx=2,pady=6)
        self.txtPrecscription.grid(row=0,column=0)

        #=========================== buttons ====================================

        btnprescription = Button(Buttonframe,command=self.iprectioptiion,text="Prescription",bg="green",fg="black", font=("arial", 12, "bold"), width=22, height=2 ,padx=2,pady=4)
        btnprescription.grid(row=0, column=0)

        btnprescriptionData = Button(Buttonframe,command=self.iprecsriptionData,text="Prescription data", bg="green", fg="white", font=("arial", 12, "bold"), width=22, height=2,padx=2,pady=4)
        btnprescriptionData.grid(row=0, column=1)
       


        btnUpdate = Button(Buttonframe,command=self.update ,text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=22, height=2,padx=2,pady=4)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe,command=self.idelete ,text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=22, height=2,padx=2,pady=4)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, command=self.clear,text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=22, height=2,padx=2,pady=4)
        btnClear.grid(row=0, column=4)


        btnExit = Button(Buttonframe,command=self.iexit ,text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=22, height=2,padx=2,pady=4)
        btnExit.grid(row=0, column=5)
        #========================table================================
        #======================= scroll bar ========================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        
        self.hospitail_table=ttk.Treeview(Detailsframe,columns=("nameoftables","refno","dose","nooftablets","lotno","issuedate","expdate","dailydose","BloodPreusser",
                                                                "PatientName","PatientCnicNo","PatientDoB","PatientAddress","storage","Medication","PatientID"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospitail_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospitail_table.yview)
        #================================================================================
        #now creata a database

        self.hospitail_table.heading("nameoftables",text= "Name of Tables")                    #show to user
        self.hospitail_table.heading("refno",text= "Refrence No")  
        self.hospitail_table.heading("dose",text= "Dose")  
        self.hospitail_table.heading("nooftablets",text= "No of Tablets") 
        self.hospitail_table.heading("lotno",text= "Lot No")  
        self.hospitail_table.heading("issuedate",text= "Issues Date")  
        self.hospitail_table.heading("expdate",text= "Exp Date")  
        self.hospitail_table.heading("dailydose",text= "Daily Dose")    
        self.hospitail_table.heading("BloodPreusser",text= "Blood Preusser")  
        self.hospitail_table.heading("PatientCnicNo",text= "Cnic No") 
        self.hospitail_table.heading("PatientName",text= "Name") 
        self.hospitail_table.heading("PatientDoB",text= " DoB") 
        self.hospitail_table.heading("PatientAddress",text= "Address") 


        self.hospitail_table["show"]="headings"

        self.hospitail_table.column("nameoftables",width=110)     #set width of table heading:
        self.hospitail_table.column("refno",width=100)
        self.hospitail_table.column("dose",width=100)
        self.hospitail_table.column("nooftablets",width=100)
        self.hospitail_table.column("lotno",width=100)
        self.hospitail_table.column("issuedate",width=100)
        self.hospitail_table.column("expdate",width=100)
        self.hospitail_table.column("dailydose",width=100)
        self.hospitail_table.column("BloodPreusser",width=100)
        self.hospitail_table.column("PatientCnicNo",width=100)
        self.hospitail_table.column("PatientName",width=100)
        self.hospitail_table.column("PatientDoB",width=100)
        self.hospitail_table.column("PatientAddress",width=100)

        
        self.hospitail_table.pack(fill=BOTH,expand=1)
        self.hospitail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

        #now work on button functions so go to top and creating variables.to take data from text file
    def iprecsriptionData(self):
        '''it insert into sql schema'''
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All field are Requrid:")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hospital_data")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO waqas values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                            self.Nameoftablets.get(),
                                                                                                            self.ref.get(),
                                                                                                            self.Dose.get(),
                                                                                                            self.NumberofTablets.get(),
                                                                                                            self.Lot.get(),
                                                                                                            self.Issuedate.get(),
                                                                                                            self.Expdate.get(),
                                                                                                            self.DailyDose.get(),
                                                                                                            self.BloodPrusser.get(),
                                                                                                            self.PatientName.get(),
                                                                                                            self.CnicNumber.get(),
                                                                                                            self.DateOfBirth.get(),
                                                                                                            self.Address.get()


                                                                                                        ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("success","record has been inserted")
    
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hospital_data")
        my_cursor=conn.cursor()
        my_cursor.execute("update waqas set nameoftablets=%s,refno=%s,dose=%s,nooftablets=%s,lotno=%s,issuedate=%s,expdate=%s,dailydose=%s,bloodPreusser=%s,patientname=%s,patientdob=%s,patientaddress=%s where patientcnicno=%s",( 
                                                                                                        self.Nameoftablets.get(),
                                                                                                        self.ref.get(),
                                                                                                        self.Dose.get(),
                                                                                                        self.NumberofTablets.get(),
                                                                                                        self.Lot.get(),
                                                                                                        self.Issuedate.get(),
                                                                                                        self.Expdate.get(),
                                                                                                        self.DailyDose.get(),
                                                                                                        self.BloodPrusser.get(),
                                                                                                        self.PatientName.get(),
                                                                                                        self.CnicNumber.get(),
                                                                                                        self.DateOfBirth.get(),
                                                                                                        self.Address.get()


                                                                                                    ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","your record has been updated")




    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hospital_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from waqas")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospitail_table.delete(*self.hospitail_table.get_children())
            for i in rows:
                self.hospitail_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursso_row=self.hospitail_table.focus()
        content=self.hospitail_table.item(cursso_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.Expdate.set(row[6])
        self.DailyDose.set(row[7])
        self.BloodPrusser.set(row[8])
        self.CnicNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.Address.set(row[12])
    def iprectioptiion(self):
        self.txtPrecscription.insert(END,"Name of tablets:\t\t\t"+self.Nameoftablets.get() +"\n")
        self.txtPrecscription.insert(END,"Reference No:\t\t\t"+self.ref.get() +"\n")
        self.txtPrecscription.insert(END,"Dose:\t\t\t"+self.Dose.get() +"\n")
        self.txtPrecscription.insert(END,"Number of tablets:\t\t\t"+self.NumberofTablets.get() +"\n")
        self.txtPrecscription.insert(END,"Lot:\t\t\t"+self.Lot.get() +"\n")
        self.txtPrecscription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get() +"\n")
        self.txtPrecscription.insert(END,"Exp Date:\t\t\t"+self.Expdate.get() +"\n")
        self.txtPrecscription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get() +"\n")
        self.txtPrecscription.insert(END,"Side Effect:\t\t\t"+self.sideEfect.get() +"\n")
        self.txtPrecscription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get() +"\n")
        self.txtPrecscription.insert(END,"StorageAdvice:\t\t\t"+self.StorageAdvice.get() +"\n")
        self.txtPrecscription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivinguseingMachaine.get() +"\n")
        self.txtPrecscription.insert(END,"Patient ID:\t\t\t"+self.PatientId.get() +"\n")
        self.txtPrecscription.insert(END,"Cnic No:\t\t\t"+self.CnicNumber.get() +"\n")
        self.txtPrecscription.insert(END,"Name:\t\t\t"+self.PatientName.get() +"\n")
        self.txtPrecscription.insert(END,"Date of Birth:\t\t\t"+self.DateOfBirth.get() +"\n")
        self.txtPrecscription.insert(END,"Address:\t\t\t"+self.Address.get() +"\n")

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hospital_data")
        my_cursor=conn.cursor()
        query="DELETE FROM waqas WHERE patientcnicno=%s"
        value=(self.CnicNumber.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Deleted","Patient has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivinguseingMachaine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.CnicNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.Address.set("")
        self.txtPrecscription.delete("1.0",END)

    def iexit(self):
        iexit=messagebox.askyesno("Hospital managment system","confrim you want to exist")
        if iexit>0:
            root.destroy()
            return

root=Tk()
ob=Hospital(root)
root.mainloop()
