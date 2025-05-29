from agent_starter_pack.src.agent.base import BaseAgent
from agent_starter_pack.agents.data_agent import DataAgent

class ReportAgent(BaseAgent):
    async def execute(self, input_data: dict) -> dict:
        analysis = input_data["data"]
        return {"report": f"Analysis complete: {len(analysis)} rows"}