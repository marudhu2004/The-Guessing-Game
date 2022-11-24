from core import Guesser


def main():
  max = 100
  guesser = Guesser(max=max)

  # Banner text
  print(" Welcome to the guessing game!! ".center(50, "*"))
  print(f"Choose a number between 1 and {max}")
  print(
    f"I will guess the number in {guesser.get_max_guess_count() } turns max!")

  while True:
    # guessing and asking the user
    guess = guesser.guess()
    usr_val = input(f"Is the number {guess}? ").lower()

    # If the guess is correct exiting
    if usr_val in ["y", 'yes']:
      print("Yay!!")
      print(f"I guessed it in {guesser.tries} turn(s)")
      break

    # Updating the guesser to make the next guess
    elif usr_val in ["h", "l"]:
      guesser.update_from_reply(usr_val)

  print("Thank you for playing!")


if __name__ == "__main__":
  main()
