print("=========================\n -{ CALCULATOR }-\n=========================")
print("WRITE THE NUMBER CORRESPONDING TO THE SHAPE:-\n1)Square\n3)Rectangle\n3)Triangle\n4)Circle\n5)Exit")

opt=int(input('Which shape:'))
        
if opt==1:
    side=float(input("ENTER THE SIDE OF SQUARE:"))
    print(f'THE AREA IS {side*side}')
elif opt==2:
    lenght=float(input("ENTER THE LENGTH:"))
    breath=float(input('ENTER THE BREATH :'))
    print(f'THE AREA IS:{lenght*breath}')
elif opt==3:
    height=float(input("ENTER THE HEIGHT:"))
    base=float(input("ENTER THE BASE :"))
    print(f'THE AREA IS {(height*base)/2}')
elif opt==4:
    radius=float(input('ENTER THE RADIUS :'))
    print(f'THE AREA IS {2*3.14*radius}')
elif opt==5:
    print("YOU HAVE EXITED THE SYSTEM SUCCESFULLY")
else :
    print('INVALID OPTION CHOSEN')