# from collections import deque
#
# count_of_pumps = int(input())
# pumps_data = deque()
# for i in range(count_of_pumps):
#     current_fuel, current_km = input().split()
#     pumps_data.append([int(current_fuel), int(current_km)])
#
# index = 0
# fuel_left = 0
# copy_pumps_data = pumps_data.copy()
#
# while copy_pumps_data:
#     petrol, km = copy_pumps_data.popleft()
#     fuel_left += petrol
#     if fuel_left < km:
#         index += 1
#         pumps_data.rotate(-1)
#         copy_pumps_data = pumps_data.copy()
#         fuel_left = 0
#     else:
#         fuel_left -= km
# print(index)


from collections import deque

count_of_pumps = int(input())
pumps_data = deque()
for i in range(count_of_pumps):
    current_fuel, current_km = input().split()
    pumps_data.append([int(current_fuel), int(current_km)])

start_position = 0
stops = 0

while stops < count_of_pumps:
    fuel_left = 0
    for i in pumps_data:
        new_fuel, km = i
        fuel_left += new_fuel
        if km > fuel_left:
            start_position += 1
            pumps_data.rotate(-1)
            stops = 0
            break
        fuel_left -= km
        stops += 1
print(start_position)