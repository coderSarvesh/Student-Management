from tkinter import*
from tkinter import messagebox
from tkinter.tix import Tree
from PIL import Image,ImageTk
from course import CourseClass
from Student import StudentClass
from result import resultClass
from report import reportClass
import sqlite3
class RMS:
     def __init__(self,root):
         self.root=root
         self.root.title("Student Result Management System")
         self.root.geometry("1350x700+0+0") 
         self.root.config(bg="white")
         self.logo_dash = ImageTk.PhotoImage(file="appicon.png") 
     
       # root.resizable(0,0)

         title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
         M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
         M_Frame.place(x=10,y=70,width=1340,height=80)

         btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2", command=self.add_course).place(x=20,y=5,width=200,height=40)
         btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2", command=self.add_student).place(x=250,y=5,width=200,height=40)
         btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=470,y=5,width=200,height=40)
         btn_view=Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=690,y=5,width=200,height=40)
         btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=910,y=5,width=200,height=40)
        
         self.bg_img=Image.open("bg.png")   
         self.bg_img=self.bg_img.resize((1400,550),Image.ANTIALIAS)
         self.bg_img=ImageTk.PhotoImage(self.bg_img)

         self.lbl_bg=Label(self.root,image=self.bg_img).place(x=0,y=200,height=400)

         self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
         self.lbl_course.place(x=150,y=530,width=300,height=100)

         self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
         self.lbl_student.place(x=550,y=530,width=300,height=100)
         
         self.lbl_result=Label(self.root,text="Total Result\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#ffab00",fg="white")
         self.lbl_result.place(x=950,y=530,width=300,height=100)

         footer=Label(self.root,text="SYSP-System\nContact Us 9999000000",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
         self.update_details()


     def add_course(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=CourseClass(self.new_win)

     def add_student(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=StudentClass(self.new_win)   

     def add_result(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=resultClass(self.new_win)

     def add_report(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=reportClass(self.new_win)

     def exit_(self):
         op=messagebox.askyesno("Confirm","You want to exit Exiting",parent=self.root)
         if op==True:
             self.root.destroy()

     def update_details(self):
         con=sqlite3.connect(database="rms.db")
         cur=con.cursor()
         try:
              cur.execute("select * from course")
              cr=cur.fetchall()
              self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

              cur.execute("select * from student")
              cr=cur.fetchall()
              self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

              cur.execute("select * from result")
              cr=cur.fetchall()
              self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]") 
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()