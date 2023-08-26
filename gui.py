import tkinter as tk


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("360x280")
        self.root.title("Random Desktop Wallpaper Changer")
        self.root.configure(background="black")

        self.topicLabel = tk.Label(self.root, text="Search for a wallpaper", font=('Arial', 20), bg='black', fg='white')
        self.topicLabel.pack(padx=20, pady=20)

        self.topicBox = tk.Text(self.root, height=1, font=('Arial', 16))
        self.topicBox.bind("<KeyPress>", self.enterKey)
        self.topicBox.pack(padx=10, pady=20)

        self.button = tk.Button(self.root,
                                text="Get Wallpaper!",
                                font=('Arial', 20),
                                command=self.handleInput,
                                background="#4285F4")
        self.button.pack()

        self.githubLabel = tk.Label(self.root, text="github.com/ZIAD220", font=('Arial', 11), bg='black', fg='white')
        self.githubLabel.pack(side='bottom')
        self.githubLabel.pack(side='right')

        self.root.mainloop()

    def handleInput(self):
        topic = self.topicBox.get("1.0", tk.END)
        print(topic)

    def enterKey(self, event):
        if event.keysym == "Return":
            self.handleInput()

GUI()