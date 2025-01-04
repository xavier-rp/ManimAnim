from manim import *

# manim -qh -p CentripetalAcceleration.py CentripetalAcceleration

class CentripetalAcceleration(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        circTraj = Circle(radius=2)
        particle = Dot([2,0,0])

        self.add(circTraj, particle)

        xaxis = Arrow(start=ORIGIN, end=UP, buff=0)
        xaxis.move_to([2, 0.5, 0])
        self.add(xaxis)

        self.play(AnimationGroup(Rotate(xaxis, 2*PI, about_point=ORIGIN), Rotate(particle, 2*PI, about_point=ORIGIN)))

class CentripetalAcceleration2(Scene):
    def construct(self):
        #plane = NumberPlane()
        #self.add(plane)
        particle = Dot([2,0,0])
        self.add(particle)
        ref_begin = [2, 0, 0]
        speedVector = Arrow(start=ref_begin, end=[2, 1, 0], buff=0)

        nbSectors = 20
        circTraj = Circle(radius=2)
        speedVector.rotate(PI/nbSectors, about_point=speedVector.get_start())

        self.add(speedVector, circTraj)
        for i in range(1, nbSectors + 1):
            if i > 1 and i < nbSectors/4 + 1:
                self.play(FadeOut(accVect), run_time=0.1)

            ref_end = 2*np.array([np.cos(i*2*PI/nbSectors), np.sin(i*2*PI/nbSectors), 0])

            line_i = Line(ref_begin, ref_end)



            if i < nbSectors/4:
                self.play(AnimationGroup(particle.animate(rate_func=linear, run_time=0.2).move_to(ref_end),
                                         speedVector.animate(rate_func=linear, run_time=0.2).move_to(
                                             ref_end + 0.5 * np.array(speedVector.get_end() - speedVector.get_start())),
                                         Create(line_i, rate_func=linear, run_time=0.2)))
                self.play(Rotate(speedVector, angle=2*PI/nbSectors, about_point=speedVector.get_start()), rate_func=linear, run_time = 0.2)
                v2 = speedVector.copy()
                v2.rotate(angle=2 * PI / nbSectors, about_point=v2.get_start())
                accVect = Arrow(start=speedVector.get_end(), end=v2.get_end(), buff=0)

                self.play(FadeIn(accVect), run_time=0.2)

            else:
                self.remove(speedVector)
                speedVector.rotate(angle=2*PI/nbSectors, about_point=speedVector.get_start())
                self.play(AnimationGroup(particle.animate(rate_func=linear, run_time=0.2).move_to(ref_end),
                                         Create(line_i, rate_func=linear, run_time=0.2)))



            ref_begin = ref_end

