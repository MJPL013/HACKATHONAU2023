from flask import Flask, render_template, request

app = Flask(__name__)

# Define categories and user data
categories = {
    "Art": ["Digital Art", "Painting", "Photography", "Sculpture", "Crafts"],
    "Sports": ["Cricket", "Football", "Basketball", "Tennis", "Badminton"],
    "Gaming": ["Minecraft", "Valorant", "GTA V", "Among Us", "CS:GO"],
    "Reading ": ["Books", "Poetry", "Articles", "Blogs", "Novels"],
    "Programming and Coding": ["Web Development", "Data Science", "CyberSecurity", "Game development"]
}

user_data = {
    "User2": {"Painting", "Football", "Articles"},
    "User3": {"Basketball", "Minecraft", "Poetry"},
    "User4": {"CyberSecurity", "Game development", "Crafts"}
}

user_location = {}

# Main function to calculate compatibility
def calculate_compatibility(selected_options):
    compatibility_scores = {}
    
    for user, user_selection in user_data.items():
        intersection_count = len(selected_options.intersection(user_selection))
        compatibility_scores[user] = intersection_count
    
    return compatibility_scores

# Flask route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        selected_options = set(request.form.getlist("options"))
        compatibility_scores = calculate_compatibility(selected_options)
        print(user_location,user_data)
        return render_template("result.html", selected_options=selected_options, compatibility_scores=compatibility_scores, user_data=user_data)
    
    return render_template("index.html", categories=categories)

@app.route('/store_location', methods=['POST'])
def store_location():
    data = request.json
    user_location['latitude'] = data['latitude']
    user_location['longitude'] = data['longitude']
    print("User Location:", user_location)
    return 'Location stored successfully!'

if __name__ == "__main__":
    app.run(debug=True)
