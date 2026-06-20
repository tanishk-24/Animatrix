# Author: tanishk-24
import os
import google.generativeai as genai

# Setup Gemini API
api_client = genai.Client()

# Instruction for the model
instructions = """
Please generate a Python script utilizing the Manim Community library to demonstrate the Pythagorean Theorem visually.

Key guidelines:
- Draw a right triangle with sides named 'a', 'b', and 'c'.
- Animate squares attached to each of the three sides.
- Show the formula a^2 + b^2 = c^2 clearly.
- Include proper animations using self.play() and self.wait().
- Use color coding for the sides and their corresponding squares.

Output only the raw Python code within a single markdown block.
"""

print("Requesting code generation from Gemini...")

res = api_client.models.generate_content(
    model='gemini-2.5-flash',
    contents=instructions,
)

target_file = "pythagoras_theorem.py"

# Extract code from response
gen_text = res.text
if "```python" in gen_text:
    final_code = gen_text.split("```python")[1].split("```")[0].strip()
elif "```" in gen_text:
    final_code = gen_text.split("```")[1].split("```")[0].strip()
else:
    final_code = gen_text.strip()

with open(target_file, "w", encoding="utf-8") as file:
    file.write(final_code)

print(f"Code saved to {target_file}")