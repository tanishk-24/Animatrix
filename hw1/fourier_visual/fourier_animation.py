# Author: tanishk-24
from manim import *
import numpy as np

class SquareWaveFourier(Scene):
    def construct(self):
        # Title of the animation
        heading = Text("Square Wave via Fourier Series", font_size=32)
        heading.to_edge(UP, buff=0.5)
        self.play(Write(heading))
        
        # Coordinate system setup
        chart = Axes(
            x_range=[-4 * np.pi, 4 * np.pi, np.pi],
            y_range=[-2.5, 2.5, 0.5],
            x_length=11,
            y_length=5,
            axis_config={"color": DARK_GRAY},
            tips=False
        )
        chart.center()
        
        lbl_x = Text("Time (t)", font_size=18).next_to(chart.x_axis.get_end(), DOWN)
        lbl_y = Text("Amplitude", font_size=18).next_to(chart.y_axis.get_end(), UP)
        
        self.play(Create(chart), Write(lbl_x), Write(lbl_y))
        self.wait(1)
        
        # Odd harmonics for square wave
        harmonic_nums = [1, 3, 5, 7, 9]
        palette = [RED, ORANGE, YELLOW, GREEN, BLUE]
        
        # UI list
        info_header = Text("Harmonics Included:", font_size=20).to_corner(UL, buff=1.0)
        self.play(Write(info_header))
        
        last_ui_elem = info_header
        sum_graph = None
        
        # Animation loop
        for i, h in enumerate(harmonic_nums):
            col = palette[i]
            
            # Harmonic text info
            info_txt = Text(f"Harmonic {h}", font_size=18, color=col)
            info_txt.next_to(last_ui_elem, DOWN, buff=0.2).align_to(last_ui_elem, LEFT)
            
            # Function for the current sine wave
            func_harmonic = lambda x: (4 / (h * np.pi)) * np.sin(h * x)
            graph_harmonic = chart.plot(func_harmonic, color=col, stroke_width=2, stroke_opacity=0.7)
            
            self.play(Write(info_txt), Create(graph_harmonic), run_time=1.0)
            self.wait(0.2)
            
            # Cumulative sum function
            def get_sum_func(max_idx):
                return lambda x: sum((4 / (harmonic_nums[j] * np.pi)) * np.sin(harmonic_nums[j] * x) for j in range(max_idx + 1))
            
            graph_sum = chart.plot(get_sum_func(i), color=WHITE, stroke_width=4)
            
            if sum_graph is None:
                self.play(Create(graph_sum), run_time=1.0)
                sum_graph = graph_sum
            else:
                self.play(Transform(sum_graph, graph_sum), run_time=1.0)
                self.remove(graph_sum)
                
            self.play(FadeOut(graph_harmonic, run_time=0.5))
            last_ui_elem = info_txt
            
        # Final text
        end_text = Text("The series approximates a square wave.", font_size=22, color=WHITE)
        end_text.to_edge(DOWN, buff=0.5)
        
        self.play(Write(end_text))
        self.wait(2)