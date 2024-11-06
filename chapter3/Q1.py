welcome = "Hi <NAME>, welcome in <clg>"

name=input("enter your name")
college=input("enter your college")

newWelcome=welcome.replace("<NAME>",name).replace("<clg>",college)

print(newWelcome)