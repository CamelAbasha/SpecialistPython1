# Даны два уравнения прямых вида у=kx+b и виде строки. Проверить, пересекаются ли данные прямые?
# Примеры уравнений: "y = 2x + 4"  "y = -12x -12"

# Проверьте входные данные на корректность

def intersection(equation1, equation2):
    try:
        if (equation1.split()[1] + equation2.split()[1] == '==' and
                equation1.split()[3] + equation1.split()[3] in ('++', '+-', '-+', '--')):     # проверяется, те ли знаки стоят            
            return equation1.split()[2] != equation2.split()[2]                               # проверяется, равны ли 2ые коэффициенты
        raise ValueError
    except ValueError:
        return "Уравнения прямых введены некорректно"

e1 = "y = -12x + 4"
e2 = "y = +2x + 6"

print(intersection(e1, e2))
