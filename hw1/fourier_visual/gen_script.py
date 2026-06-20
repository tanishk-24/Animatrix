# Author: tanishk-24
import os
import google.generativeai as genai

# Setup API
client_api = genai.Client()

# Prompt for the animation
task_desc = """
Develop a Python script with the Manim Community library to visualize the Fourier Series.

Specific requirements:
- Illustrate a square wave construction using a sum of sine waves.
- Display the first 5 odd harmonics.
- Assign a unique color to each harmonic wave.
- Animate the cumulative sum progressively.
- Add an appropriate title, axes, and labels.

Provide solely the executable Python code inside a markdown block.
"""

print("Submitting Fourier Series task to Gemini...")

resp = client_api.models.generate_content(
    model='gemini-2.5-flash',
    contents=task_desc,
)

out_file = "fourier_animation.py"

# Parse code
output_text = resp.text
if "```python" in output_text:
    extracted = output_text.split("```python")[1].split("```")[0].strip()
elif "```" in output_text:
    extracted = output_text.split("```")[1].split("```")[0].strip()
else:
    extracted = output_text.strip()

with open(out_file, "w", encoding="utf-8") as fh:
    fh.write(extracted)

print(f"Saved to {out_file}!")