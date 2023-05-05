def only_english(string1):
    mes = ''.join([str(i) for i in string1 if(i >= "a" and i <= "z") or (i >= "A" and i <= "Z") ])
    return mes
print(only_english("4ommyx_"))