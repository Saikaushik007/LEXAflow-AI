# src/main.py
# LEXAflow AI - Prototype Entry Point

from context_engine import ContextEngine

# Sample policy corpus (could later be loaded from policy_store.py or JSON)
policy_corpus = {
    "clause_001": "All claims must be submitted within 30 days.",
    "clause_002": "Coverage includes fire, theft, and accidental damage.",
    "clause_003": "Exclusions apply to natural disasters and war-related damages."
}

def main():
    # Initialize context engine with policies
    engine = ContextEngine(policy_corpus)
    
    print("LEXAflow AI system initialized")
    
    # Sample queries for demonstration
    sample_queries = [
        "What is the coverage for fire?",
        "How can I file a claim?",
        "Tell me about exclusions."
    ]
    
    for query in sample_queries:
        response = engine.generate_response(query)
        print(f"\nQuery: {query}")
        print(f"Detected Intent: {response['intent_detected']}")
        print("Matched Clauses:")
        for cid, text in response["matched_clauses"].items():
            print(f"- {cid}: {text}")

if __name__ == "__main__":
    main()
