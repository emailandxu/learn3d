import pygame as pg
import moderngl as mgl
import numpy as np

import sys
from model import Cube
from camera import Camera
from scipy.spatial.transform import Rotation

class Engine:
    def __init__(self, win_size=(1600, 900)) -> None:
        pg.init()
        self.WIN_SIZE = win_size

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        self.ctx.front_face = "ccw"
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        self.camera = Camera(self)

        self.scene = Cube(self)

    def check_events(self):
        def quit():
            self.scene.destory()
            pg.quit()
            sys.exit()

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                quit()
            if event.type == pg.KEYDOWN:
                print(event.key)
                if event.key == pg.K_ESCAPE:
                    quit()

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        self.scene.render()
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)

if __name__ == "__main__":
    engine = Engine()
    engine.run()
