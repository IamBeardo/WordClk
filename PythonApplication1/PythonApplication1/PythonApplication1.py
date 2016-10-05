from GI_classes import individual, word, population, letter
print ("Hell0 W0rld")




#c=population(10)
#print(c.individuals)


a = letter([1,3],"A")
b = letter([1,3],"B")
c = letter([1,3],"C")

print (a)

skapa = word("Hello",[0,1],0)
gapa = word("World",[4,0],1)


print (skapa.grid)
print (gapa.grid)

print (skapa.grid.intersection(gapa.grid))
