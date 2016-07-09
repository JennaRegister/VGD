import pygame
import math, random


class Puck:

    __X_AXIS = pygame.math.Vector2(1,0)
    __Y_AXIS = pygame.math.Vector2(0,1)

    def __init__(self, xy, velocity, color, radius, mass=1.0):
        self.pos = pygame.math.Vector2(*xy)
        self.vel = pygame.math.Vector2(*velocity)
        self.col = color
        self.rad = radius
        self.m = mass

    def add_force(self, f):
        # f = m*a
        acceleration = f / self.m
        # note: not synchronized!
        self.vel += acceleration

    def draw(self, surf):
        pygame.draw.circle(surf, self.col, [int(p) for p in self.pos], self.rad)

    def contain(self, rect, bounce=1.0, drift=None):
        # a collision is handled in the following way:
        # 1. backtrack 'out' of the wall to where it is flush. This is done along the -velocity vector
        # 2. flip the velocity perpendicular to the wall and scale it by 'bounce'
        # 3. play forward the time we lost backtracking

        # LEFT
        if self.pos[0] - self.rad < rect[0]:
            # get depth into wall
            depth_x = rect[0] - (self.pos[0] - self.rad)
            # amount of "rewind" time is fraction of the last time step spent "in" the wall
            rewind_t = abs(float(depth_x) / self.vel[0])
            # backtrack
            self.pos -= self.vel * rewind_t
            # bounce x velocity
            self.vel[0] *= -bounce
            if drift: self.vel += drift*rewind_t
            # play it forward
            self.pos += self.vel * rewind_t
        # RIGHT
        elif self.pos[0] + self.rad > rect[0] + rect[2]:
            # get depth into wall
            depth_x =  self.pos[0] + self.rad - (rect[0] + rect[2])
            # amount of "rewind" time is fraction of the last time step spent "in" the wall
            rewind_t = abs(float(depth_x) / self.vel[0])
            # backtrack
            self.pos -= self.vel * rewind_t
            # bounce x velocity
            self.vel[0] *= -bounce
            if drift: self.vel += drift*rewind_t
            # play it forward
            self.pos += self.vel * rewind_t

        # TOP
        if self.pos[1] - self.rad < rect[1]:
            # get depth into wall
            depth_y = rect[1] - (self.pos[1] - self.rad)
            # amount of "rewind" time is fraction of the last time step spent "in" the wall
            rewind_t = abs(float(depth_y) / self.vel[1])
            # backtrack
            self.pos -= self.vel * rewind_t
            # bounce x velocity
            self.vel[1] *= -bounce
            if drift: self.vel += drift*rewind_t
            # play it forward
            self.pos += self.vel * rewind_t
        # BOTTOM
        elif self.pos[1] + self.rad > rect[1] + rect[3]:
            # get depth into wall
            depth_y =  self.pos[1] + self.rad - (rect[1] + rect[3])
            # amount of "rewind" time is fraction of the last time step spent "in" the wall
            rewind_t = abs(float(depth_y) / self.vel[1])
            # backtrack
            self.pos -= self.vel * rewind_t
            # bounce x velocity
            self.vel[1] *= -bounce
            if drift: self.vel += drift*rewind_t
            # play it forward
            self.pos += self.vel * rewind_t

    def move(self):
        self.pos += self.vel

    def get_rect(self):
        return pygame.Rect(self.pos[0]-self.rad, self.pos[1]-self.rad, 2*self.rad, 2*self.rad)

    def is_colliding(self, other):
        if isinstance(other, Puck):
            diff = other.pos - self.pos
            if diff.length() < self.rad + other.rad:
                return True
        return False

    def ricochet(self, other, elasticity=1.0):
        if self.is_colliding(other):
            total_mass = self.m + other.m

            # MOVE THEM SO THEY'RE NO LONGER OVERLAPPING
            diff = other.pos - self.pos
            overlap = (other.rad + self.rad) - diff.length()
            separation_vector = diff.normalize() * overlap

            other.pos += self.m * separation_vector / total_mass
            self.pos  -= other.m * separation_vector / total_mass

            # COMPUTE NEW VELOCITIES
            angle_to_x_axis = diff.angle_to(Puck.__X_AXIS)
            rotated_self_vel = self.vel.rotate(angle_to_x_axis)
            rotated_other_vel = other.vel.rotate(angle_to_x_axis)
            # we've rotated everything so that the direction self-->other is on the x' axis,
            # so now we only need to do the bouncing on that direction
            total_momentum_x = self.m * rotated_self_vel[0] + other.m * rotated_other_vel[0]

            # 'px' refers to momentum. momentum is velocity * mass
            # new self momentum = total momentum + elasticity * relative momentum of other object
            # new other momentum = total momentum + elasticity * relative momentum of self
            new_self_rotated_px = total_momentum_x + elasticity * other.m * (rotated_other_vel[0] - rotated_self_vel[0])
            new_other_rotated_px = total_momentum_x + elasticity * self.m * (rotated_self_vel[0] - rotated_other_vel[0])

            # convert from momentum back to velocity
            rotated_self_vel[0] = new_self_rotated_px / total_mass
            rotated_other_vel[0] = new_other_rotated_px / total_mass

            # rotate coordinates back - now we know the new velocities!
            self.vel = rotated_self_vel.rotate(-angle_to_x_axis)
            other.vel = rotated_other_vel.rotate(-angle_to_x_axis)

class PuckSet(object):

    def __init__(self):
        self.pucks = []
        self.accel = None

    def add(self, b):
        self.pucks.append(b)

    def update_all(self, bounciness=1.0, container=None, container_bounciness=1.0):
        for i in range(len(self.pucks)):
            for j in range(i+1, len(self.pucks)):
                self.pucks[i].ricochet(self.pucks[j], bounciness)

        for b in self.pucks:
            if container is not None:
                b.contain(container, container_bounciness, drift=self.accel)
            b.move()

    def draw_all(self, surf):
        for b in self.pucks:
            b.draw(surf)

    def drift(self, acceleration):
        for puck in self.pucks:
            puck.vel += acceleration
        self.accel = acceleration

    def friction(self, strength=0.98):
        for puck in self.pucks:
            puck.vel *= strength