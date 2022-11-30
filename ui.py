import customtkinter
from core import Guesser

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

  def __init__(self):

    super().__init__()
    self.title("The Guessing Game")
    self.geometry("400x240")
    self.resizable(False,False)

    self.screen_count = 0
    self.elements = []
    self.screen_setters = [self.setup_guesser, self.the_dare_screen, self.setup_game]

    self.guesser = Guesser()
    self.setup_home_page()

  def next_page(self):

    if self.screen_count > 3:
      return

    for element in self.elements:
      element.destroy()

    self.screen_setters[self.screen_count]()
    self.screen_count += 1

  def setup_home_page(self):
    self.start_text = customtkinter.CTkLabel(
      master=self, text="welcome to the guessing game!!!")
    self.start_text.configure(font=("Ariel", 15))
    self.start_text.place(x=43, y=67)

    self.start_button = customtkinter.CTkButton(master=self,
                                                text="Start",
                                                command=self.next_page,
                                               width=191, height=40)
    self.start_button.place(x=105, y=120)
    self.elements = [self.start_text, self.start_button]

  def setup_guesser(self):

    self.label = customtkinter.CTkLabel(master=self,
                                        text="enter the max num for the range")
    self.label.configure(font=("Ariel", 14))
    self.label.place(x=43, y=67)

    self.text_box = customtkinter.CTkTextbox(master=self, width=253, height=30)
    self.text_box.place(x=69, y=120)

    self.button = customtkinter.CTkButton(master=self,
                                          text="bet",
                                          command=self.set_max_and_next,
                                          width=147, height=29)
    self.button.place(x=122, y=170)
    self.elements = [self.label, self.text_box, self.button]

  def the_dare_screen(self):
    self.the_dare = customtkinter.CTkLabel(master=self, text=f"I will guess the number in {self.max_guess_count - self.guesser.tries} guesses!")
    self.the_dare.configure(font=("Ariel", 13))
    self.the_dare.place(x=28, y=88)
    self.bet_button = customtkinter.CTkButton(master=self, text="BET", command= self.next_page)
    self.bet_button.place(x=125, y=136)

    self.elements = [self.the_dare, self.bet_button]

  def setup_game(self):
    guess = self.guesser.guess()
    self.question_text = customtkinter.CTkLabel(master=self,
                                                text=f"Is the number {guess}?  ({self.max_guess_count - self.guesser.tries} guesses left!)".center(70, " "))
    self.question_text.configure(font= ("Ariel", 10))
    self.question_text.place(x=10, y=33)

    self.high_btn = customtkinter.CTkButton(
      master=self,
      text="Higher",
      command=lambda: self.update_guess('h'),
      corner_radius=4,
      fg_color='#ba7e29',
      hover_color="#8f611f",
      width=128, height=29)
    
    self.high_btn.place(x=68, y=86)

    self.lower_btn = customtkinter.CTkButton(
      master=self, text="Lower", command=lambda: self.update_guess('l'),
      fg_color="#478f47", hover_color="#366b36", corner_radius=4,
      width=128, height=29)
    self.lower_btn.place(x=204, y=86)

    
    self.yes_btn = customtkinter.CTkButton(master=self,
                                           text="Yes",
                                           command=self.finish_game,
                                          width=147, height=29)
    self.yes_btn.place(x=125, y=136)

    self.win_text = customtkinter.CTkLabel(master=self, text="")

  ##############################  Utility Functions ####################################
  
  def set_max_and_next(self):
    self.guesser.max = int(self.text_box.textbox.get("0.0", 'end-1c'))
    self.max_guess_count = self.guesser.get_max_guess_count()
    self.next_page()
    
  def update_guess(self, reply):
    self.guesser.update_from_reply(reply)
    guess = self.guesser.guess()
    if self.guesser.tries > self.max_guess_count:
      self.finish_game()
    self.question_text.configure(text=f"Is the number {guess}? ({self.max_guess_count - self.guesser.tries} guesses left!)".center(70, " "))

  def finish_game(self):

    self.high_btn.configure(state=customtkinter.DISABLED)
    self.lower_btn.configure(state=customtkinter.DISABLED)
    self.yes_btn.configure(state=customtkinter.DISABLED)
    self.win_text.configure(font=("Ariel", 10))
    self.win_text.place(x=52, y=193)

    if self.guesser.tries > self.max_guess_count:
      self.win_text.configure(text=f"My bad, I lost")
    else:
      self.win_text.configure(text=f"Guessed in {self.guesser.tries} turn(s)! Thank you for playing")
      

app = App()
app.mainloop()
