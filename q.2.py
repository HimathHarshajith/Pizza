toppings=["Beacon","Carrot","Cheese","Chicken","Fish","Greenchilies",
          "Ham","Meatballs","Mushrooms","Onions","Pepers","Pineapple",
          "Sausage","Tomato"]
Noc=[92,25,85,35,60,5,45,120,10,15,8,20,125,14] #Number of Calaries


a=str(input("Input here : "))
l=a.split(' ')

psCal=0 
for i in range (len(l)):
    if i%2 != 0: #pizza slices belongs to odd places 
        psCal=psCal+int(l[i])*250 #calaries in pizza slices


topcal=0
for j in range(1,len(l)):       #Topping slices belongs to even places
    if j%2==0:           
        k=l[j].split(',')
        
        for r in range(len(k)):
            for s in range(len(Noc)):
                
                if toppings[s]==k[r]:
                    topcal=topcal+(int(l[j-1])*int(Noc[s]))
print("The total calorie intake is",str(psCal+topcal)+'\n')      


