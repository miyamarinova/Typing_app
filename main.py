from tkinter import *
from tkinter import filedialog

class Screen:
    def __init__(self):
        self.window = Tk()
        self.main_screen()
        self.typing = False
        self.timer = 0
        self.window.mainloop()

    def main_screen(self):
        self.window.title("Most Dangerous Writing App")
        self.window.geometry("800x600")
        title_1 = Label(text="Keep Typing...",font=('Arial',30))
        title_1.pack(pady=10)
        self.subtitle_1 = Label(text="If you stop typing, in 5 seconds you will lose everything that you've written.", font=('Arial', 15),fg='grey')
        self.subtitle_1.pack(pady=4)
        self.my_frame = Frame(self.window)
        self.my_frame.pack(pady=20,padx=50)
        self.create_text()
        self.my_text.bind('<Key>', self.clear_text)

    def create_text(self):

        self.my_text = Text(self.my_frame, width=90,height=25,undo=True,font=('Arial',20))
        self.my_text.pack()
        self.my_text.focus_force()

    def no_typing(self):
        self.delay=5000
        self.after_id = None

    def clear_text(self,event=None):
        if self.typing:
            self.my_text.config(highlightcolor='black')
            self.reset_timer()
        else:
            self.typing = True
            self.my_text.delete('1.0','end')
            self.countdown()


    def countdown(self):
        if self.typing:
            self.subtitle_1.config(text=f'Seconds without typing: {self.timer}')
            self.my_text.config(highlightcolor='black',background='white')
            self.timer += 1

            if self.timer >= 6:
                self.my_text.config(highlightcolor='#DC3535',background='#DC3535')
                self.my_text.delete('1.0','end')
                self.typing = False
                self.timer = 0
            self.window.after(1000, self.countdown)

    def reset_timer(self):
        self.timer = 0

Screen()