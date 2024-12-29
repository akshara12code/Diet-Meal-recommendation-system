import json
from flask import Flask, render_template, request, jsonify, Response
from llama_cpp import Llama
from typing import List, Dict, Generator

app = Flask(__name__)

# Path to your GGUF model
# MODEL_PATH = "E:/komal/komal135/llama-3-8b-Instruct-bnb-4bit-aiaustin-demo/unsloth.Q4_K_M.gguf"
MODEL_PATH = "E:/komal/komal135/llama-3-8b-Instruct-bnb-4bit-aiaustin-demo/unsloth.Q4_K_M.gguf"
try:
    llm = Llama(model_path=MODEL_PATH,n_threads=None,
                verbose=False,n_ctx=2048)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

def format_chat_messages(messages: List[Dict[str, str]]) -> str:
    """
    Format chat messages into a single prompt string.
    
    Args:
        messages (List[Dict[str, str]]): List of message dictionaries with 'role' and 'content' keys.
    
    Returns:
        str: Formatted prompt string for the model
    """
    formatted_prompt = ""
    for msg in messages:
        role = msg['role']
        content = msg['content']
        
        if role == 'system':
            formatted_prompt += f"<|system|>\n{content}\n"
        elif role == 'user':
            formatted_prompt += f"<|user|>\n{content}\n"
        elif role == 'assistant':
            formatted_prompt += f"<|assistant|>\n{content}\n"
    formatted_prompt += "<|assistant|>\n"
    
    return formatted_prompt

def stream_chat(messages: List[Dict[str, str]], max_tokens: int = 2048, temperature: float = 0.7) -> Generator[str, None, None]:
    """
    Stream chat responses from the Llama model with improved handling.
    
    Args:
        messages (List[Dict[str, str]]): List of messages in conversation
        max_tokens (int): Maximum tokens to generate
        temperature (float): Sampling temperature
    
    Yields:
        str: Streamed response tokens
    """
    # Format messages into a single prompt
    formatted_prompt = format_chat_messages(messages)

    try:
        response = llm(
            formatted_prompt, 
            max_tokens=max_tokens, 
            temperature=temperature, 
            stream=True,
            stop=["</response>"] 
        )
        
        full_response = ""
        for chunk in response:
            if chunk and 'choices' in chunk and chunk['choices']:
                token = chunk['choices'][0].get('text', '')
                if token:
                    full_response += token
                    yield token

        if len(full_response) < max_tokens:
            yield "\n\nNote: Full meal plan generation may have been truncated. Please regenerate if needed."
    
    except Exception as e:
        yield f"\n\nError in generating response: {str(e)}"

@app.route('/')
def home():
    """Render the HTML template"""
    return render_template('chat.html')

@app.route('/generate-meal-plan', methods=['POST'])
def generate_meal_plan():
    """Generate a meal plan based on user input with streaming"""
    try:
        # Get user input from request
        user_data = request.json
        age = user_data.get("age")
        gender = user_data.get("gender")
        weight = user_data.get("weight")
        height = user_data.get("height")
        health_condition = user_data.get("health_condition", "None")
        allergies = user_data.get("allergies", "None")
        food_preference = user_data.get("food_preference")

        # Prepare messages for the chat
        messages = [
            {
                "role": "system", 
                "content": """
                You are an expert nutritionist creating personalized 7-day meal plans. 
                Provide a detailed meal plan with:
                - 3 meals and 1 snack per day
                - Vegetarian diet
                - Balanced nutrition
                - Detailed calorie and macronutrient breakdown
                - Varied and interesting meals
                """
            },
            {
                "role": "user", 
                "content": f"""
                Create a personalized 7-day meal plan with the following details:
                - Age: {age}
                - Gender: {gender}
                - Weight: {weight}kg
                - Height: {height}cm
                - Health Condition: {health_condition}
                - Allergies: {allergies}
                - Diet Preference: {food_preference}

                Please provide a comprehensive meal plan with:
                - Day-by-day breakdown
                - Meal details for Breakfast, Lunch, Dinner, and Snack
                - Calories and macronutrient breakdown for each meal
                - Vegetarian-friendly options
                - Variety in meals
                - Indian Meal
                """
            }
        ]

        def generate():
            for token in stream_chat(messages):
                yield f"data: {json.dumps({'token': token})}\n\n"
        
        return Response(generate(), mimetype='text/event-stream')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
