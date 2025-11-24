#!/usr/bin/python3
class Rectangle:

  def __init__(self):
      self.set_length = 1
      self.set_width = 1
      self.get_length = 1
      self.get_width = 1
      self.get_area = 1

def get_area(self):
    self.get_area = self.get_width * self.get_length
    return self.get_area


def main():

  my_rect = Rectangle()

  my_rect.set_length(4)
  my_rect.set_width(2)

  print('The length is',my_rect.get_length())
  print('The width is', my_rect.get_width())

  print('The area is',my_rect.get_area())
  print(my_rect)

  input('press enter to continue')
