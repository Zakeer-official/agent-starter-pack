import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from agents.data_agent import DataAgent
from agents.report_agent import ReportAgent

async def run_pipeline():
    data_agent = DataAgent()
    report_agent = ReportAgent()
    
    # Execute agents sequentially
    data = await data_agent.execute({"query": "SELECT * FROM `project.dataset.table`"})
    report = await report_agent.execute(data)
    
    print(report)  # {"report": "Analysis complete: X rows"}