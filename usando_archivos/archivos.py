def main():
    guardar_nombres()

    #f = open("file", "r")
    #i = 1
    #while(1):
        #s = f.readline()
        #s = f.read(8)
        #if(s!=""):
            #print("Línea"+str(i)+" = "+s)
            #i+=1
        #else:
            #break
        
    #for x in range(1,4):
        #f.write("Hola mundo"+str(x)+"\n")
def guardar_nombres():
    f = open("file","r+")
    x = input(">")
    while(x!="."):
        f.write(x+"\n")
        a = f.tell()
        f.seek(0,0)
        print("Archivo:")
        print(f.read())
        f.seek(a,0)
        x = input(">")
        

main()
