# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'',
                        'answer_why_intent': r'',
                        'cubed_intent': r''
                            }

  # Define .greet() below:
  def greet(self):
    self.name = input("Hello there, what's your name? ")
    will_help = input(f"Hi {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ")

    if will_help.lower() in self.negative_responses:
      print("Ok, have a nice Earth day!")
      return
    self.chat()

  # Define .make_exit() here:
  def make_exit(self, reply):
    for exit in self.exit_commands:
      if exit in reply.lower():
        print("Ok, have a nice Earth Day!")
        return True

  # Define .chat() next:
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
     input(self.match_reply(reply))

  # Define .match_reply() below:
  def match_reply(self, reply):
    for key,value in self.alienbabble.items():
      intent = key
      regex_pattern = value
      found_match = re.match(regex_pattern, reply)


  # Define .describe_planet_intent():
  def describe_planet_intent(self):
    return "Inside .describe_planet_intent()"

  # Define .answer_why_intent():
  def answer_why_intent(self):
    return "Inside .answer_why_intent()"
       
  # Define .cubed_intent():
  def cubed_intent(self, number):
    return "Inside .cubed_intent()"

  # Define .no_match_intent():
  def no_match_intent(self):
    return "Inside .no_match_intent()"

# Create an instance of AlienBot below:
alienOne = AlienBot()
alienOne.greet()