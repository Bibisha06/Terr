import folium

# Create a basic map centered on a location
m = folium.Map(location=[20.5937, 78.9629], zoom_start=4)

# Add a marker
folium.Marker([20.5937, 78.9629], tooltip='India').add_to(m)

# Save the map
m.save('test_map.html')

print("Map created successfully!")
