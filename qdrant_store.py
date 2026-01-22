from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams
from utils.embeddings import embed_text

# Connect to Qdrant
client = QdrantClient(url="http://localhost:6333")
COLLECTION_NAME = "seva_portal_users"

def create_qdrant_collection():
    if COLLECTION_NAME not in [c.name for c in client.get_collections().collections]:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors=VectorParams(size=1536, distance="Cosine")
        )

# Save user info in Qdrant
def save_user(user: dict):
    vector = embed_text(user["email"])  # Embed email for vector search
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[{
            "id": user["email"],
            "vector": vector,
            "payload": user
        }]
    )

# Verify login credentials
def verify_user(phone_or_email: str, password: str):
    result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=embed_text(phone_or_email),
        limit=1
    )
    if result:
        user = result[0].payload
        return user["password"] == password
    return False

# Evaluate suitable schemes based on user details
def evaluate_schemes(user_payload: dict):
    user_vector = embed_text(user_payload["email"])
    results = client.search(
        collection_name="gov_schemes",
        query_vector=user_vector,
        limit=5
    )
    return [r.payload["scheme_name"] for r in results]
