#!/usr/bin/python
# Copyright (C) 2018 Azhar Ali Khaked here
#
# This program is free software; you can redistribute it
# and/or modify it under the terms of the GNU General
# Public License as published by the Free Software
# Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even
# the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General
# Public License along with this program; if not, write
# to the Free Software Foundation, Inc., 51 Franklin
# St, Fifth Floor, Boston, MA 02110-1301  USA

from gettext import gettext as _
from sugar3.graphics.xocolor import XoColor
from sugar3 import profile
import pygame
import sys
from pygame.locals import *
from random import randint
from gi.repository import Gtk


def randomOperation(maxi):
    x = (randint(0, maxi))
    y = (randint(1, maxi))
    pick = (randint(1, 4))
    if (pick == 1):
        return 1, x + y, x, y
    elif (pick == 2):
        return 2, x * y, x, y
    elif (pick == 3):
        x = x * y
        return 3, x / y, x, y
    elif (pick == 4):
        if (x > y):
            return 4, x - y, x, y
        else:
            return 5, y - x, x, y


def displayQuery(pick, x, y):
    if (pick == 1):
        strin = _("Q: %d + %d =") % (x, y)
        texSurfaceObj = fontObj.render(strin, True, WHITE)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, 20)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
    elif (pick == 2):
        strin = _("Q: %d * %d =") % (x, y)
        texSurfaceObj = fontObj.render(strin, True, WHITE)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, 20)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
    elif (pick == 3):
        strin = _("Q: %d / %d =") % (x, y)
        texSurfaceObj = fontObj.render(strin, True, WHITE)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, 20)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
    elif (pick == 4):
        strin = _("Q: %d - %d =") % (x, y)
        texSurfaceObj = fontObj.render(strin, True, WHITE)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, 20)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
    elif (pick == 5):
        strin = _("Q: %d - %d =") % (y, x)
        texSurfaceObj = fontObj.render(strin, True, WHITE)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, 20)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)


def scoreBoard(score, hscore):
    texSurfaceObj = fontObj.render(("Score = %d") % (score), True, WHITE)
    texRectObj = texSurfaceObj.get_rect()
    texRectObj.center = (80, 20)
    DISPLAYSURF.blit(texSurfaceObj, texRectObj)

    texSurfaceObj = fontObj.render(("High Score = %d") % (hscore), True, WHITE)
    texRectObj = texSurfaceObj.get_rect()
    texRectObj.center = (ResX - 120, 20)
    DISPLAYSURF.blit(texSurfaceObj, texRectObj)


def newGameAnimation():

    DISPLAYSURF.fill(GREY)
    texSurfaceObj = megaFont.render(("3"), True, BLACK)
    texRectObj = texSurfaceObj.get_rect()
    texRectObj.center = (ResX / 2, ResY / 2)
    DISPLAYSURF.blit(texSurfaceObj, texRectObj)
    pygame.display.update()
    pygame.time.wait(1000)
    DISPLAYSURF.fill(GREY)
    texSurfaceObj = megaFont.render(("2"), True, BLACK)
    texRectObj = texSurfaceObj.get_rect()
    texRectObj.center = (ResX / 2, ResY / 2)
    DISPLAYSURF.blit(texSurfaceObj, texRectObj)
    pygame.display.update()
    pygame.time.wait(1000)
    DISPLAYSURF.fill(GREY)
    texSurfaceObj = megaFont.render(("1"), True, BLACK)
    texRectObj = texSurfaceObj.get_rect()
    texRectObj.center = (ResX / 2, ResY / 2)
    DISPLAYSURF.blit(texSurfaceObj, texRectObj)
    pygame.display.update()
    pygame.time.wait(1000)
    DISPLAYSURF.fill(GREY)
    texSurfaceObj = megaFont.render("GO!", True, BLACK)
    texRectObj = texSurfaceObj.get_rect()
    texRectObj.center = (ResX / 2, ResY / 2)
    DISPLAYSURF.blit(texSurfaceObj, texRectObj)
    pygame.display.update()
    pygame.time.wait(1500)


def ggAnimation(score, hscore):
    flicker = 0
    while True:
        flicker += 1
        DISPLAYSURF.fill(GREY)
        texSurfaceObj = megaFont.render(_("GAME OVER!"), True, RED)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, ResY / 2)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        texSurfaceObj = megaFont.render(
            _("You Scored = %d") %
            (score), True, BLACK)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, ResY / 2 + 90)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        texSurfaceObj = fontObj.render(
            _("High Score = %d") %
            (hscore), True, BLACK)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, ResY / 2 + 180)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        if(flicker < 15):
            texSurfaceObj = fontObj.render(
                _("Press any key to continue"), True, BLACK)
            texRectObj = texSurfaceObj.get_rect()
            texRectObj.center = (ResX / 2, 20)
            DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        if(flicker == 30):
            flicker = 0
        while Gtk.events_pending():
            Gtk.main_iteration()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                return ()
        pygame.display.update()
        fpsClock.tick(FPS)


def startAnimation():
    flicker = 0
    while True:
        flicker += 1
        DISPLAYSURF.fill(WHITE)
        texSurfaceObj = megaFont.render(_("Number Rush!"), True, BLACK)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, ResY / 2)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        texSurfaceObj = fontObj.render(
            _("Use arrow left-right OR A and D keys to move box"), True, BLACK)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX / 2, ResY / 2 + 180)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        if(flicker < 15):
            texSurfaceObj = fontObj.render(
                _("Press any key to continue"), True, BLACK)
            texRectObj = texSurfaceObj.get_rect()
            texRectObj.center = (ResX / 2, 20)
            DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        if(flicker == 30):
            flicker = 0
        while Gtk.events_pending():
            Gtk.main_iteration()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                return ()
        pygame.display.update()
        fpsClock.tick(FPS)


def main():

    pygame.init()

    game = numrush()

    game.run()


class numrush():

    def __init__(self):
        pass

    def run(self):
        global DISPLAYSURF, WHITE, BLACK, BLUE, GREEN, PURPLE, RED, GREY, fontObj, megaFont, ResX, ResY, FPS, fpsClock
        score = 0
        hscore = 0
        infoObject = pygame.display.Info()

        FPS = 30
        fpsClock = pygame.time.Clock()
        ResX = infoObject.current_w
        ResY = infoObject.current_h
        DISPLAYSURF = pygame.display.set_mode((ResX, ResY), 0, 32)
        pygame.display.set_caption(('Number Rush'))

        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREY = (200, 200, 200)
        PURPLE = (100, 0, 100)
        RED = (255, 0, 0)
        GREEN = (200, 200, 0)
        BLUE = (0, 0, 255)

        LEFT = 'left'
        RIGHT = 'right'

        foodx = 0
        foody = 100
        food = 4
        speed = ResY / 320
        speedinc = 1

        gap = (ResX) / (food + 1)
        direction = 'down'
        maxi = 10
        boxx = gap
        boxy = ResY - 40

        selection, n, x, y = randomOperation(maxi)
        if (n < 3):
            a = n + (1)
            b = n + (2)
            c = n + (3)
        else:
            a = n + (1) * (-1)**randint(1, 2)
            b = n + (2) * (-1)**randint(1, 2)
            c = n + (3) * (-1)**randint(1, 2)

        randomOptions = [a, b, c]

        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        megaFont = pygame.font.Font('freesansbold.ttf', 70)

        counter = 0
        rand = randint(1, 4)
        startAnimation()
        newGameAnimation()
        while True:
            DISPLAYSURF.fill(GREY)
            pygame.draw.rect(DISPLAYSURF, PURPLE, (0, 0, ResX, 50))
            pygame.draw.rect(DISPLAYSURF, PURPLE, (0, 0, 100, ResY))
            pygame.draw.rect(DISPLAYSURF, PURPLE, (ResX - 100, 0, ResX, ResY))

            displayQuery(selection, x, y)

            for i in range(4):
                if(i + 1 == rand):
                    texSurfaceObj = fontObj.render(str(n), True, BLACK)
                    texRectObj = texSurfaceObj.get_rect()
                    pygame.draw.circle(DISPLAYSURF, GREEN,
                                       (foodx + (i + 1) * gap, foody), 40, 0)
                    texRectObj.center = (foodx + (i + 1) * gap, foody + 3)
                    DISPLAYSURF.blit(texSurfaceObj, texRectObj)
                else:
                    texSurfaceObj = fontObj.render(
                        str(randomOptions[counter]), True, BLACK)
                    counter += 1
                    texRectObj = texSurfaceObj.get_rect()
                    pygame.draw.circle(DISPLAYSURF, GREEN,
                                       (foodx + (i + 1) * gap, foody), 40, 0)
                    texRectObj.center = (foodx + (i + 1) * gap, foody + 3)
                    DISPLAYSURF.blit(texSurfaceObj, texRectObj)
            counter = 0
            pygame.draw.rect(
                DISPLAYSURF, BLUE, (boxx - 40, boxy, boxx - boxx + 80, boxy))

            scoreBoard(score, hscore)

            foody += speed

            if (score == 10 * speedinc):
                speed += 2
                speedinc += 1

            if foody > ResY - 1:
                if(foodx + (rand) * gap == boxx):
                    score += 1

                else:
                    if(score > hscore):
                        hscore = score
                    ggAnimation(score, hscore)
                    newGameAnimation()
                    score = 0
                    speed = ResY / 320
                    speedinc = 1

                foody = 100
                selection, n, x, y = randomOperation(maxi)
                rand = randint(1, 4)
                if (n < 3):
                    a = n + (1)
                    b = n + (2)
                    c = n + (3)
                else:
                    a = n + (1) * (-1)**randint(1, 2)
                    b = n + (2) * (-1)**randint(1, 2)
                    c = n + (3) * (-1)**randint(1, 2)

                randomOptions = [a, b, c]
                counter = 0

            while Gtk.events_pending():
                Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if (event.key == K_LEFT or event.key == K_a):
                        if(boxx > gap):
                            boxx -= gap
                    elif (event.key == K_RIGHT or event.key == K_d):
                        if(boxx < ResX - gap):
                            boxx += gap

            pygame.display.update()
            fpsClock.tick(FPS)


if __name__ == '__main__':
    main()
