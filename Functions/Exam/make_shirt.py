# имитация печати на футблке
def make_shirt(size='L', text='I love Python', color=''):
    if color:
        data = f"Your shirt: size {size.title()}, content '{text.title()}', color {color.title()}"
    else:
        data = f"Your shirt: size {size.title()}, content '{text.title()}'"
    return data

print(make_shirt())
print(make_shirt('s', 'Tets', 'Green'))