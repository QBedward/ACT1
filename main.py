import customtkinter as ctk
from PIL import Image

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login UI")
        self.geometry("700x650")
        self.resizable(True, True)

        self.original_image = Image.open("IMAGE/image/1.avif")
        self.bg_label = ctk.CTkLabel(self, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.resize_bg)

        frame = ctk.CTkFrame(self.bg_label, fg_color="white")
        frame.place(relx=0.5, rely=0.5, anchor="center")

       
        ctk.CTkLabel(frame, text="Email", font=("Arial", 12, "bold"), text_color="white").pack(anchor="w")
        ctk.CTkEntry(frame, placeholder_text="Enter Email", width=320, height=42, corner_radius=20, fg_color="#1a1a1a", text_color="white").pack(pady=(4, 15))

        ctk.CTkLabel(frame, text="Password", font=("Arial", 12, "bold"), text_color="white").pack(anchor="w")
        ctk.CTkEntry(frame, placeholder_text="Enter Password", show="*", width=320, height=42, corner_radius=20, fg_color="#1a1a1a", text_color="white").pack(pady=(4, 25))

        ctk.CTkButton(frame, text="Login", command=lambda: None, width=320, height=44, corner_radius=22, font=("Arial", 14, "bold")).pack()

    def resize_bg(self, event):
     
        if event.widget == self:
            self.bg_image = ctk.CTkImage(
                light_image=self.original_image.resize((event.width, event.height), Image.LANCZOS), 
                size=(event.width, event.height)
            )
            self.bg_label.configure(image=self.bg_image)

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()