from manim import *

# manim -qh -p CentripetalAcceleration.py CentripetalAcceleration1

class CentripetalAcceleration1(Scene):
    """
    This animation displays a particle going around a circle
    at constant velocity with its velocity and acceleration vectors
    """
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        circTraj = Circle(radius=2)
        particle = Dot([2,0,0])

        self.add(circTraj, particle)

        velocityVector = Arrow(start=[2, 0, 0], end=[2, 1, 0], buff=0)
        accVector = Arrow(start=[2, 0, 0], end=[1.5, 0, 0], buff=0)

        self.add(velocityVector, accVector)

        self.wait(0.5)

        self.play(AnimationGroup(Rotate(velocityVector, 2*PI, about_point=ORIGIN, rate_func=linear),
                                 Rotate(accVector, 2 * PI, about_point=ORIGIN, rate_func=linear),
                                 Rotate(particle, 2 * PI, about_point=ORIGIN, rate_func=linear), run_time=10))

        self.wait(0.5)

class CentripetalAcceleration2(Scene):
    """
    This animation displays a particle following a trajectory shaped as a regular polygone since it's reflected
    each time it collides with the boundary. The animation shows how the orientation of the velocity vector is modified
    at each collision by an pseudo-(instaneous acceleration) vector.

    The number of sides of the polygone can be increased. At higher values, we start to see that the velocity vector
    is closer to the tangent of the circle.
    """
    def construct(self):
        #plane = NumberPlane()
        #self.add(plane)
        particle = Dot([2,0,0])
        self.add(particle)

        #Point of reference when we begin a segment of the trajectory (a side of the polygone)
        ref_begin = [2, 0, 0]
        velocityVector = Arrow(start=ref_begin, end=[2, 1, 0], buff=0)

        #Chooses the number of sides of the polygone
        nbSides = 32
        circTraj = Circle(radius=2)

        #Rotates the velocity vector so it matches the direction of the first segment.
        velocityVector.rotate(PI/nbSides, about_point=velocityVector.get_start())
        velocityVector.generate_target()

        self.add(circTraj, velocityVector)
        self.wait(0.5)

        for i in range(1, nbSides + 1):

            #End position of the current side of the polygone being completed
            ref_end = 2*np.array([np.cos(i*2*PI/nbSides), np.sin(i*2*PI/nbSides), 0])

            currentSide = Line(ref_begin, ref_end)

            #We only want to display the modification of the orientation of the velocity vector a few times
            if i < nbSides/8:

                velocityVectorAtEnd = Arrow(start=ref_end, end=ref_end+np.array(velocityVector.get_vector()), buff=0)
                self.play(AnimationGroup(particle.animate(rate_func=linear, run_time=0.2).move_to(ref_end),
                                         Transform(velocityVector, velocityVectorAtEnd, rate_func=linear, run_time=0.2),
                                         Create(currentSide, rate_func=linear, run_time=0.2)))

                #This object is used to determine the acceleration vector. "velocityVector" is now actually the same
                #as velocityVectorAtEnd because of how the "Transform" animation works currently
                velocityAfterCollision = velocityVector.copy()
                velocityAfterCollision.rotate(angle=2 * PI / nbSides, about_point=velocityAfterCollision.get_start())

                #This object represents an actual vector in cartesian notation. It represents the vector that we have
                #to add to velocityVectorAtEnd to obtain the velocity after the collision
                vref = Vector(velocityAfterCollision.get_end() - velocityVector.get_end())

                #Builds the acceleration vector that will be displayed on the particle
                accVect1 = Arrow(start=velocityVector.get_start(), end=velocityVector.get_start() + vref.get_vector(), buff=0)

                #Builds the acceleration vector that will be displayed at the tip of the velocity vector
                accVect2 = Arrow(start=velocityVector.get_end(), end=velocityAfterCollision.get_end(), buff=0)

                line_to_center = DashedLine(velocityVector.get_start(), [0, 0, 0])
                self.play(AnimationGroup(FadeIn(line_to_center), FadeIn(accVect1), run_time=0.5))

                self.play(ReplacementTransform(accVect1, accVect2), run_time = 0.5)
                self.play(Rotate(velocityVector, angle=2*PI/nbSides, about_point=velocityVector.get_start()), rate_func=linear, run_time = 0.2)

                self.play(AnimationGroup(FadeOut(accVect2, run_time=0.2), FadeOut(line_to_center, run_time=0.2)))

            else:
                #Rest of the animation where the particle moves at constant velocity around the trajectory
                self.remove(velocityVector)
                velocityVector.rotate(angle=2*PI/nbSides, about_point=velocityVector.get_start())
                self.play(AnimationGroup(particle.animate(rate_func=linear, run_time=0.2).move_to(ref_end),
                                         Create(currentSide, rate_func=linear, run_time=0.2)))



            ref_begin = ref_end

        self.wait(0.5)