def format_name(s):
    x1 = s[0].upper()
    x2 = s[1:].lower()
    return x1+x2
print map(format_name, ['adam', 'LISA', 'barT'])
