public_toilet = "PB"

def Home():
    private_toilet = "PT"
    print(private_toilet)
    print(public_toilet)

def stranger():
    print(public_toilet)
    #print(private_toilet) local variable can't be called

print(public_toilet) # global
#print(private_toilet)#private