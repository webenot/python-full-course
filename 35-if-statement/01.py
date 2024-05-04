def route_info(route):
    if type(route.get('distance')) == int:
        return f"Distance to your destination is {route['distance']}"

    if (type(route.get('speed')) == int) and (type(route.get('time')) == int):
        return f"Distance to your destination is {route['speed'] * route['time']}"

    return 'No distance info is available'


print(route_info({'distance': 5}))
print(route_info({'speed': 5, 'time': 5}))
print(route_info({'time': 5}))
