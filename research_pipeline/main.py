from agents.orchestrator import OrchestratorAgent
from agents.problem_decomposition import ProblemDecompositionAgent
from agents.knowledge_base_config import KnowledgeBaseConfigAgent
from agents.contextual_retrieval import ContextualRetrievalAgent
from agents.data_validation import DataValidationAgent
from agents.scenario_simulation import ScenarioSimulationAgent
from agents.insight_generation import InsightGenerationAgent
from agents.report_generation import ReportGenerationAgent
from utils.state_management import ResearchState
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.openai import OpenAI

def run_research_pipeline():
    state = ResearchState()
    root_memory = ChatMemoryBuffer.from_defaults(token_limit=16000)
    
    # Initialize all agents
    agents = {
        "orchestrator": OrchestratorAgent(state),
        "problem_decomposition": ProblemDecompositionAgent(state),
        "knowledge_base_config": KnowledgeBaseConfigAgent(state),
        "contextual_retrieval": ContextualRetrievalAgent(state),
        "data_validation": DataValidationAgent(state),
        "scenario_simulation": ScenarioSimulationAgent(state),
        "insight_generation": InsightGenerationAgent(state),
        "report_generation": ReportGenerationAgent(state)
    }

    orchestrator = agents["orchestrator"]

    while not state.is_completed():
        next_step = orchestrator.decide_next_agent()
        current_agent = agents[next_step]

        if next_step == "problem_decomposition" and state.is_first_run():
            user_input = input("Enter your research question: ")
            state.set_research_question(user_input)
        else:
            user_input = state.get_last_output()

        print(f"\nExecuting {next_step.replace('_', ' ').capitalize()} Agent...")
        response = current_agent.run(user_input, chat_history=root_memory.get())
        print(f"{next_step.replace('_', ' ').capitalize()} Agent output: {response}\n")

        state.update_step(next_step, response)
        root_memory.put(response)

    print("Research pipeline completed. Final report generated.\n")
    print(state.get_final_report())

if __name__ == "__main__":
    run_research_pipeline()