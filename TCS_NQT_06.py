# l=["Apple","Banana","apple","Banana",]
prduct=list(map(str , input().split()))
prize=list(map(int, input().split()))
quantity=list(map(int, input().split()))
# total_sale=map(int, sum(prize* quantity))
revenue=[]
for i in range(len(prduct)):
    revenue.append(prize[i]* quantity[i])
print(f"total revenue : {sum(revenue)}")

max_revenue=max(revenue)
index = revenue.index(max_revenue)
most_sold_item =prduct[index]
average_revenue = sum(revenue) / len(prduct)

print("Most Sold Item:", most_sold_item)
print("Average Revenue:", average_revenue)





