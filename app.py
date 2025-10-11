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
    if "diet" in user_input or "food" in user_input or "eat" in user_input:
        if "weight" in user_input or "lose" in user_input:
            return random.choice(responses["diet_weight_loss"])
        elif "muscle" in user_input or "gain" in user_input:
            return random.choice(responses["diet_muscle_gain"])
        elif "non veg" in user_input or "non-vegetarian" in user_input:
            return random.choice(responses["diet_nonveg"])
        elif "veg" in user_input or "vegetarian" in user_input:
            return random.choice(responses["diet_balanced"])
        else:
            return random.choice(responses["diet_balanced"])


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
    elif "motivate" in user_input or "lazy" in user_input:
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


