# Seva-Portal
Seva Portal
-----------
Seva Portal is a web application that helps Indian citizens discover government schemes they are eligible for, based on their personal information and status. The platform provides a seamless experience from Sign Up → Login → Dashboard → Evaluation, guiding users to the most relevant schemes.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Key Features
-------------
Sign Up / Login: Secure user authentication with email, phone, and password.
Dashboard: Home, About, Updates, Evaluate, and Profile sections.
Home: Personalized user overview.
About: Application description.
Updates: Latest government news on citizen schemes.
Evaluate: Ask essential questions to predict suitable government schemes.
Profile: User information with logout functionality.
Scheme Recommendation: Personalized suggestions based on real-time user data and government scheme criteria.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Role of Qdrant
--------------
Seva Portal leverages Qdrant, a high-performance vector database, to enable semantic matching between users and government schemes:

User information and scheme details are converted into vector embeddings.
Qdrant performs similarity-based searches to identify the most relevant schemes for each user.
Provides fast, scalable, and accurate recommendations, even with hundreds of schemes and thousands of users.
Integrates seamlessly with AI embeddings to improve predictive capabilities over time.
By using Qdrant, Seva Portal transforms traditional information lookup into a smart recommendation engine, ensuring citizens receive personalized and timely guidance about government benefits.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Tech Stack
----------
Frontend: Streamlit
Backend: FastAPI
Database: Qdrant (Vector store for scheme matching)
Embeddings: OpenAI embeddings for user & scheme data
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Project Structure
------------------
con4/
├─ backend/
│  ├─ auth/
│  │  ├─ routes.py
│  │  └─ __init__.py
│  ├─ schemas.py
│  ├─ utils/
│  │  └─ embeddings.py
│  ├─ vectorstore/
│  │  └─ qdrant_store.py
│  └─ main.py
├─ frontend/
│  └─ app.py
├─ requirements.txt
└─ README.md
