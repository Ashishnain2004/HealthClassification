from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from transformers import T5Tokenizer, T5ForConditionalGeneration
import pandas as pd
import tensorflow as tf

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes



@app.route("/health-predict", methods=["333333333333333333333333333333333333333333333333"])
def health_predict():
    # Load your model (adjust the path to where your .keras file is stored)
    model_path = r"D:\Programs\Python Codes\Classroom\best_model.keras"
    model = tf.keras.models.load_model(model_path)
    # data = request.json
    data = request.get_json()
    Gender = data["gender"]
    Age = data["age"]
    Occupation = data["occupation"]
    sleep_duration = data["sleep_duration"]
    quality_sleep = data["quality_sleep"]
    activity_level = data["activity_level"]
    stress_level = data["stress_level"]
    BMI = data["bmi"]
    Heart_rate = data["heart_rate"]
    Steps = data["steps"]
    Sleep_disorder = data["sleep_disorder"]
    BP_High = data["bp_high"]
    BP_Low = data["bp_low"]
    data = [Gender,	Age	,Occupation,sleep_duration,	quality_sleep,activity_level,stress_level,	BMI	,Heart_rate	,Steps,	Sleep_disorder,	BP_High	,BP_Low	, sleep_duration]
    cols = [
        "Gender",
        "Age",
        "Occupation",
        "sleep_duration",
        "quality_sleep",
        "activity_level",
        "stress_level",
        "BMI",
        "Heart_rate",
        "Steps",
        "Sleep_disorder",
        "BP_High",
        "BP_Low",
        "Sleep_Category",
    ]
    df = pd.DataFrame([data], columns=cols)
    # Preprocess input_text (adjust based on your model's requirements)
    # Example: Convert text to a tensor or suitable input format for the model

    # Make prediction
    predictions = model.predict(df)
    output = predictions[0][0]
    label = "Unhealthy"
    if output >= 0.7:
        label = "Healthy"

    return jsonify({"output": label})


###############################################
###############################################

# # Testing the model on a prompt
def generate_response(prompt):
    # Load the model and tokenizer
    model_name = r"C:\Users\ashis\Downloads\HealthCareMagic\HealthCareMagic\saved_model"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Encode the input prompt
    input_encodings = tokenizer(
        prompt,
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=512,
    )

    # Generate a response from the model
    output = model.generate(
        input_ids=input_encodings["input_ids"],
        attention_mask=input_encodings["attention_mask"],
        max_length=1024,  # Maximum length of generated text
        num_return_sequences=1,  # Number of generated outputs to return
        pad_token_id=tokenizer.eos_token_id,  # Ensure correct padding token (usually EOS token for models like GPT)
        do_sample=True,  # Enable sampling for diversity
        temperature=0.7,  # Controls randomness, 0.7 is a good balance for coherence and diversity
        top_k=50,  # Limit the sampling to the top 50 tokens (high diversity, reasonable quality)
        top_p=0.9,  # Nucleus sampling: use the top 90% of probability mass (ensures diversity while keeping quality)
        num_beams=4,  # Beam search to improve quality of generation (4 beams strikes a good balance)
        no_repeat_ngram_size=2,  # Prevents repeating bigrams to avoid redundancy in generated text
        early_stopping=True  # Stops generation when EOS token is generated
    )

    # Decode the output to text    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

@app.route("/chat-predict", methods=["POST"])
def chat_predict():
    data = request.json
    instruction = ""
    input = data.get("input_text", "")
    instruction = "If you are a doctor, please answer the medical questions based on the patient's description."
    prompt = f"question: {input} context: {instruction}"
    decoded_output = generate_response(prompt)

    return jsonify({"output": decoded_output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
