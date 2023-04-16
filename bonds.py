from tabulate import tabulate

#method that prints out bond amortization schedule, for num, 1 = annualy, 2 = semianually
def bond_amortization_schedule(face_value, redemption_value ,years ,coupon_percentage ,yield_percentage, num):
    book_value = yield_rate(face_value, redemption_value ,years ,coupon_percentage ,yield_percentage, num)
    coupon_percentage = coupon_percentage / 100
    yield_percentage = yield_percentage / 100
    coupon = face_value * coupon_percentage
    table = [["Time", "Coupon", "Eff. Amnt of Interest", "Ammortized Amt", "Book Value"],
                 [0, "----", "---", "---", book_value]]
    while book_value > redemption_value:
        time = 1
        effective_interest = yield_percentage * book_value
        amount_ammortized = coupon - effective_interest
        book_value = book_value - amount_ammortized
        table.append([time, round(coupon, 2), round(effective_interest,2), 
                      round(amount_ammortized,2)
                      ,round(book_value,2)])
        time +=1 
        #to prevent infinite loop
        if time > 30:
            print("POSSIBLE INFINITE LOOP!!! CHECK QUANTITIES")
            break
    print(tabulate(table, headers="firstrow"))

#determine yield rate
def yield_rate(face_value, redemption_value ,years ,coupon_percentage ,yield_percentage, num):
    interest = yield_percentage / 100
    n = years * num
    V = 1 / (1 + interest)
    a_angle = (1-(1 + interest) ** -n) / interest
    Fr = face_value * (coupon_percentage / 100)
    C = redemption_value
    final_answer = Fr * a_angle + C * V ** n
    return round(final_answer,2)

#gives answer to specific hmk problem 6.2
def yield_rate_answer():
    answer = []
    for i in range(2,12):
        interest = i / 100
        n = 6
        V = 1 / (1 + interest)
        a_angle = (1-(1 + interest) ** -n) / interest
        Fr = 100 * 0.08
        C = 103
        calculation = Fr * a_angle + C * V ** n
        answer.append(round(calculation, 2))
    return answer
#test should result in
#  
bond_amortization_schedule(100,103,6,8,2,1)
