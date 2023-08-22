def sum(t1,t2):
    result={}
    result["h"]=t1["h"]+t2["h"]
    result["m"]=t1["m"]+t2["m"]
    result["s"]=t1["s"]+t2["s"]



    if result["s"]>=60:
        a=result["s"]//60
        result["s"]-=a*60
        result["m"]+=a


    if result["m"]>=60:
        b=result["m"]//60
        result["m"]-=b*60
        result["h"]+=b
    return result

def subtrac(t1,t2):
    result={}
    result["h"]=t1["h"]-t2["h"]
    result["m"]=t1["m"]-t2["m"]
    result["s"]=t1["s"]-t2["s"]

    if result["m"]<0:
        b=(result["m"]//-60)+1
        result["m"]+=b*60
        result["h"]-=b

    if result["h"]<0:
        print("try again")

    if result["s"]<0:
        a=(result["s"]//-60)+1
        result["s"]+=a*60
        result["m"]-=a
    return result

def show(result):
    print(f"{result['h']}:{result['m']}:{result['s']}")

timeh1=int(input("Pleas Enter hour1:"))
timem1=int(input("Pleas Enter minute1:"))
times1=int(input("Pleas Enter second1:"))

timeh2=int(input("Pleas Enter hour2:"))
timem2=int(input("Pleas Enter minute2:"))
times2=int(input("Pleas Enter second2:"))

time1={"h":timeh1,"m":timem1,"s":times1}
time2={"h":timeh2,"m":timem2,"s":times2}

resultsum=sum(time1,time2)
show(resultsum)
resultsubtrac=subtrac(time1,time2)
show(resultsubtrac)