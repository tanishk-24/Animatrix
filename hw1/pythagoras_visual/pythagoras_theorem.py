# Author: tanishk-24
from manim import *

class PythagoreanTheoremProof(Scene):
    def construct(self):
        # Setup the triangle vertices
        pt_A = ORIGIN
        pt_B = RIGHT * 3
        pt_C = UP * 4

        # Draw lines for sides
        base_line = Line(pt_A, pt_B, color=ORANGE)
        height_line = Line(pt_A, pt_C, color=PURPLE)
        hypotenuse_line = Line(pt_C, pt_B, color=TEAL)

        # Create a polygon for the triangle
        right_triangle = Polygon(pt_A, pt_B, pt_C, fill_opacity=0.15, fill_color=GRAY, stroke_width=2)

        # Add the right angle symbol
        angle_indicator = RightAngle(base_line, height_line, length=0.35, color=WHITE)

        # Add side length labels
        lbl_height = Text("a", color=PURPLE).next_to(height_line, LEFT, buff=0.2)
        lbl_base = Text("b", color=ORANGE).next_to(base_line, DOWN, buff=0.2)
        lbl_hyp = Text("c", color=TEAL).next_to(hypotenuse_line, UR, buff=0.1)

        # Draw squares on each side
        sq_base = Square(side_length=3, stroke_color=ORANGE, fill_color=ORANGE, fill_opacity=0.4)
        sq_base.next_to(base_line, DOWN, buff=0)

        sq_height = Square(side_length=4, stroke_color=PURPLE, fill_color=PURPLE, fill_opacity=0.4)
        sq_height.next_to(height_line, LEFT, buff=0)

        sq_hyp = Square(side_length=5, stroke_color=TEAL, fill_color=TEAL, fill_opacity=0.4)
        rot_angle = hypotenuse_line.get_angle()
        sq_hyp.rotate(rot_angle)
        sq_hyp.move_to(hypotenuse_line.get_center()).shift(UP * 1.5 + RIGHT * 2.0)

        # Equation text
        formula = Text("a² + b² = c²", t2c={"a²": PURPLE, "b²": ORANGE, "c²": TEAL})
        formula.to_edge(UP).shift(LEFT * 4)

        # Animate everything
        self.play(Write(formula))
        self.wait(0.5)

        self.play(Create(right_triangle), Create(angle_indicator))
        self.play(Write(lbl_height), Write(lbl_base), Write(lbl_hyp))
        self.wait(1)

        self.play(FadeIn(sq_height, shift=RIGHT), run_time=1)
        self.play(FadeIn(sq_base, shift=UP), run_time=1)
        self.play(FadeIn(sq_hyp), run_time=1.5)
        
        self.wait(2)