from google.cloud import bigquery
from agent_starter_pack.src.agent.base import BaseAgent
from agent_starter_pack.agents.data_agent import DataAgent

class DataAgent(BaseAgent):
    async def execute(self, input_data: dict) -> dict:
        client = bigquery.Client()
        query = input_data.get("query", "SELECT 1")
        results = client.query(query).to_dataframe()
        return {"data": results.to_dict()}