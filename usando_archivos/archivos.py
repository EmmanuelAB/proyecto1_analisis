def main():
    f = open("file", "r")
    i = 1
    while(1):
        #s = f.readline()
        s = f.read(8)
        if(s!=""):
            print("Línea"+str(i)+" = "+s)
            i+=1
        else:
            break
        
    #for x in range(1,4):
        #f.write("Hola mundo"+str(x)+"\n")


main()
