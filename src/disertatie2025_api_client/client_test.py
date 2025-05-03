from src.disertatie2025_api_client.client import RouterClient

client = RouterClient()

# Add a router
print(client.add_router(
    name="R_INTERNET",
    mgmt_ip="192.168.72.31",
    site="ISP"
))

# List routers
print(client.list_routers())

# Get a router by name
print(client.get_router_by_name("R_INTERNET"))

# Update a router
print(client.update_router("R_INTERNET", site="ISP_PE"))

# Send a command to a router
print(client.run_command("R_INTERNET", "show ip interface brief"))

# Delete a router
print(client.delete_router("R_INTERNET"))

