import folium

m = folium.Map((0, 0), zoom_start=3, tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png', 
               attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')

map_title = "Peng's Footprints"
title_html = f'<h2 style="position:absolute;z-index:100000;left:40vw" >{map_title}</h2>'
m.get_root().html.add_child(folium.Element(title_html))

# visited
visited = folium.FeatureGroup("visited").add_to(m)
## China
folium.Marker((37.3821099, 117.97279), tooltip="Binzhou", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((36.6518399, 117.12009), tooltip="Jinan", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((36.8130999, 118.0548), tooltip="Zibo", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((36.0662299, 120.38299), tooltip="Qingdao", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((39.904211, 116.407395), tooltip="Beijing", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((39.085099, 117.199369), tooltip="Tianjin", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((31.230416, 121.473701), tooltip="Shanghai", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((31.2983399, 120.58319), tooltip="Suzhou", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((30.2741499, 120.15515), tooltip="Hangzhou", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((32.0583799, 118.79647), tooltip="Nanjing", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((34.2658138, 108.9540936), tooltip="Xian", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((29.5656843, 106.5511838), tooltip="Chongqing", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((24.8797, 102.8332), tooltip="Kunming", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((23.1290799, 113.26436), tooltip="Guangzhou", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((32.7811199, 119.45558), tooltip="Gaoyou", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((21.4811199, 109.12008), tooltip="Beihai", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((28.2277799, 112.93886), tooltip="Changsha", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((37.4336499, 118.67466), tooltip="Dongying", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((42.5387299, 125.7121), tooltip="Meihekou", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((22.3193039, 114.1693611), tooltip="Hong Kong", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((34.4142699, 115.65635), tooltip="Shangqiu", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((29.9853899, 122.20778), tooltip="Zhoushan", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((29.995762, 120.586109), tooltip="Zhoushan", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
## Southeast Asia
folium.Marker((3.1319197, 101.6840589), tooltip="Kuala Lumpur", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((1.352083, 103.819836), tooltip="Singapore", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((13.7563309, 100.5017651), tooltip="Bangkok", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((14.6090537, 121.0222565), tooltip="Metro Manila", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
## USA
folium.Marker((41.8781136, -87.6297982), tooltip="Chicago", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((37.7749295, -122.4194155), tooltip="San Francisco", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)
folium.Marker((34.0549076, -118.242643), tooltip="Los Angeles", icon=folium.Icon("blue", icon="shoe-prints", prefix="fa")).add_to(visited)

# planned
planned = folium.FeatureGroup("planned").add_to(m)
folium.Marker((40.7127753, -74.0059728), tooltip="New York", icon=folium.Icon("red", icon="flag")).add_to(planned)
folium.Marker((48.8575, 2.3514), tooltip="Paris", icon=folium.Icon("red", icon="flag")).add_to(planned)
folium.Marker((51.5072, 0.1276), tooltip="London", icon=folium.Icon("red", icon="flag")).add_to(planned)
folium.Marker((35.6764, 139.6500), tooltip="Tokyo", icon=folium.Icon("red", icon="flag")).add_to(planned)

folium.LayerControl().add_to(m)
m.save("index.html")