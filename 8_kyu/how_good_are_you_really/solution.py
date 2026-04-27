def better_than_average(class_points, your_points):
    average_class_point = sum(class_points) / len(class_points)
    if average_class_point >= your_points:
        return False
    return True

print(better_than_average([50, 50, 50], 50))