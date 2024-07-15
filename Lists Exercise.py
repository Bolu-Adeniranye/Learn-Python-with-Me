sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = int(input("Add sales for today"))
sales_w2.append(new_day)
sales.extend(sales_w1)
sales.extend(sales_w2)

print(sales)
bestDay = sales[-1] * 1.5
worstDay = sales[0] * 1.5

print(bestDay)
print(worstDay)

print(bestDay * worstDay)

