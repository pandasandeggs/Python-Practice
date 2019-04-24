def tip():
    price = float(raw_input("How much did your meal cost? "))

    ten = float(price) * .10
    fifteen = float(price) * .15
    twenty = float(price) * .2

    print """If your meal costs %.2f then your tip options are:
    Ten Percent - %.2f
    Fifteen Percent - %.2f
    Twenty Percent - %.2f """ % (round(price,2), round(ten,2), round(fifteen,2), round(twenty,2))


tip()
