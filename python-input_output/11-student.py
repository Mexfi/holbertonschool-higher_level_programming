#!/usr/bin/python3
def pascal_triangle(n):
    """Returns Pascal's triangle of n"""
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [1]  # Every row starts with 1
        
        # Calculate middle elements for rows after the first
        if i > 0:
            prev_row = triangle[i-1]
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])
            row.append(1)  # Every row ends with 1
        
        triangle.append(row)
    
    return triangle
