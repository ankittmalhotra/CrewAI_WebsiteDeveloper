import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import strategist, designer, animator, developer
from tasks import analysis_task, design_task, animation_task, coding_task

# 1. Setup Environment
load_dotenv()

# --- PRE-FLIGHT CHECK: Ensure directories and files exist to prevent errors ---
def setup_directories():
    # Create directories if they don't exist
    os.makedirs("./input", exist_ok=True)
    os.makedirs("./output", exist_ok=True)

setup_directories()
# ---------------------------------------------------------------------------

# 2. Run the Crew
website_crew = Crew(
    agents=[strategist, designer, animator, developer],
    tasks=[analysis_task, design_task, animation_task, coding_task],
    process=Process.sequential
)

if __name__ == "__main__":
    print("### Starting the Agency ###")
    result = website_crew.kickoff()
    print("\n\n########################")
    print("## Website Generated! ##")
    print("########################\n")
    print(f"File saved to: {os.path.abspath('./output/index.html')}")