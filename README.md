Diet-Meal Recommendation System

Project Overview


The Diet-Meal Recommendation System is designed to recommend personalized meal plans based on user preferences, health conditions, fitness goals, and dietary restrictions. This system utilizes a Large Language Model (LLM) to process user inputs and suggest optimized meal plans.

<img width="1912" height="965" alt="Screenshot 2025-08-01 022822" src="https://github.com/user-attachments/assets/a1bc1a55-3030-4416-9e99-f8628afc49e6" />
<img width="1919" height="978" alt="Screenshot 2025-08-01 022844" src="https://github.com/user-attachments/assets/f3cc7a94-4767-4fe8-b840-9b7f33790616" />
<img width="1919" height="811" alt="Screenshot 2025-08-01 022906" src="https://github.com/user-attachments/assets/1e48fbbc-b518-4d24-847f-d9330acbda11" />


Features

    Personalized Recommendations: Suggest meals based on user preferences, such as vegetarian, vegan, gluten-free, etc.
    Health & Fitness Goals: Recommend meals according to weight loss, muscle gain, or maintenance goals.
    Dietary Restrictions: Suggest meals based on allergies (e.g., dairy-free, nut-free, etc.).
    User Input Processing: Collect user data through forms or a conversational interface (e.g., chatbot).
    Meal Plan Generation: Generate daily, weekly, or monthly meal plans for the user.

Technologies Used

    Python: Programming language for backend development.
    Hugging Face Transformers: For LLM models.
    Flask/Django: For creating the web-based API or application.
    OpenAI GPT: For generating meal suggestions.
    Pandas, NumPy: For data manipulation and analysis.
    SQL/NoSQL Database: To store meal database and user data.
    NLP: To process and understand user preferences and goals.

System Architecture

    User Interface:
        A web-based front-end or chatbot where users can input their meal preferences, dietary restrictions, and goals.
        Interacts with the backend via REST API or direct chatbot interaction.

    Backend:
        The backend processes the user's input, such as dietary preferences and goals.
        The LLM model is used to interpret and generate meal recommendations.

    Database:
        Stores a large set of recipes with nutritional information.
        Keeps track of user profiles, preferences, and dietary goals.

    Recommendation Engine:
        Based on user data, a recommendation engine powered by the LLM generates personalized meal plans.
        LLM-based NLP models like GPT-3 or GPT-4 are used to understand complex user inputs and suggest optimized meal plans.
