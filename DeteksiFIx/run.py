import requests

# Send the request
response = requests.post("http://localhost:5000/predict", json={
    "Jenis_Kelamin": "Perempuan",
    "Tinggi_Badan": 30,
    "Berat_Badan": 01,
    "Usia": 20
})

# Get the response
output = response.json()

# Print the output
print(output)