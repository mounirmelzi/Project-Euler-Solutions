def gencount(coins):
    if len(coins) == 0: return lambda i0: 0    
    if len(coins) == 1: return lambda i0: int(i0 % coins[0] == 0)

    coins = sorted(coins, reverse=True)
    code = "lambda i0: sum( 1"

    for i, c in enumerate(coins[:-1]):
        code += f" for i{i+1} in range( i{i}, -1, -{c})"

    if coins[-1] != 1:
        code += f"if i{i+1} % {coins[-1]} == 0"

    code += " )"
    return eval(code)


print(gencount(( 1, 2, 5, 10, 20, 50, 100, 200 ))(200))
