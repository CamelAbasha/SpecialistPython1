# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# TODO: your code here
point_a, point_b, point_c = (0, 0), (0, 4), (3, 0)

ab, bc, ac = distance(*point_a, *point_b), distance(*point_b, *point_c), distance(*point_a, *point_c)
segments = ('AB', ab), ('AC', ac), ('BC', bc)

answer, shortest_len = 'AB', ab

for seg in segments:
    if seg[1] < shortest_len:
        answer=seg[0]


print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
