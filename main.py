def planets(p):
#def myList()
    for i in range(0, len(planet)):
        if p == planet[i]:
            return i + 1
    return p + " is not a planet" 
#mylist = [1, 2, 3, 4, 5, 6, 7, 8]
#myList.append(2)
planet = ["mercury", "venus", "earth", "mars", "jupitur", "saturn", "uranus", "neptun"]
print (planets("earth"))

#"mercury" = 1; "venus" = 2; "earth" = 3