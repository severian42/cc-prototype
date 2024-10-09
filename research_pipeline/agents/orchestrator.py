from .base_agent import BaseAgent
from .problem_decomposition import ProblemDecompositionAgent
from .knowledge_base_config import KnowledgeBaseConfigAgent
from .contextual_retrieval import ContextualRetrievalAgent
from .data_validation import DataValidationAgent
from .scenario_simulation import ScenarioSimulationAgent
from .insight_generation import InsightGenerationAgent
from .report_generation import ReportGenerationAgent
from llama_index.core.tools import FunctionTool

class OrchestratorAgent(BaseAgent):
    def __init__(self, state):
        super().__init__(state)
        self.agents = {
            "problem_decomposition": ProblemDecompositionAgent(state),
            "knowledge_base_config": KnowledgeBaseConfigAgent(state),
            "contextual_retrieval": ContextualRetrievalAgent(state),
            "data_validation": DataValidationAgent(state),
            "scenario_simulation": ScenarioSimulationAgent(state),
            "insight_generation": InsightGenerationAgent(state),
            "report_generation": ReportGenerationAgent(state),
        }

    def get_tools(self):
        return [
            FunctionTool.from_defaults(fn=self.check_step_completion),
        ]

    def get_system_prompt(self):
        return f"""
        You are the orchestrator agent responsible for managing the research workflow.
        Your job is to decide which agent to run next based on the current state and progress.
        The current state is: {self.state}
        """

    def check_step_completion(self, step: str) -> bool:
        return self.state.is_step_completed(step)

    def decide_next_agent(self):
        """
        Decide the next agent to execute based on the current state.
        """
        workflow_order = [
            "problem_decomposition",
            "knowledge_base_config",
            "contextual_retrieval",
            "data_validation",
            "scenario_simulation",
            "insight_generation",
            "report_generation"
        ]
        
        for step in workflow_order:
            if not self.state.is_step_completed(step):
                print(f"Deciding to run: {step}")
                return step
        
        return "report_generation"  # Default to report generation if all steps are completed

    def get_agent(self, agent_name):
        return self.agents[agent_name]