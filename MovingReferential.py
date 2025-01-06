from manim import *
from manim import bezier
from manim.typing import Point3D_Array
from manim.utils.rate_functions import ease_in_sine, ease_out_sine, ease_in_out_sine

# manim -qh -p MovingReferential.py MovingReferential

config.background_color = WHITE

class MovingReferential1(Scene):
    def construct(self):
        #plane = NumberPlane()
        #self.add(plane)
        bloc1 = Square(side_length=1, color=BLACK)
        bloc2 = Square(side_length=1, color=BLACK)
        pulley = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1)
        inclinedPlane = Polygon([-5, -2, 0], [5, -2, 0], [0, 0, 0], color=BLACK)

        bloc1.move_to([-4, -1.05, 0])
        bloc1.rotate(0.380506377)
        bloc2.move_to([4, -1.05, 0])
        bloc2.rotate(-0.380506377)
        pulley.move_to([0, 0.5, 0])
        self.add( inclinedPlane, bloc1, bloc2)

        p1 = bloc1.get_corner(UR) - [0.35, 0, 0]
        rope1 = Line(p1, [0, 1, 0], color=BLACK)
        d1 = Dot(point=p1).set_color(BLUE)
        p2 = bloc2.get_corner(UL) + [0.35, 0, 0]
        rope2 = Line([0, 1, 0], p2, color=BLACK)
        d2 = Dot(point=p2).set_color(RED)

        self.add(rope1, rope2, pulley, d1, d2)
        xaxis = Arrow(start=ORIGIN, end=RIGHT, buff=0, color=BLACK)
        x_label = Text("x", color=BLACK)
        x_label.scale(0.65)
        x_label.move_to([0.85, -0.35, 0])

        yaxis = Arrow(start=ORIGIN, end=[0, 1, 0], buff=0, color=BLACK)
        y_label = Text("y", color=BLACK)
        y_label.scale(0.65)
        y_label.move_to([-0.35, 0.85, 0])
        dref = Dot(point=[-3, 1, 0])
        referential = VGroup(xaxis, yaxis, x_label, y_label)
        referential.move_to(dref)
        referential.rotate(np.atan(2/5))
        self.add(referential)

        self.play(referential.animate(rate_func=ease_in_out_sine).move_to([-0.3, 2, 0]), run_time=2.5)
        self.play(Rotate(referential, -PI/4.2, about_point=ORIGIN),rate_func=ease_in_out_sine, run_time = 2)
        self.play(referential.animate(rate_func=ease_in_out_sine).move_to([3.5, 0.7, 0]), run_time=2.5)
        self.wait(1)

class MovingReferential2(Scene):
    def construct(self):
        #plane = NumberPlane()
        #self.add(plane)
        bloc1 = Square(side_length=0.75, color=BLACK)
        bloc2 = Square(side_length=0.75, color=BLACK)
        pulley = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1)

        bloc1.move_to([-0.5, -2, 0])
        bloc2.move_to([0.5, -1, 0])

        pulley.move_to([0, 2, 0])
        self.add(bloc1, bloc2)

        p1 = bloc1.get_corner(UP)
        rope1 = Line(p1, [-0.5, 2, 0], color=BLACK)
        d1 = Dot(point=p1).set_color(BLUE)
        p2 = bloc2.get_corner(UP)
        rope2 = Line([0.5, 2, 0], p2, color=BLACK)
        d2 = Dot(point=p2).set_color(RED)

        self.add(rope1, rope2, pulley, d1, d2)

        yaxis = Arrow(start=ORIGIN, end=[0, 1, 0], buff=0, color=BLACK)
        yaxis.move_to([-1, 0, 0])
        y_label = Text("y", color=BLACK)
        y_label.scale(0.65)
        y_label.move_to([-1.25, 0.5 , 0])
        referential = VGroup( yaxis, y_label)
        self.add(referential)
        self.play(referential.animate(rate_func=ease_in_out_sine).move_to([-1.125, 2,0]), run_time=2.5)
        self.play(Rotate(referential, -PI, about_point=[0, 2, 0]),rate_func=ease_in_out_sine, run_time = 2)
        self.play(referential.animate(rate_func=ease_in_out_sine).move_to([1.125, 0,0]), run_time=2.5)
        self.wait(1)

class MovingReferential3(Scene):
    def construct(self):
        #plane = NumberPlane()
        #self.add(plane)
        bloc1 = Square(side_length=1, color=BLACK)
        bloc2 = Square(side_length=1, color=BLACK)
        floor = Line([-5, 0, 0], [2, 0, 0], color=BLACK)
        pulley = Circle(radius=0.5, fill_color=WHITE, fill_opacity=1)

        bloc1.move_to([-3, 0.5, 0])
        bloc2.move_to([2.5, -2, 0])

        pulley.move_to([2, 0, 0])
        self.add(bloc1, bloc2, floor)

        p1 = bloc1.get_corner(RIGHT)
        rope1 = Line(p1, [2, 0.5, 0], color=BLACK)
        d1 = Dot(point=p1).set_color(BLUE)
        p2 = bloc2.get_corner(UP)
        rope2 = Line([2.5, 0, 0], p2, color=BLACK)
        d2 = Dot(point=p2).set_color(RED)

        self.add(rope1, rope2, pulley, d1, d2)


        xaxis = Arrow(start=ORIGIN, end=RIGHT, buff=0, color=BLACK)
        x_label = Text("x", color=BLACK)
        x_label.scale(0.65)
        x_label.move_to([0.85, -0.35, 0])

        yaxis = Arrow(start=ORIGIN, end=[0, 1, 0], buff=0, color=BLACK)
        y_label = Text("y", color=BLACK)
        y_label.scale(0.65)
        y_label.move_to([-0.35, 0.85, 0])
        referential = VGroup(xaxis, yaxis, x_label, y_label)
        self.add(referential)
        referential.move_to([-1 ,1.4, 0])
        self.play(referential.animate(rate_func=ease_in_out_sine).move_to([2, 1.4,0]), run_time=2.5)
        self.play(Rotate(referential, -PI/2, about_point=[2, 0, 0]),rate_func=ease_in_out_sine, run_time = 2)
        self.wait(1)