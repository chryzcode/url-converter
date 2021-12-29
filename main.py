from pyshorteners import Shortener

s = Shortener()

choice = int(input("Enter 1 for link shortener and 2 for link expander: "))

def short():
    link = input("Enter the link to be shortened: ")
    shortened_link = s.tinyurl.short(link)
    print(" The Shortened Link is: " + shortened_link)

def expand():
       link = input("Enter the link to be expanded: ")
       expanded_link = s.tinyurl.expand(link)
       print("The Expanded link is: " + expanded_link)

if choice == 1:
    short()
elif choice == 2:
    expand()
else:
    print("Wrong Entry. Please try again.")
