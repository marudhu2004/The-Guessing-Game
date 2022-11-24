class Guesser:

  def __init__(self, min=0, max=10):
    self.min = min
    self.max = max
    self.tries = 0

  def guess(self) -> int:
    self.tries += 1

    guess_val = (self.max + self.min) / 2
    if guess_val > int(guess_val): guess_val += 1
    self.guess_val = int(guess_val)
    return self.guess_val

  def update_from_reply(self, reply):
    if reply == 'h':
      self.min = self.guess_val
    elif reply == 'l':
      self.max = self.guess_val

  def get_max_guess_count(self):
    max, min = self.max, self.min

    count = 0
    while max - min > 1:
      max = (max + min) / 2
      count += 1

    return count


if __name__ == "__main__":
  guesser = Guesser()
  print(guesser.get_max_guess_count())