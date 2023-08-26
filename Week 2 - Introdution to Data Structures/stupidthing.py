a = [1,45,5,34,23,5,82,12,35,21,8,9]
m = 6

def count_collisions(A, m):
    collision_count = {}  # Dictionary to store collision counts
    
    for num in A:
        key = num % m  # Calculate the modulo
        if key in collision_count:
            collision_count[key] += 1  # Increment collision count if key already exists
        else:
            collision_count[key] = 1  # Initialize collision count for new key
            
    sum_modulos = sum(collision_count.values())  # Sum of all modulo values
    total_collisions = sum_modulos - len(collision_count)  # Calculate total collisions
    
    print("Total collisions:", total_collisions)
    return collision_count

print(count_collisions(a, m))