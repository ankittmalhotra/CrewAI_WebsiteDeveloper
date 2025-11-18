from crewai import Task
from agents import strategist, designer, animator, developer

# Task 1: Analyze the Input
analysis_task = Task(
    description=(
        "Read the file './input/brief.txt' and analyze the client's request. "
        "1. Identify the company name, industry, and core offerings. "
        "2. Define a modern, premium color palette with 4-5 complementary hex codes (e.g., a primary, secondary, accent, and neutral colors). "
        "3. Recommend a font pairing from Google Fonts that fits a modern, clean, and luxurious aesthetic. "
        "4. Write a compelling headline and a concise, engaging subheadline for the Hero Section that will captivate the user."
    ),
    expected_output='A structured document detailing the brand identity, an expanded color palette (with hex codes), recommended premium fonts, and captivating hero section copy.',
    agent=strategist
)

# Task 2: Create the Blueprint
design_task = Task(
    description=(
        "Using the brand identity from the Strategist, create a detailed UI plan for a world-class website. "
        "1. Specify the Google Fonts to be used in the HTML head. "
        "2. Define the Tailwind CSS configuration for the color palette. "
        "3. Create a list of all website sections (e.g., Navbar, Hero, About, Services, Features, Testimonials, Contact, Footer). "
        "4. For each section, describe the layout, key UI elements, and the specific Tailwind CSS classes for colors, spacing, and typography. "
        "Focus on creating a clean, modern design with excellent visual hierarchy, generous use of whitespace, and a premium feel. "
        "Your design should be award-winning."
    ),
    expected_output='A comprehensive UI design document with Google Font links, Tailwind color configuration, and a detailed breakdown of each section with specific Tailwind classes for a world-class website.',
    agent=designer,
    context=[analysis_task] # Wait for task 1
)

# Task 3: Add Animations
animation_task = Task(
    description=(
        "Based on the design plan, propose and describe subtle, elegant animations to enhance the user experience. "
        "1. Identify key elements for animation (e.g., hero section text, service cards, buttons). "
        "2. For each element, describe the animation type (e.g., fade-in, slide-in-up, subtle hover effects). "
        "3. Recommend a library like AOS (Animate on Scroll) and provide the necessary CDN link and initialization script. "
        "4. Specify the AOS attributes (e.g., `data-aos='fade-up'`) to be added to the HTML elements."
    ),
    expected_output='A document outlining the animation strategy, including CDN links, initialization scripts, and specific data attributes for HTML elements.',
    agent=animator,
    context=[design_task]
)

# Task 4: Write the Code
coding_task = Task(
    description=(
        "Based on the UI design plan and animation strategy, write the complete 'index.html' file. "
        "1. Use semantic HTML5 boilerplate. "
        "2. Include the specified Google Fonts, Tailwind CSS CDN, and animation library (AOS) CDN in the <head>. "
        "3. Implement all sections as described in the design plan, using the exact Tailwind CSS classes provided. "
        "4. Integrate the animations by adding the specified data attributes to the HTML elements. "
        "5. Ensure the website is fully responsive, accessible, and pixel-perfect. "
        "6. Write all code into a single 'index.html' file and save it to './output/index.html' using the file writer tool."
    ),
    expected_output='A single, valid, and responsive index.html file with modern animations, saved to the output directory.',
    agent=developer,
    context=[analysis_task, design_task, animation_task],
    output_file='./output/index.html'
)
