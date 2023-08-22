f1 = {"s":3 , "m":4} 
f2 = {"s":5 , "m":6}

def sum(f1, f2):
    result = {} 
    result["s"] =(f1["s"] * f2["m"]) + (f2["s"] * f1["m"])
    result["m"] =f1["m"] * f2["m"]
    return result

def mutiple(f1, f2):
    result = {}
    result["s"] =f1["s"] * f2["s"]
    result["m"] =f2["m"] * f2["m"]
    return result

def subtract(f1 ,f2):
    result = {}
    result["s"] =(f1["s"] * f2["m"]) - (f2["s"] * f1["m"])
    result["m"] =f1["m"] * f2["m"]
    return result

def divide(f1, f2):
    result = {}
    result["s"] =f1["s"] * f2["m"]
    result["m"] =f2["m"] * f2["s"]
    return result  

def show(r):
    print(f"{r['s']} / {r['m']}")

result_S = sum(f1, f2)
show(result_S)

result_m = mutiple(f1, f2)
show(result_m)

result_sub = subtract(f1, f2)
show(result_sub)

result_d = divide(f1, f2)
show(result_d)