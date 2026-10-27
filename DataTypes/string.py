#multiline strings
print("MULTILINE STRINGS")
sentence = """This
is
Sparta"""
print(sentence, "\n\n")



#slicing strings
print("SLICING STRINGS")
varHelloWorld = 'Hello World'
print(varHelloWorld[2:6])
print(varHelloWorld[2:])#slice to end
print(varHelloWorld[:5])#slice from start
print(varHelloWorld[-6:-2], "\n\n")#negative slicing, slicees by taking reference from the end



#modify strings
print("MODIFY STRINGS")
print(varHelloWorld.upper())
print(varHelloWorld.lower())

hiWithSpace = "     Hi  "

print(hiWithSpace)
print(hiWithSpace.strip()) #this only removes whitespaces from the beginning and the end

varHelloWorld = varHelloWorld.replace(" ", ", ")
print(varHelloWorld)
if ',' in varHelloWorld:
    print("varHelloWorld has ,")

varHastags="Ferrari#Mercedes#Red Bull#McLaren#Aston Martin"
varHastags = varHastags.split("#",3);
Constructor_1, Constructor_2, Constructor_3, Constructor_4 = varHastags
print(varHastags)
print(Constructor_2)
