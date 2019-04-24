def tip():
    price = raw_input("How much did your meal cost?" )
    ten = float(price) * .10
    fifteen = float(price) * .15
    twenty = float(price) * .2
    tips = """If your meal costs {} then your tip options are:
    10% - {}
    15% - {}
    20% - {}""".format(price, ten, fifteen, twenty)
    print tips

tip()
