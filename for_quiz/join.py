p = Product.objects.filter(categories__name="Information Technology")[:10]

for i in p:
    print("ID: %d, PRODUCT NAME: %s, PRODUCT CATEGORY:" %(i.id, i.name), end=" ")
    t=()
    for j in (i.categories.all()):
        t += (j.name, )
#         print("PRODUCT ID: %d" %())
    x = ", ".join(t)
    print(x)
