from tkinter import Button

from tkinter import *

class Program:

    def __init__(self):
        b = Button(text="click me", command=self.callback)
        b.pack()

    def callback(self):
        print ("clicked!")


def main():
  program = Program()
  return 0

if __name__ == '__main__':
  main()

