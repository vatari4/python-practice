def circle_length(radius):
    return 2 * 3.14159 * radius
 
 
def circle_area(radius):
    return 3.14159 * radius ** 2
 
 
def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))
