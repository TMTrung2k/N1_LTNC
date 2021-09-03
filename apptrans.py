from tkinter import*
from PIL import Image , ImageTk
from googletrans import Translator


#đầu tiên cần cài đặt gói hộ trợ của python trong cmd
# bước 1 , mở cmd gõ <pip install googletrans > --- rồi enter nếu bị lỗi gõ lại : <pip install googletrans==3.1.0a0    >> rồi enter 
#bước 2  , gõ tiếp : <pip install Pillow>   >> rồi enter . 
# b3 mở code và bắt đẩu  chạy ...
#note: dịch từ "en sang "vi" bằng cách nhập chữ tiếng anh rồi click "Reverse"    ngôn ngữ  sẽ dược dịch ra 
#note:  dịch "vi" sang "en"  bằng cách nhập chữ tiếng việt rồi click "Translate"  ngôn ngữ  sẽ dược dịch ra 


# tạo màn Windown
root= Tk()
root.title('Google Dịch VN-EN')
root.geometry("960x630")
root.iconbitmap('logo.ico')
# tạo background
load= Image.open('hinhnen.png')
render= ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)
# text trong background
name=Label(root,text="Translator",fg="#303030",bd=0,bg="#7500B4")
name.config(font=("Transformers Movie",30))
name.pack(pady=10)
# textbox trong màn hình 
box= Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)
button_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)

def translate():
    input= box.get(1.0,END)
    print(input)
    t= Translator()
    a=t.translate(input,src="vi",dest="en")
    b=a.text
    box1.insert(END,b)

def reverse():
    
    input= box.get(1.0,END)
    print(input)
    t= Translator()
    b=t.translate(input,src="en",dest="vi")
    c=b.text
    box1.insert(END,c)
pass

clear_button= Button(button_frame,text="Clear Text",font=(("Time New Roman"),15,"bold"),bg="#303030",fg="#FFFFFF",command=clear)
clear_button.place(x=310,y=310)
trans_button=Button(button_frame,text="Translate",font=(("Times New Roman"),15,'bold'),bg="#303030",fg="#FFFFFF",command=translate)
trans_button.place(x=550,y=310)
reverse_button= Button(button_frame,text="Reverse",font=(("Time New Roman"),15,"bold"),bg="#303030",fg="#FFFFFF",command= reverse)
reverse_button.place(x=440,y=310)
box1=Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)    
root.mainloop()                 
