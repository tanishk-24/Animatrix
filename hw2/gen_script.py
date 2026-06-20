# Author: tanishk-24
import os
import google.generativeai as genai

# Client initialization
ai_client = genai.Client()

# Prompt for advanced Pythagorean visual
adv_prompt = """
Write a Python script using the Manim library. The objective is to visualize the Pythagorean Theorem (a^2 + b^2 = c^2) with a unit dissection proof for a 3-4-5 right triangle.

Criteria:
1. Draw a 3-4-5 right triangle. Scale it by 0.6 and offset it (e.g., A=(0, -0.9), B=(2.4, -0.9), C=(0, 0.9)). Label sides 'a=3', 'b=4', 'c=5'. Include a right-angle mark.
2. Construct three outward-facing squares from the triangle sides. Ensure no overlap.
3. Show calculations on the left side: title, colored equation, area breakdown (Area 1 = 9, Area 2 = 16, Target Area = 25), and final check (9+16=25).
4. Fill the squares with 0.6x0.6 grid units: 3x3 for side a (red), 4x4 for side b (blue), and 5x5 empty slots for side c.
5. Create an animation where the 9 red and 16 blue grid squares move into the 25 slots of the hypotenuse square.
6. Use self.wait() for pacing. Rely on Text objects instead of LaTeX to avoid compiler issues.

Output just the python code in a markdown block.
"""

print("Generating Advanced Pythagoras code...")

model_reply = ai_client.models.generate_content(
    model='gemini-2.5-flash',
    contents=adv_prompt,
)

target_path = "advanced_pythagoras.py"

# Extracting the code block
raw_content = model_reply.text
if "```python" in raw_content:
    py_code = raw_content.split("```python")[1].split("```")[0].strip()
elif "```" in raw_content:
    py_code = raw_content.split("```")[1].split("```")[0].strip()
else:
    py_code = raw_content.strip()

with open(target_path, "w", encoding="utf-8") as out:
    out.write(py_code)

print(f"Generated advanced animation code at {target_path}")