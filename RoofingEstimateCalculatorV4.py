name = input("Enter your first/last name: ")
roof_length = float(input("Enter the length of your roof in feet: "))
roof_width = float(input("Enter the width of your roof in feet: "))
waste_percentage = float(input("Enter the waste percentage (as a decimal, e.g., 0.1 for 10%): "))
price_per_square_ft = float(input("Enter the price per square ft of roofing materials: "))
roof_pitch = float(input("Enter the pitch of your roof: "))
roof_area = roof_length * roof_width
waste_amount = roof_area * waste_percentage
total_area = roof_area + waste_amount
material_cost = total_area * price_per_square_ft
labor_cost = float(input("Enter the labor cost per sq ft: "))
final_labor_cost = total_area * labor_cost
if roof_pitch >= 8:
    final_labor_cost *= 1.15 
elif roof_pitch >= 5:
    final_labor_cost *= 1
else:
    final_labor_cost *= 1
total_cost = material_cost + final_labor_cost

print("=" * 25)
print("Roofing Estimate Summary")
print("=" * 25)
print("\nCustomer name: ", name)
print("\nRoof area (sq ft): ", roof_area)
print("\nMaterial cost: $", material_cost)
print("\nLabor cost: $", final_labor_cost)
if roof_pitch >= 8: 
    print("\nNote: Labor cost increased by 15% due to steep roof pitch.")
elif roof_pitch >= 5:
    print("\nNote: Labor cost remains standard for standard roof pitch.")
else:
    print("\nNote: Labor cost remains standard for low roof pitch.")
print("\nTotal estimated cost: $", total_cost)