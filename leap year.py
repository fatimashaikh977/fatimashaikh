year=int(input("enter the year:"))

if(year %400 ==00):{
    print("the {}  is leap year".format( year))
}
elif(year %100==0):{
    print("the {}  is not leap year".format( year))
}
elif(year%4==0):{
    print("the {}  is a leap year".format( year))
}
else:{
    print("{}  is not an leap year".format( year))
}