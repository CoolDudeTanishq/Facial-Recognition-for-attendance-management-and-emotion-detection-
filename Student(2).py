


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # type: ignore
from tkinter import messagebox
import mysql.connector # type: ignore

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1515x800+0+0")
        self.root.title("Face Recognition System")
        
        # ============ Variables ============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_specialization = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_faculty = StringVar()




        # Load and resize the image
        img = Image.open(r"Images\Img21.webp")
        img = img.resize((2000, 800), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
    
        # Create a label to display the image
        f_lbl = Label(self.root, image=self.photoimg,text = "Face Recognition Attendance Management System", font = ("times new roman",35,"bold"),bg = "white",fg ="red")
        f_lbl.place(x=0, y=0, width=2000, height=800)  # Fixed: width and height should be in lowercase

        # Title Text
        title_lbl = Label(f_lbl,text = "Student Management System", font = ("times new roman",30,"bold"),bg = "Sky Blue",fg ="Black")
        title_lbl.place(x = 0, y = 0, width=1600, height=50 )


        # Left Label frame
        Left_frame = LabelFrame(f_lbl, bd = 5, bg = "white", relief = RIDGE, text = "Student Details" , font = ("times new roman",12,"bold" ))
        Left_frame.place(x = 15, y = 50, width = 740, height = 730)

        # Left frame Image
        img_Left = Image.open(r"Images\Img18.png")
        img_Left = img_Left.resize((750, 150), Image.LANCZOS)
        self.photoimg_Left = ImageTk.PhotoImage(img_Left)
    
        # Create a label to display the image
        Left_lbl = Label(Left_frame, image=self.photoimg_Left)
        Left_lbl.place(x=5, y=0, width=725, height=150) 

        # Current Course Information
        Current_Course_frame = LabelFrame(Left_frame, bd = 5, bg = "white", relief = RIDGE, text = "Current Course Information" , font = ("times new roman",12,"bold" ))
        Current_Course_frame.place(x = 5, y = 150, width=725, height= 150)
        
        # Department Label
        Dep_Label = Label(Current_Course_frame,text = "Department:" , font = ("times new roman",12,"bold" ), bg = "white")
        Dep_Label.grid(row = 0, column = 0, padx = 10)

        Dep_Combo = ttk.Combobox(Current_Course_frame,textvariable = self.var_dep, font = ("times new roman",12,"bold" ),state = "read only")
        Dep_Combo["values"] = ("Select Department", "Computer","IT","Civil", "Mechanical")
        Dep_Combo.current(0)
        Dep_Combo.grid(row = 0, column = 1, padx = 20, pady = 10)

        # Year Label
        Year_Label = Label(Current_Course_frame,text = "Year:" , font = ("times new roman",12,"bold" ), bg = "white")
        Year_Label.grid(row = 2, column = 0, padx = 10)

        Year_Combo = ttk.Combobox(Current_Course_frame,textvariable = self.var_year, font = ("times new roman",12,"bold" ),state = "read only")
        Year_Combo["values"] = ("Select Year", "2021-22","2022-23","2023-24", "2024-25")
        Year_Combo.current(0)
        Year_Combo.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = W)

        # Course Label
        Course_Label = Label(Current_Course_frame,text = "Course:" , font = ("times new roman",12,"bold" ), bg = "white")
        Course_Label.grid(row = 0, column = 2, padx = 10, sticky = W)

        Course_Combo = ttk.Combobox(Current_Course_frame,textvariable = self.var_course, font = ("times new roman",12,"bold" ),state = "read only")
        Course_Combo["values"] = ("Select Course", "B.Tech","M.Tech","PHD", "LAW")
        Course_Combo.current(0)
        Course_Combo.grid(row = 0, column = 3, padx = 20, pady = 10, sticky = W)

        # Semester Label
        Semester_Label = Label(Current_Course_frame,text = "Semester:" , font = ("times new roman",12,"bold" ), bg = "white")
        Semester_Label.grid(row = 2, column = 2, padx = 10)

        Semester_Combo = ttk.Combobox(Current_Course_frame, textvariable = self.var_semester, font = ("times new roman",12,"bold" ),state = "read only")
        Semester_Combo["values"] = ("Select Semester", "I","II","III", "IV", "V","VI","VII","VIII")
        Semester_Combo.current(0)
        Semester_Combo.grid(row = 2, column = 3, padx = 20, pady = 10, sticky = W)

        # Class Student Information 
        Class_Student_frame = LabelFrame(Left_frame, bd = 5, bg = "white", relief = RIDGE, text = "Class Student Information" , font = ("times new roman",12,"bold" ))
        Class_Student_frame.place(x = 5, y = 300, width=725, height= 400)

        # Student Id
        Student_ID_Label = Label(Class_Student_frame,text = "StudentID:" , font = ("times new roman",12,"bold" ), bg = "white")
        Student_ID_Label.grid(row = 0, column = 0, padx = 10)

        StudentID_Entry = ttk.Entry(Class_Student_frame,textvariable = self.var_std_id, width = 22, font = ("times new roman",12,"bold" ))
        StudentID_Entry.grid(row = 0, column = 1, padx = 30, sticky = W)
        
        # Student Name
        Student_Name_Label = Label(Class_Student_frame,text = "Student Name:" , font = ("times new roman",12,"bold" ), bg = "white")
        Student_Name_Label.grid(row = 0, column = 2, padx = 1)

        StudentName_Entry = ttk.Entry(Class_Student_frame,textvariable = self.var_std_name, width = 22, font = ("times new roman",12,"bold" ))
        StudentName_Entry.grid(row = 0, column = 3, padx = 2, sticky = W)

        # Student Course
        Specialization_Label = Label(Class_Student_frame,text = "Course:" , font = ("times new roman",12,"bold" ), bg = "white")
        Specialization_Label .grid(row = 1, column = 0,pady = 20)

        Specialization_Entry = ttk.Entry(Class_Student_frame,textvariable = self.var_specialization, width = 22, font = ("times new roman",12,"bold" ))
        Specialization_Entry.grid(row = 1, column = 1, padx = 30,pady = 10, sticky = W)

        # Roll Number
        Roll_No_Label = Label(Class_Student_frame,text = "Roll No:" , font = ("times new roman",12,"bold" ), bg = "white")
        Roll_No_Label .grid(row = 1, column = 2,padx = 1,pady = 20)

        Roll_No_Entry = ttk.Entry(Class_Student_frame,textvariable = self.var_roll, width = 22, font = ("times new roman",12,"bold" ))
        Roll_No_Entry.grid(row = 1, column = 3, padx = 2,pady = 10, sticky = W)
        
        # Gender
        Gender_Label = Label(Class_Student_frame,text = "Gender:" , font = ("times new roman",12,"bold" ), bg = "white")
        Gender_Label .grid(row = 2, column = 0,pady = 5)

        Gender_Entry = ttk.Entry(Class_Student_frame,textvariable = self.var_gender, width = 22, font = ("times new roman",12,"bold" ))
        Gender_Entry.grid(row = 2, column = 1, padx = 30,pady = 5, sticky = W)

        # Date Of Birth
        DOB_Label = Label(Class_Student_frame,text = "DOB:" , font = ("times new roman",12,"bold" ), bg = "white")
        DOB_Label .grid(row = 2, column = 2)

        DOB_Entry = ttk.Entry(Class_Student_frame,textvariable = self.var_dob, width = 22, font = ("times new roman",12,"bold" ))
        DOB_Entry.grid(row = 2, column = 3, sticky = W)

         # Email
        Email_Label = Label(Class_Student_frame,text = "Email:" , font = ("times new roman",12,"bold" ), bg = "white")
        Email_Label .grid(row = 3, column = 0,pady = 20)

        Email_Entry = ttk.Entry(Class_Student_frame, textvariable = self.var_email, width = 22, font = ("times new roman",12,"bold" ))
        Email_Entry.grid(row = 3, column = 1, padx = 30,pady = 20, sticky = W)

        # Phone Number
        Phone_NO_Label = Label(Class_Student_frame,text = "Phone No:" , font = ("times new roman",12,"bold" ), bg = "white")
        Phone_NO_Label .grid(row = 3, column = 2)

        Phone_NO_Entry = ttk.Entry(Class_Student_frame, textvariable = self.var_phone, width = 22, font = ("times new roman",12,"bold" ))
        Phone_NO_Entry.grid(row = 3, column = 3, sticky = W)

         # Address
        Address_Label = Label(Class_Student_frame,text = "Address:" , font = ("times new roman",12,"bold" ), bg = "white")
        Address_Label .grid(row = 4, column = 0,pady = 5)

        Address_Entry = ttk.Entry(Class_Student_frame, textvariable = self.var_address, width = 22, font = ("times new roman",12,"bold" ))
        Address_Entry.grid(row = 4, column = 1, padx = 30,pady = 5, sticky = W)

        # Faculty Name
        Faculty_Name_Label = Label(Class_Student_frame,text = "Faculty Name:" , font = ("times new roman",12,"bold" ), bg = "white")
        Faculty_Name_Label .grid(row = 4, column = 2)

        Faculty_Name_Entry = ttk.Entry(Class_Student_frame, textvariable = self.var_faculty, width = 22, font = ("times new roman",12,"bold" ))
        Faculty_Name_Entry.grid(row = 4, column = 3, sticky = W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radionbtn1 = ttk.Radiobutton(Class_Student_frame,variable = self.var_radio1, text = "Take Photo sample", value = "Yes")
        radionbtn1.grid(row = 5, column = 0, padx = 20, pady = 10)

        radionbtn2 = ttk.Radiobutton(Class_Student_frame,variable = self.var_radio1, text = "No Photo sample", value = "No")
        radionbtn2.grid(row = 5, column = 1, padx = 20, pady = 10)

        # Buttons Frame For Save, Update, Delete, Reset Button
        Btn_Frame = Frame(Class_Student_frame, bd = 2, relief = RIDGE, bg = "white", cursor = "hand2")
        Btn_Frame.place(x = 8, y = 270, width = 700, height = 35)

        Save_Btn = Button(Btn_Frame, text = "Save", command = self.Add_data, width = 17,font = ("times new roman",13,"bold" ), bg = "blue", fg = "white", cursor = "hand2")
        Save_Btn.grid(row = 0, column = 0)

        Update_Btn = Button(Btn_Frame, text = "Update",width = 17,font = ("times new roman",13,"bold" ), bg = "blue", fg = "white", cursor = "hand2")
        Update_Btn.grid(row = 0, column = 1)

        Delete_Btn = Button(Btn_Frame, text = "Delete",width = 17,font = ("times new roman",13,"bold" ), bg = "blue", fg = "white", cursor = "hand2")
        Delete_Btn.grid(row = 0, column = 2)

        Reset_Btn = Button(Btn_Frame, text = "Reset",width = 17,font = ("times new roman",13,"bold" ), bg = "blue", fg = "white", cursor = "hand2")
        Reset_Btn.grid(row = 0, column = 3)

        # # Buttons Frame For Take Phot, Update Photo Button
        Btn_Frame1 = Frame(Class_Student_frame, bd = 2, relief = RIDGE, bg = "white", cursor = "hand2")
        Btn_Frame1.place(x = 8, y = 305, width = 700, height = 35)

        Take_Photo_Btn = Button(Btn_Frame1, text = "Take Photo Sample",width = 34,font = ("times new roman",13,"bold" ), bg = "blue", fg = "white", cursor = "hand2")
        Take_Photo_Btn.grid(row = 1, column = 0)

        Update_Photo_Btn = Button(Btn_Frame1, text = "Update Photo Sample",width = 34,font = ("times new roman",13,"bold" ), bg = "blue", fg = "white", cursor = "hand2")
        Update_Photo_Btn.grid(row = 1, column = 1)

        # Right Label frame
        Right_frame = LabelFrame(f_lbl, bd = 5, bg = "white", relief = RIDGE, text = "Student Details" , font = ("times new roman",12,"bold" ))
        Right_frame.place(x = 755, y = 50, width = 740, height = 730)

        # Right frame Image
        img_Right = Image.open(r"Images\Img19.webp")
        img_Right = img_Right.resize((750, 150), Image.LANCZOS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)
    
        # Create a label to display the image
        Right_lbl = Label(Right_frame, image=self.photoimg_Right)
        Right_lbl.place(x=5, y=0, width=725, height=150) 

        # ===========Search System ====================
        Search_frame = LabelFrame(Right_frame, bd = 5, bg = "white", relief = RIDGE, text = "Search System" , font = ("times new roman",12,"bold" ))
        Search_frame.place(x = 5, y = 150, width=720, height= 80)

        # SearchBy Label Inside Serch System Frame
        SearchBy_Label = Label(Search_frame,text = "Search By:" , font = ("times new roman",15,"bold" ), bg = "Light Green")
        SearchBy_Label .grid(row = 0, column = 0, padx = 15, pady = 5, sticky = W)

        SearchBy_Combo = ttk.Combobox(Search_frame, font = ("times new roman",12,"bold" ),state = "read only", width = "15")
        SearchBy_Combo["values"] = ("Select", "Roll_No.","Phone_Number")
        SearchBy_Combo.current(0)
        SearchBy_Combo.grid(row = 0, column = 1, pady = 10, sticky = W)

        Search_Entry = ttk.Entry(Search_frame, width = 18, font = ("times new roman",12,"bold" ))
        Search_Entry.grid(row = 0, column = 2,padx = 10, sticky = W)

        SearchBy_Btn = Button(Search_frame, text = "Search",width = 12,font = ("times new roman",12,"bold" ), bg = "blue", fg = "white", cursor = "hand2")
        SearchBy_Btn.grid(row = 0, column = 3, pady = 5)

        ShowAll_Btn = Button(Search_frame, text = "Show All",width = 12,font = ("times new roman",12,"bold" ), bg = "blue", fg = "white", cursor = "hand2")
        ShowAll_Btn.grid(row = 0, column = 4,padx = 10, pady = 5)

        # Table Frame Below Search Frame Inside Right Label Frame
        Table_frame = Frame(Right_frame, bd = 5, bg = "white", relief = RIDGE)
        Table_frame.place(x = 5, y = 230, width=720, height= 470)

        ScrollBar_X = ttk.Scrollbar(Table_frame,orient = HORIZONTAL)
        ScrollBar_Y = ttk.Scrollbar(Table_frame,orient = VERTICAL)

        self.Student_Table = ttk.Treeview(Table_frame,column = ("Dep","Course","Year","Semester","Student_ID","Student_Name","Specialization","Roll_NO","Gender","DOB","Email","Phone_NO","Address","Faculty_Name","Photo"), xscrollcommand = ScrollBar_X.set, yscrollcommand = ScrollBar_Y.set)
        
        ScrollBar_X.pack(side = BOTTOM, fill = X)
        ScrollBar_Y.pack(side = RIGHT, fill = Y)
        ScrollBar_X.config(command = self.Student_Table.xview)
        ScrollBar_Y.config(command = self.Student_Table.yview)
    
        self.Student_Table.heading("Dep", text = "Department")
        self.Student_Table.heading("Course", text = "Course")
        self.Student_Table.heading("Year", text = "Year")
        self.Student_Table.heading("Semester", text = "Semester")
        self.Student_Table.heading("Student_ID", text = "Student_ID")
        self.Student_Table.heading("Student_Name", text = "Student_Name")
        self.Student_Table.heading("Specialization", text = "Specialization")
        self.Student_Table.heading("Roll_NO", text = "Roll_NO")
        self.Student_Table.heading("Gender", text = "Gender")
        self.Student_Table.heading("DOB", text = "DOB")
        self.Student_Table.heading("Email", text = "Email")
        self.Student_Table.heading("Phone_NO", text = "Phone_NO")
        self.Student_Table.heading("Address", text = "Address")
        self.Student_Table.heading("Faculty_Name", text = "Faculty_Name")
        self.Student_Table.heading("Photo", text = "PhotoSampleStatus")
        self.Student_Table["show"] = "headings"

        self.Student_Table.column("Dep", width = 100)
        self.Student_Table.column("Course", width = 100)
        self.Student_Table.column("Year", width = 100)
        self.Student_Table.column("Semester", width = 100)
        self.Student_Table.column("Student_ID", width = 100)
        self.Student_Table.column("Student_Name", width = 100)
        self.Student_Table.column("Specialization", width = 100)
        self.Student_Table.column("Roll_NO", width = 100)
        self.Student_Table.column("Gender", width = 100)
        self.Student_Table.column("DOB", width = 100)
        self.Student_Table.column("Email", width = 100)
        self.Student_Table.column("Phone_NO", width = 100)
        self.Student_Table.column("Address", width = 100)
        self.Student_Table.column("Faculty_Name", width = 100)
        self.Student_Table.column("Photo", width = 150)

        self.Student_Table.pack(fill = BOTH, expand = 1)

    # ================= function Declaration =====================
    def Add_data(self):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() =="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "Shakti@123", database = "face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_specialization.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_faculty.get(),
                                                                                                self.var_radio1.get()

                                                                                        ))
                # Commit the transaction
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)



        



   

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
