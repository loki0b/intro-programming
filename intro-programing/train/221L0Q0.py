arthur_average_dm = int(input())
luiz_average_dm = int(input())
pedro_average_dm = int(input())

time = int(input())

maxx = (arthur_average_dm + luiz_average_dm + abs(arthur_average_dm - luiz_average_dm)) / 2
maxx = (maxx + pedro_average_dm + abs(maxx - pedro_average_dm)) / 2

maxx = maxx * time

print(int(maxx))
