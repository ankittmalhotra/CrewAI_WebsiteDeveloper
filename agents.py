from crewai import Agent, LLM
from crewai_tools import FileReadTool, FileWriterTool

# Define Gemini LLMs
gemini_flash = LLM(
    model="gemini/gemini-2.5-flash-lite",
    temperature=0.5
)

gemini_pro = LLM(
    model="gemini/gemini-2.5-pro",
    temperature=0.2
)

# Tool to read the user's brief
file_read_tool = FileReadTool(file_path='./input/brief.txt')
# Tool to save the final website
file_write_tool = FileWriterTool()

# Agent 1: The Brain (Analyst)
strategist = Agent(
    role='Lead Brand & Marketing Strategist',
    goal='Uncover the core brand identity and marketing strategy from a client brief to create a modern, world-class website',
    backstory=(
        "You are a master strategist, skilled in distilling the essence of a brand. "
        "You read between the lines of a client's request to define a compelling brand identity, "
        "a modern and sophisticated color palette, and a font pairing that speaks to a premium, international audience. "
        "Your work sets the stage for a visually stunning and effective website that will win design awards."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_flash,
    tools=[file_read_tool]
)

# Agent 2: The Eye (Designer)
designer = Agent(
    role='Principal UI/UX Designer',
    goal='Create a visually stunning, modern, and user-friendly website design plan that is the best in the world',
    backstory=(
        "You are a world-class UI/UX designer with a keen eye for clean, modern aesthetics. "
        "You specialize in creating beautiful and intuitive layouts using Tailwind CSS. "
        "You think in terms of design systems, ensuring consistency in spacing, typography, and color. "
        "Your designs are not just beautiful, but also highly functional, accessible, and award-winning."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_flash
)

# Agent 3: The Hand (Developer)
developer = Agent(
    role='Lead Web Developer',
    goal='Build a pixel-perfect, responsive, and accessible website from a design plan',
    backstory=(
        "You are a seasoned web developer who translates design blueprints into clean, efficient, and beautiful code. "
        "You are a master of HTML5 and Tailwind CSS. You write semantic markup, "
        "ensure cross-browser compatibility, and prioritize accessibility (A11Y). "
        "Your code is not just functional, it's a work of art."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_pro, # Using Pro for better coding logic
    tools=[file_write_tool]
)

# Agent 4: The Animator
animator = Agent(
    role='Motion Graphics & Web Animations Specialist',
    goal='Enhance the website with subtle, elegant, and performant animations',
    backstory=(
        "You are a specialist in web animations, with a deep understanding of how motion can "
        "enhance user experience and guide the user's eye. You use libraries like GSAP and AOS (Animate on Scroll) "
        "to create smooth, aesthetically pleasing animations that are optimized for performance. "
        "Your animations are not just decorative; they serve a purpose, making the website feel more "
        "dynamic, engaging, and modern."
    ),
    verbose=True,
    allow_delegation=False,
    llm=gemini_flash  # Flash is sufficient for generating animation ideas and code snippets
)
