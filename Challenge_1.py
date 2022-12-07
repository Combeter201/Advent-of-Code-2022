def function():
    # read file line by line
    file = open("input.txt", "r")
    i = []
    for n in file.readlines():
        if n.strip() != '':
            i.append(int(n.strip()))
        else:
            i.append("")

    # Nutrition score summed up in a list
    nutriscore_sum = 0
    nutriscore_list = []

    for m in i:
        if m == "":
            nutriscore_list.append(nutriscore_sum)
            nutriscore_sum = 0
        else:
            nutriscore_sum += m
    print(max(nutriscore_list))

    # Top 3 Nutrition score summed up
    t3 = 0
    nutriscore_list.sort(reverse=True)
    for s in nutriscore_list[:3]:
        t3 += s
    print(t3)


if __name__ == '__main__':
    function()
