import glm
import pygame as pg
import numpy as np
from scipy.spatial.transform import Rotation

FOV = 50 # deg
NEAR = 0.1
FAR = 100
SPEED = 0.01

class Camera:
    def __init__(self, app) -> None:
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        
        self.position = glm.vec3(0, 0, 5)
        

        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.lookat = self.position + self.forward

        self.m_view = self.get_view_matrix()
        self.m_proj = self.get_projection_matrix()


    def update(self):
        self.move()
        self.m_view = self.get_view_matrix()

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_SPACE]:
            self.position += self.up * velocity
        if keys[pg.K_LSHIFT]:
            self.position -= self.up * velocity
        
        x, y = pg.mouse.get_pos()
        x, y = x - self.app.WIN_SIZE[0]/2, -y + self.app.WIN_SIZE[1]/2
        x, y = (x/(self.app.WIN_SIZE[0]/2), y/(self.app.WIN_SIZE[1]/2))
        x, y = x * 0.5, y * 0.5
        self.lookat = self.position + glm.vec3(*Rotation.from_euler("xyz", (-y, x, 0)).apply(self.forward))
        ""

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.lookat, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)