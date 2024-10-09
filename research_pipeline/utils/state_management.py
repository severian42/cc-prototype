class ResearchState:
    def __init__(self):
        self.research_question = None
        self.sub_questions = []
        self.knowledge_base = []
        self.retrieved_contexts = []
        self.validated_data = []
        self.simulated_scenarios = []
        self.generated_insights = []
        self.final_report = None
        self.completed_steps = set()

    def set_research_question(self, question):
        self.research_question = question

    def add_sub_question(self, sub_question):
        self.sub_questions.append(sub_question)

    def add_to_knowledge_base(self, item):
        self.knowledge_base.append(item)

    def add_retrieved_context(self, context):
        self.retrieved_contexts.append(context)

    def add_validated_data(self, data):
        self.validated_data.append(data)

    def add_simulated_scenario(self, scenario):
        self.simulated_scenarios.append(scenario)

    def add_generated_insight(self, insight):
        self.generated_insights.append(insight)

    def set_final_report(self, report):
        self.final_report = report

    def mark_step_completed(self, step):
        self.completed_steps.add(step)

    def is_step_completed(self, step):
        return step in self.completed_steps

    def is_completed(self):
        return len(self.completed_steps) == 7  # Total number of steps

    def get_knowledge_base(self):
        return self.knowledge_base

    def get_last_output(self):
        """
        Retrieve the last output from the retrieved contexts or generated insights.
        """
        if self.retrieved_contexts:
            return self.retrieved_contexts[-1]
        elif self.generated_insights:
            return self.generated_insights[-1]
        return ""

    def update_step(self, step, output):
        if step == "problem_decomposition":
            self.add_sub_question(output)
        elif step == "knowledge_base_config":
            self.add_to_knowledge_base(output)
        elif step == "contextual_retrieval":
            self.add_retrieved_context(output)
        elif step == "data_validation":
            self.add_validated_data(output)
        elif step == "scenario_simulation":
            self.add_simulated_scenario(output)
        elif step == "insight_generation":
            self.add_generated_insight(output)
        elif step == "report_generation":
            self.set_final_report(output)
        
        self.mark_step_completed(step)

    def get_final_report(self):
        return self.final_report

    def is_first_run(self):
        return len(self.completed_steps) == 0

    def get_generated_insights(self):
        return self.generated_insights