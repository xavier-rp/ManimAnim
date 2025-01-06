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



class AngularVelocity2(Scene):
    """
    This animation displays a particle following a trajectory shaped as a regular polygone since it's reflected
    each time it collides with the boundary. The animation shows how the orientation of the velocity vector is modified
    at each collision by a pseudo-(instaneous acceleration) vector.

    The number of sides of the polygone can be increased. At higher values, we start to see that the velocity vector
    is closer to the tangent of the circle.
    """
    def construct(self):
        #plane = NumberPlane()
        #self.add(plane)
        particle = Dot([2,0,0], color=RED)
        particle.set_z_index(1)
        #Point of reference when we begin a segment of the trajectory (a side of the polygone)
        ref_begin = [2, 0, 0]
        velocityVector = Arrow(start=ref_begin, end=[2, 1, 0], buff=0, color=BLACK)

        #Chooses the number of sides of the polygone
        nbSides = 8
        circTraj = DashedVMobject(Circle(radius=2, color=BLACK), num_dashes=120)


        #Rotates the velocity vector so it matches the direction of the first segment.
        velocityVector.rotate(PI/nbSides, about_point=velocityVector.get_start())
        velocityVector.generate_target()

        self.add(circTraj, velocityVector, particle)
        self.wait(0.5)

        for i in range(1, nbSides + 1):

            #End position of the current side of the polygone being completed
            ref_end = 2*np.array([np.cos(i*2*PI/nbSides), np.sin(i*2*PI/nbSides), 0])

            currentSide = Line(ref_begin, ref_end, color=GRAY)

            #We only want to display the modification of the orientation of the velocity vector a few times
            if i < nbSides/2:

                velocityVectorAtEnd = Arrow(start=ref_end, end=ref_end+np.array(velocityVector.get_vector()), buff=0, color=BLACK)
                self.play(AnimationGroup(Transform(velocityVector, velocityVectorAtEnd, rate_func=linear, run_time=0.2),
                                         Create(currentSide, rate_func=linear, run_time=0.2),
                                        particle.animate(rate_func=linear, run_time=0.2).move_to(ref_end)))

                #This object is used to determine the acceleration vector. "velocityVector" is now actually the same
                #as velocityVectorAtEnd because of how the "Transform" animation works currently
                velocityAfterCollision = velocityVector.copy()
                velocityAfterCollision.rotate(angle=2 * PI / nbSides, about_point=velocityAfterCollision.get_start())

                #This object represents an actual vector in cartesian notation. It represents the vector that we have
                #to add to velocityVectorAtEnd to obtain the velocity after the collision
                vref = Vector(velocityAfterCollision.get_end() - velocityVector.get_end())

                #Builds the acceleration vector that will be displayed on the particle
                accVect1 = Arrow(start=velocityVector.get_start(), end=velocityVector.get_start() + vref.get_vector(), buff=0, color=BLUE)

                #Builds the acceleration vector that will be displayed at the tip of the velocity vector
                accVect2 = Arrow(start=velocityVector.get_end(), end=velocityAfterCollision.get_end(), buff=0, color=BLUE)

                line_to_center = DashedLine(velocityVector.get_start(), [0, 0, 0], color=BLACK)
                self.play(AnimationGroup(FadeIn(line_to_center), FadeIn(accVect1), run_time=0.5))

                self.play(ReplacementTransform(accVect1, accVect2), run_time = 0.5)
                self.play(Rotate(velocityVector, angle=2*PI/nbSides, about_point=velocityVector.get_start()), rate_func=linear, run_time = 0.2)

                self.play(AnimationGroup(FadeOut(accVect2, run_time=0.2), FadeOut(line_to_center, run_time=0.2)))

            else:
                #Rest of the animation where the particle moves at constant velocity around the trajectory
                self.remove(velocityVector)
                #velocityVector.rotate(angle=2*PI/nbSides, about_point=velocityVector.get_start())
                self.play(AnimationGroup(particle.animate(rate_func=linear, run_time=0.2).move_to(ref_end),
                                         Create(currentSide, rate_func=linear, run_time=0.2)))



            ref_begin = ref_end

        self.wait(0.5)