"""
Context Engine Module
---------------------
Responsible for understanding user intent, extracting key entities,
and mapping them to relevant policy clauses.
"""

import re
from typing import Dict, List


class ContextEngine:
    def __init__(self, policy_corpus: Dict[str, str]):
        """
        Initializes the context engine with indexed policy data.
        policy_corpus: Dictionary of clause_id -> clause_text
        """
        self.policy_corpus = policy_corpus

    def preprocess(self, query: str) -> List[str]:
        """
        Cleans and tokenizes the user query for intent understanding.
        """
        query = query.lower()
        query = re.sub(r"[^a-zA-Z0-9\s]", "", query)
        tokens = query.split()
        return tokens

    def extract_intent(self, tokens: List[str]) -> str:
        """
        Determines the intent based on keywords.
        """
        if "claim" in tokens:
            return "CLAIM_QUERY"
        if "coverage" in tokens:
            return "COVERAGE_QUERY"
        if "exclusion" in tokens:
            return "EXCLUSION_QUERY"
        return "GENERAL_POLICY_QUERY"

    def retrieve_relevant_clauses(self, intent: str) -> Dict[str, str]:
        """
        Retrieves clauses relevant to the detected intent.
        """
        results = {}
        for clause_id, text in self.policy_corpus.items():
            if intent.split("_")[0].lower() in text.lower():
                results[clause_id] = text
        return results

    def generate_response(self, query: str) -> Dict[str, str]:
        """
        End-to-end pipeline: query → intent → relevant clauses.
        """
        tokens = self.preprocess(query)
        intent = self.extract_intent(tokens)
        clauses = self.retrieve_relevant_clauses(intent)

        return {
            "intent_detected": intent,
            "matched_clauses": clauses
        }
