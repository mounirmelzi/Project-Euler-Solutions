import fractions, termcolor

fraction = fractions.Fraction(6,3)
product = fractions.Fraction(1,1)

for numerator in range(11, 100):
    if '0' in str(numerator):
        continue

    for denominator in range(numerator + 1, 100):
        if '0' in str(denominator):
            continue

        fraction = fractions.Fraction(numerator, denominator)
        temp_fraction = None

        if str(numerator)[0] == str(denominator)[0]:
            temp_fraction = fractions.Fraction(int(str(numerator)[1]), int(str(denominator)[1]))        
        elif str(numerator)[0] == str(denominator)[1]:
            temp_fraction = fractions.Fraction(int(str(numerator)[1]), int(str(denominator)[0]))
        elif str(numerator)[1] == str(denominator)[0]:
            temp_fraction = fractions.Fraction(int(str(numerator)[0]), int(str(denominator)[1]))
        elif str(numerator)[1] == str(denominator)[1]:
            temp_fraction = fractions.Fraction(int(str(numerator)[0]), int(str(denominator)[0]))

        if temp_fraction == fraction:
            print(f"{numerator}/{denominator} == {fraction} : have been found ...")
            product *= fraction

print("Final product fraction:", product)
termcolor.cprint(f"Solution: {product.denominator}", color="green")
