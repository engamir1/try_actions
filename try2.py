# سيتم عمل مقارنة بين اللسته القديمه والجديده كل عنصر ف الجديده لو موجود ف القديمه عدي ولو مش موده ضيفه ف لسته جديده وف الاخر هات طول اللسته الجديده وده يبقي العمليات الجديده
# - عمليات  اقترب تاريخ الفتح لها وستحذف
# حسب التاريخ مقارنته باليوم

stack1 = [1, 8, 15, 9, 11]  # new list
stack2 = [8, 15, 9, 11]  # old list
new_tender = []

for i in stack1:
    if i in stack2:
        pass

    else:
        new_tender.append(i)


print(f"the new tender is : {new_tender}")
print(f"the new tender is {len(new_tender)}")
