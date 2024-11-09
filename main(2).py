from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # type: ignore
from Student import Student





class Face_Recognition_Attendance_Management:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1515x800+0+0")
        self.root.title("Face Recognition System")

        # Load and resize the image
        img = Image.open(r"Images\Img2.webp")
        img = img.resize((2000, 800), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
    
        # Create a label to display the image
        f_lbl = Label(self.root, image=self.photoimg,text = "Face Recognition Attendance Management System", font = ("times new roman",35,"bold"),bg = "white",fg ="red")
        f_lbl.place(x=0, y=0, width=2000, height=800)  # Fixed: width and height should be in lowercase

        # Title Text
        title_lbl = Label(f_lbl,text = "Face Recognition Attendance Management System", font = ("times new roman",30,"bold"),bg = "Sky Blue",fg ="Black")
        title_lbl.place(x = 0, y = 0, width=1600, height=50 )

         
        # Student Button
        img1 = Image.open(r"Images\Img10.jpg")
        img1 = img1.resize((300, 300), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(f_lbl,image = self.photoimg1,command = self.Student_Details, cursor = "hand2",bg = "Blue", border = "10")
        b1.place(x = 10, y = 100, width = 200, height = 220)

        Below_b1 = Button(f_lbl, text = "Student Details",command = self.Student_Details, cursor = "hand2",border = "10", font = ("times new roman",20,"bold"),bg = "Blue",fg ="White")
        Below_b1.place(x = 10, y = 300, width = 200, height = 50)

        # Face Detector Button
        img2 = Image.open(r"Images\Img8.png")
        img2 = img2.resize((300, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(f_lbl,image = self.photoimg2, cursor = "hand2",bg = "Blue",border = "10")
        b2.place(x = 10, y = 400, width = 200, height = 200)

        Below_b2 = Button(f_lbl, text = "Face Detector", cursor = "hand2", border = "10", font = ("times new roman",20,"bold"),bg = "Blue",fg ="White")
        Below_b2.place(x = 10, y = 600, width = 200, height = 50)

        # Attendance Button
        img3 = Image.open(r"Images\Img11.png")
        img3 = img3.resize((200, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(f_lbl,image = self.photoimg3, cursor = "hand2",bg = "Blue", border = "10")
        b3.place(x = 250, y = 100, width = 200, height = 220)

        Below_b3 = Button(f_lbl, text = "Attendance", cursor = "hand2", border = "10",  font = ("times new roman",20,"bold"),bg = "Blue",fg ="White")
        Below_b3.place(x = 250, y = 300, width = 200, height = 50)
        

        # Developer Face Button
        img4 = Image.open(r"Images\Img15.jpg")
        img4 = img4.resize((310, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(f_lbl,image = self.photoimg4, cursor = "hand2",bg = "Blue", border = "10")
        b4.place(x = 250, y = 400, width = 200, height = 200)

        Below_b4 = Button(f_lbl, text = "Developer", cursor = "hand2", border = "10", font = ("times new roman",20,"bold"),bg = "Blue",fg ="White")
        Below_b4.place(x = 250, y = 600, width = 200, height = 50)


        # Train face Button
        img5 = Image.open(r"Images\Img13.jpeg")
        img5 = img5.resize((400, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5 = Button(f_lbl,image = self.photoimg5, cursor = "hand2",bg = "Blue", border = "10")
        b5.place(x = 490, y = 100, width = 200, height = 220)

        Below_b5 = Button(f_lbl, text = "Train Data", cursor = "hand2", border = "10",  font = ("times new roman",20,"bold"),bg = "Blue",fg ="White")
        Below_b5.place(x = 490, y = 300, width = 200, height = 50)


        # Photos Face Button
        img6 = Image.open(r"Images\Img14.webp")
        img6 = img6.resize((170, 170), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(f_lbl,image = self.photoimg6, cursor = "hand2",bg = "Blue", border = "10")
        b6.place(x = 490, y = 400, width = 200, height = 200)
        
        Below_b6 = Button(f_lbl, text = "Photos", cursor = "hand2", border = "10", font = ("times new roman",20,"bold"),bg = "Blue",fg ="White")
        Below_b6.place(x = 490, y = 600, width = 200, height = 50)

        # Help Desk Button
        img7 = Image.open(r"Images\Img16.jpg")
        img7 = img7.resize((200, 80), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b7 = Button(f_lbl,image = self.photoimg7, cursor = "hand2",bg = "Blue", border = "10")
        b7.place(x = 1000, y = 640, width = 200, height = 80)

        Below_b7 = Button(f_lbl, text = "Help Desk", cursor = "hand2", border = "10", font = ("times new roman",20,"bold"),bg = "Blue",fg ="White")
        Below_b7.place(x = 1000, y = 718, width = 200, height = 50)

        # Exit Button
        img8 = Image.open(r"Images\Img17.webp")
        img8 = img8.resize((200, 80), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b8 = Button(f_lbl,image = self.photoimg8, cursor = "hand2",bg = "Blue", border = "10")
        b8.place(x = 1250, y = 640, width = 200, height = 80)

        Below_b8 = Button(f_lbl, text = "Exit", cursor = "hand2", border = "10", font = ("times new roman",20,"bold"),bg = "Blue",fg ="White")
        Below_b8.place(x = 1250, y = 718, width = 200, height = 50)


# ================= Functions Buttons ====================
    def Student_Details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_Attendance_Management(root)
    root.mainloop()
