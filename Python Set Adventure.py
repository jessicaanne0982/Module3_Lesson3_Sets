# Task 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

matching_routes = our_routes.intersection(competitor_routes)
unique_routes = our_routes.difference(competitor_routes)
routes_unique_to_both = our_routes.symmetric_difference(competitor_routes)

print("Both airlines fly to: ", matching_routes)
print("Only my airline flies to: ", unique_routes)
print("The routes unique to both airlines are: ", routes_unique_to_both)

