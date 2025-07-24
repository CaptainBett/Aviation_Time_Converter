def main():
    while True:
        time = input("Time: ").strip().lower()
        convert(time)
    

def convert(time):
    # Step 1: Split the input into two parts, time_part and period
    time_part, period = time.split(" ")
    h, m = time_part.split(":")
    h, m = float(h), float(m)
    

    # Convert from 12 hr to 24 hr clock system 
    if period == "am":
        if h == 12:
            h -= 12
            t = h + m
            t = f"{t:.2f}"
            t = t.replace(".","")
            print(f"0{t} hrs")
        elif h < 12:
            if h < 10:
                t = h + m
                t = f"{t:.2f}"
                t = t.replace(".","")
                print(f"0{t} hrs")
            else:
                t = h + m
                t = f"{t:.2f}"
                t = t.replace(".","")
                print(t,"hrs") 
    elif period == "pm":
        if h == 12:
            t = h + m
            t = f"{t:.2f}"
            t = t.replace(".","")
            print(t,"hrs")
        elif h < 12:
            h += 12
            t = h + m
            t = f"{t:.2f}"
            t = t.replace(".","")
            print(t,"hrs")   
    else:
        # Convert from 24 hr to 12 hr clock system 
        if h == 00:
            h += 12
            t = h + m
            t = f"{t:.2f}"
            t = t.replace(".",":")
            print(t,"am")
        elif h < 12:
            t = h + m
            t = f"{t:.2f}"
            t = t.replace(".",":")
            print(t,"am")   
        elif h > 12 and h < 24:
            h -= 12
            t = h + m
            t = f"{t:.2f}"
            t = t.replace(".",":")
            print(t,"pm")

         
main()
