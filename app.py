from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    cafe_menu = {
        "Signature Coffee": [
            {"name": "Eufrocina's Special Brew", "price": "₱180"},
            {"name": "Spanish Latte", "price": "₱165"}
        ],
        "Fresh Pastries": [
            {"name": "Butter Croissant", "price": "₱110"},
            {"name": "Ube Cheese Pandesal", "price": "₱45"}
        ]
    }

    branches = [
        {
            "name": "SJDM Main (Kaypian)",
            "address": "193 Kaypian Rd, San Jose del Monte, Bulacan",
            "map_url": "https://maps.google.com/maps?vet=10CAAQoqAOahcKEwiQjM2emr2UAxUAAAAAHQAAAAAQDw..i&client=opera-gx&pvq=Cg0vZy8xMXprcHIzeHdoIg8KCWV1ZnJvY2luYRACGAM&lqi=CglldWZyb2NpbmFI7-bH28a-gIAIWg0QACIJZXVmcm9jaW5hkgEEY2FmZQ&fvr=1&cs=1&um=1&ie=UTF-8&fb=1&gl=ph&sa=X&ftid=0x339703ade354de2f:0xd1e857738f5d1b46",
            "hours": "8:00 AM - 9:00 PM Daily",
            "image": "sjdm.jpg"
        },
        {
            "name": "Marilao Bulacan Branch",
            "address": "Eufrocina's Cafe, Marilao, Bulacan",
            "map_url": "https://www.google.com/maps/place/Eufrocina's+Cafe+-+Marilao+Bulacan+Branch/@14.7547519,120.9525847,17z",
            "hours": "8:00 AM - 9:00 PM Daily",
            "image": "marilao.jpg"
        }
    ]

    return render_template('index.html', menu=cafe_menu, branches=branches)

if __name__ == '__main__':
    app.run(debug=True)