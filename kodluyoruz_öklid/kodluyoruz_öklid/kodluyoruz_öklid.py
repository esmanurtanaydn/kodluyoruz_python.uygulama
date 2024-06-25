def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

# Noktalarý tanýmlayýn
points = [(1, 2), (4, 7), (3, 5), (0, 0)]

# Mesafeleri hesaplayýn
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclidean_distance(points[i], points[j]))

# Minimum mesafeyi bulun
min_distance = min(distances)

print(f"Minimum mesafe: {min_distance:.6f}")


