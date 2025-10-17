from flask import Flask, render_template, request, jsonify
import random
import datetime
import json

app = Flask(__name__)

# Load responses
with open("data/responses.json", encoding="utf-8") as f:
    responses = json.load(f)

def get_response(user_input):
    user_input = user_input.lower()

    # ---------------- Greetings ----------------
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return random.choice(responses["greeting"]) + " What would you like today? Workout, Diet, or Motivation?"
   
    # ---------------- Diet Suggestions ----------------
    elif any(word in user_input for word in ["diet", "food", "eat"]):
        # Specific types first
        if "fat" in user_input or "loss" in user_input or "lose weight" in user_input or "weight loss" in user_input:
            return random.choice(responses["diet_weight_loss"])
        elif "muscle" in user_input or "gain" in user_input:
            return random.choice(responses["diet_muscle_gain"])
        elif "non veg" in user_input or "non-veg" in user_input or "nonvegetarian" in user_input:
            return random.choice(responses["diet_nonveg"])
        elif "veg" in user_input or "vegetarian" in user_input:
            return random.choice(responses["diet_balanced"])
        else:
            # Only when user says just "diet" or general eating terms
            return random.choice(responses["diet_prompt"])

    # ---------------- Workout Suggestions ----------------
    if "muscle" in user_input and "gain" in user_input:
        return random.choice(responses["workout_muscle"])
    elif "fat" in user_input or "loss" in user_input or "lose" in user_input:
        return random.choice(responses["workout_fat"])
    elif "arm" in user_input:
        return random.choice(responses["workout_arms"])
    elif "leg" in user_input:
        return random.choice(responses["workout_legs"])
    elif "full body" in user_input or "full" in user_input:
        return random.choice(responses["workout_fullbody"])
    elif "workout" in user_input or "exercise" in user_input or "exercises" in user_input:
        return random.choice(responses["workout_prompt"])

        # ---------------- Motivation ----------------
    if any(word in user_input for word in ["motivation", "motivate"]):
        return random.choice(responses["motivation"])
    elif "i feel lazy" in user_input:
        return random.choice(responses["motivation_lazy"])
    elif "fitness quote" in user_input or "quote" in user_input:
        return random.choice(responses["motivation"])
    
    # ---------------- Progress Tracking ----------------
    elif "weight" in user_input or "lost" in user_input:
        return random.choice(responses["progress"])

    # ---------------- Goodbye ----------------
    elif any(word in user_input for word in ["bye", "goodnight", "see you"]):
        return random.choice(responses["goodbye"])

    # ---------------- Time ----------------
    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"Current time: {now.strftime('%H:%M:%S')}"

    # ---------------- Fallback ----------------
    else:
        return random.choice(responses["fallback"])

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form["msg"]
    bot_reply = get_response(user_msg)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)



