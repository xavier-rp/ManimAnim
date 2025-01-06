from Tools.scripts.texi2html import increment
from manim import *

# manim -qh -p AngularVariables.py AngularVelocity

config.background_color = WHITE

class AngularVelocity(Scene):
    """
    This animation displays a particle going around a circle
    at constant velocity with its velocity and acceleration vectors
    """
    def construct(self):
        circTraj = Circle(radius=3, color=BLACK)
        centerDot = Dot([0,0,0], color=BLACK)

        self.add(circTraj, centerDot)

        radius = Line(start=[0,0,0], end=[3,0,0], color=BLACK)
        dotOuter = Dot([3, 0, 0], color=RED)
        dotInner = Dot([1.5, 0, 0], color=BLUE)
        dotOuter.set_z_index(1)
        dotInner.set_z_index(1)

        theta = 2*PI

        innerArc = Arc(radius=1.5, angle=theta, color=GREEN)
        outerArc = Arc(radius=3, angle=theta, color=GREEN)
        xAxis = DashedLine([0,0,0], [3, 0, 0], color=BLACK)

        self.add(xAxis, radius, dotOuter, dotInner)

        self.play(AnimationGroup(Create(innerArc, rate_func=linear),
                                 Create(outerArc, rate_func=linear),
                                 Rotate(radius, angle=theta, about_point=ORIGIN, rate_func=linear),
                                 Rotate(dotInner, angle=theta, about_point=ORIGIN, rate_func=linear),
                                 Rotate(dotOuter, angle=theta, about_point=ORIGIN, rate_func=linear), run_time=6))


        outerArc2 = outerArc.copy()
        outerArc2.color = RED
        innerArc2 = innerArc.copy()
        innerArc2.color = BLUE
        self.play(AnimationGroup(Create(outerArc2), Create(innerArc2)))
        self.play(Uncreate(dotInner), Uncreate(dotOuter), Uncreate(xAxis), Uncreate(radius), Uncreate(centerDot))

        innerCirc = Circle(1.5, color=BLUE)
        outerCirc = Circle(3, color=RED)
        self.add(innerCirc, outerCirc)
        self.remove(innerArc, innerArc2, outerArc, outerArc2, circTraj)

        innerLine = Line([-PI*1.5, 1, 0], [PI*1.5,1,0], color=BLUE)
        outerLine = Line([-PI*3, 0, 0], [PI*3, 0, 0], color=RED)

        self.play(Transform(innerCirc, innerLine), Transform(outerCirc, outerLine))

        self.wait()