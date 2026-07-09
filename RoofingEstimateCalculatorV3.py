customer = input("Enter your first/last name: ")
city = input("Enter your city of residence: ")
roof_length = float(input("Enter the Length of your roof in feet: "))
roof_width = float(input("Enter the Width of your roof in feet: "))
roof_area = roof_length * roof_width
waste = roof_area / 10
total_area = roof_area + waste
materials_cost = total_area * 2.90

print("=" * 25)
print("Roof Estimate")
print("=" * 25)
print("\nCustomer: ", customer)
print("\nCity: ", city)
print("\nRoof Area: ", roof_area, " sq ft")
print("\nWaste: ", waste, " sq ft")
print("\nTotal Area: ", total_area, " sq ft")
print("\nMaterials Cost: $", materials_cost)