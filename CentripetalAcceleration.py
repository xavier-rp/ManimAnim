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

        speedVector = Arrow(start=[2, 0, 0], end=[2, 1, 0], buff=0)
        accVector = Arrow(start=[2, 0, 0], end=[1.5, 0, 0], buff=0)

        self.add(speedVector, accVector)

        self.wait(0.5)

        self.play(AnimationGroup(Rotate(speedVector, 2*PI, about_point=ORIGIN, rate_func=linear),
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
        ref_begin = [2, 0, 0]
        speedVector = Arrow(start=ref_begin, end=[2, 1, 0], buff=0)

        nbSectors = 32
        circTraj = Circle(radius=2)
        speedVector.rotate(PI/nbSectors, about_point=speedVector.get_start())
        speedVector.generate_target()

        self.add(circTraj, speedVector)
        self.wait(0.5)

        for i in range(1, nbSectors + 1):

            #Point on the circle after completing one side of the polygone
            ref_end = 2*np.array([np.cos(i*2*PI/nbSectors), np.sin(i*2*PI/nbSectors), 0])

            line_i = Line(ref_begin, ref_end)

            if i < nbSectors/8:
                newSpeedVector = Arrow(start=ref_end, end=ref_end+np.array(speedVector.get_vector()), buff=0)
                self.play(AnimationGroup(particle.animate(rate_func=linear, run_time=0.2).move_to(ref_end),
                                         Transform(speedVector, newSpeedVector, rate_func=linear, run_time=0.2),
                                         Create(line_i, rate_func=linear, run_time=0.2)))

                v2 = speedVector.copy()
                v2.rotate(angle=2 * PI / nbSectors, about_point=v2.get_start())

                vref = Vector(v2.get_end() - speedVector.get_end())
                accVect1 = Arrow(start=speedVector.get_start(), end=speedVector.get_start() + vref.get_vector(), buff=0)
                accVect2 = Arrow(start=speedVector.get_end(), end=v2.get_end(), buff=0)

                line_to_center = DashedLine(speedVector.get_start(), [0, 0, 0])
                self.play(AnimationGroup(FadeIn(line_to_center), FadeIn(accVect1), run_time=0.5))

                self.play(ReplacementTransform(accVect1, accVect2), run_time = 0.5)
                self.play(Rotate(speedVector, angle=2*PI/nbSectors, about_point=speedVector.get_start()), rate_func=linear, run_time = 0.2)

                self.play(AnimationGroup(FadeOut(accVect2, run_time=0.2), FadeOut(line_to_center, run_time=0.2)))

            else:
                self.remove(speedVector)
                speedVector.rotate(angle=2*PI/nbSectors, about_point=speedVector.get_start())
                self.play(AnimationGroup(particle.animate(rate_func=linear, run_time=0.2).move_to(ref_end),
                                         Create(line_i, rate_func=linear, run_time=0.2)))



            ref_begin = ref_end

        self.wait(0.5)