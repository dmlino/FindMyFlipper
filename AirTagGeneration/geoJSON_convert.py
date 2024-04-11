import sys
import json
from geojson import Point, Feature, FeatureCollection

# Convert data to GeoJSON format
def convert_to_geojson(input_file):
    with open(input_file, 'r') as f:
        encrypted_data = json.load(f)
        
    features = []
    for item in encrypted_data.values():
        for data in item:
            lat = data["decrypted_payload"]["lat"]
            lon = data["decrypted_payload"]["lon"]
            timestamp = data["decrypted_payload"]["timestamp"]
            confidence = data["decrypted_payload"]["confidence"]
            point = Point((lon, lat))
            properties = {
                "timestamp": timestamp,
                "confidence": confidence
            }
            features.append(Feature(geometry=point, properties=properties))

    feature_collection = FeatureCollection(features)
    return feature_collection

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = input_file.replace(".json", "_output.geojson")

    geojson_data = convert_to_geojson(input_file)

    with open(output_file, 'w') as f:
        json.dump(geojson_data, f, indent=2)

    print(f"GeoJSON data saved to {output_file}")
