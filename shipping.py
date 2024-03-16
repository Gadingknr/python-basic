weight = 41.5

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight >= 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Cost ground shipping is $", cost_ground)
cost_ground_premium = 125.0

print("Ground Shipping Premium $", cost_ground_premium)

if weight <= 2:
  cost_drone = weight * 4.5
elif weight >= 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Cost drone shipping is$:", cost_drone)