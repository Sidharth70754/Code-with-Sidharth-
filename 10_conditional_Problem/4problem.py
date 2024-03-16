# determine if a fruit is ripe , overripe , or unique on its color eg: banana : green-unripe, yellow-ripe,brown-overripe :
fruit = "banana"
color = str(input("enter the color of banana:"))

if fruit == "banana":
  if(color == "green"):
    print("This is a unripe banana.")
elif(color == "yellow"):
    print("this is a ripe banana.")
elif(color == "brown"):
    print("this is a overripe banana.")

else:
    print("Sorry this banana is totally rotten")
