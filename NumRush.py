#!/usr/bin/python3
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

import logging
import os
from gettext import gettext as _
from sugar3.graphics.xocolor import XoColor
from sugar3 import profile
import pygame
import sys
from pygame.locals import *
from random import randint
from gi.repository import Gtk
import locale
from sugar3.activity.activity import get_activity_root


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
        return 3, x // y, x, y
    elif (pick == 4):
        if (x > y):
            return 4, x - y, x, y
        else:
            return 5, y - x, x, y


def display(strin, X, Y):
    texSurfaceObj = fontObj.render(strin, True, WHITE)
    texRectObj = texSurfaceObj.get_rect()
    texRectObj.center = (X, Y)
    DISPLAYSURF.blit(texSurfaceObj, texRectObj)


def selectQuery(pick, x, y):
    if (pick == 1):
        strin = _("Q: %d + %d =") % (x, y)
        display(strin, ResX // 2, 20)

    elif (pick == 2):
        strin = _("Q: %d * %d =") % (x, y)
        display(strin, ResX // 2, 20)
    elif (pick == 3):
        strin = _("Q: %d / %d =") % (x, y)
        display(strin, ResX // 2, 20)
    elif (pick == 4):
        strin = _("Q: %d - %d =") % (x, y)
        display(strin, ResX // 2, 20)
    elif (pick == 5):
        strin = _("Q: %d - %d =") % (y, x)
        display(strin, ResX // 2, 20)
    return strin


def scoreBoard(score, hscore):
    display(_("Score = %d") % (score), 80, 20)
    display(_("High Score = %d") % (hscore), ResX - 120, 20)


def newGameAnimation(mainGame):

    text = ['3', '2', '1', 'GO!']

    for i in text:

        if mainGame.running == False:
            return

        DISPLAYSURF.fill(GREY)
        texSurfaceObj = megaFont.render((i), True, BLACK)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX // 2, ResY // 2)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)

        start = pygame.time.get_ticks()

        while mainGame.running:
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            if pygame.time.get_ticks() - start > 1000:
                break

            pygame.display.update()
            fpsClock.tick(FPS)


def ggAnimation(score, hscore, mainGame):
    flicker = 0
    while mainGame.running:
        flicker += 1
        DISPLAYSURF.fill(LightColor)
        texSurfaceObj = megaFont.render(_("GAME OVER!"), True, DarkColor)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX // 2, ResY // 2)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        texSurfaceObj = megaFont.render(
            _("You Scored = %d") %
            (score), True, BLACK)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX // 2, ResY // 2 + 90)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        texSurfaceObj = fontObj.render(
            _("High Score = %d") %
            (hscore), True, BLACK)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX // 2, ResY // 2 + 180)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        if(flicker < 15):
            texSurfaceObj = fontObj.render(
                _("Press any key to continue"), True, BLACK)
            texRectObj = texSurfaceObj.get_rect()
            texRectObj.center = (ResX // 2, 20)
            DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        if(flicker == 30):
            flicker = 0
        while Gtk.events_pending():
            Gtk.main_iteration()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                return ()

        if mainGame.running == False:
            return

        pygame.display.update()
        fpsClock.tick(FPS)


def startAnimation(mainGame):
    flicker = 0
    while mainGame.running:
        flicker += 1
        DISPLAYSURF.fill(LightColor)
        texSurfaceObj = megaFont.render(("Number Rush!"), True, DarkColor)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX // 2, ResY // 2)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        texSurfaceObj = fontObj.render(
            _("Use arrow left-right OR A and D keys to move box"), True, BLACK)
        texRectObj = texSurfaceObj.get_rect()
        texRectObj.center = (ResX // 2, ResY // 2 + 180)
        DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        if(flicker < 15):
            texSurfaceObj = fontObj.render(
                _("Press any key to continue"), True, BLACK)
            texRectObj = texSurfaceObj.get_rect()
            texRectObj.center = (ResX // 2, 20)
            DISPLAYSURF.blit(texSurfaceObj, texRectObj)
        if(flicker == 30):
            flicker = 0
        while Gtk.events_pending():
            Gtk.main_iteration()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                return ()

        if mainGame.running == False:
            return
        pygame.display.update()
        fpsClock.tick(FPS)


def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def main():

    pygame.init()

    game = numrush()

    game.run()


class numrush():

    def __init__(self):
        self.resume_game_flag = None

    def run(self):

        global XO1, XO2, DISPLAYSURF, WHITE, BLACK, DarkColor, LightColor, DarkColor, RED, GREY, fontObj, megaFont, ResX, ResY, FPS, fpsClock
        XO1, XO2 = profile.get_color().to_string().split(',')

        if not self.resume_game_flag:
            self.randomOptions = []
            self.n = -1
            self.strin = ''
            self.hscore = self.load_highscore()
            self.score = 0

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
        DarkColor = hex_to_rgb(XO1)
        RED = (255, 0, 0)
        LightColor = hex_to_rgb(XO2)
        DarkColor = hex_to_rgb(XO1)

        LEFT = 'left'
        RIGHT = 'right'

        foodx = 0
        foody = 100
        food = 4
        speed = ResY // 320
        speedinc = 1

        gap = (ResX) // (food + 1)
        direction = 'down'
        maxi = 10
        boxx = gap
        boxy = ResY - 40

        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        megaFont = pygame.font.Font('freesansbold.ttf', 70)

        self.running = True

        counter = 0
        rand = randint(1, 4)

        if not self.resume_game_flag:
            selection, self.n, x, y, self.randomOptions = self.answer_options(
                maxi)
            startAnimation(self)
            newGameAnimation(self)

        while self.running:
            DISPLAYSURF.fill(GREY)
            pygame.draw.rect(DISPLAYSURF, DarkColor, (0, 0, ResX, 50))
            pygame.draw.rect(DISPLAYSURF, DarkColor, (0, 0, 100, ResY))
            pygame.draw.rect(DISPLAYSURF, DarkColor,
                             (ResX - 100, 0, ResX, ResY))

            if self.resume_game_flag:
                display(self.strin, ResX // 2, 20)

            if not self.resume_game_flag:
                self.strin = selectQuery(selection, x, y)

            for i in range(4):
                if(i + 1 == rand):
                    texSurfaceObj = fontObj.render(str(self.n), True, BLACK)
                    texRectObj = texSurfaceObj.get_rect()
                    pygame.draw.circle(DISPLAYSURF, LightColor,
                                       (foodx + (i + 1) * gap, foody), 40, 0)
                    texRectObj.center = (foodx + (i + 1) * gap, foody + 3)
                    DISPLAYSURF.blit(texSurfaceObj, texRectObj)
                else:
                    texSurfaceObj = fontObj.render(
                        str(self.randomOptions[counter]), True, BLACK)
                    counter += 1
                    texRectObj = texSurfaceObj.get_rect()
                    pygame.draw.circle(DISPLAYSURF, LightColor,
                                       (foodx + (i + 1) * gap, foody), 40, 0)
                    texRectObj.center = (foodx + (i + 1) * gap, foody + 3)
                    DISPLAYSURF.blit(texSurfaceObj, texRectObj)
            counter = 0
            pygame.draw.rect(
                DISPLAYSURF, DarkColor, (boxx - 40, boxy, boxx - boxx + 80, boxy))

            scoreBoard(self.score, self.hscore)
            self.save_highscore()
            foody += speed

            if self.score == 5 * speedinc:
                speed += 1
                speedinc += 1

            if foody > ResY - 1:
                if(foodx + (rand) * gap == boxx):
                    self.score += 1

                else:
                    if(self.score > self.hscore):
                        self.hscore = self.score
                    ggAnimation(self.score, self.hscore, self)
                    newGameAnimation(self)
                    self.score = 0
                    speed = ResY // 320
                    speedinc = 1

                if self.resume_game_flag:
                    self.resume_game_flag = False

                foody = 100
                selection, self.n, x, y, self.randomOptions = self.answer_options(
                    maxi)
                self.strin = selectQuery(selection, x, y)
                counter = 0

            while Gtk.events_pending():
                Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if (event.key == K_LEFT or event.key == K_a):
                        if(boxx > gap):
                            boxx -= gap
                    elif (event.key == K_RIGHT or event.key == K_d):
                        if(boxx < ResX - gap):
                            boxx += gap

            if self.running == False:
                return
            pygame.display.update()
            fpsClock.tick(FPS)

    def answer_options(self, maxi):
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
        return selection, n, x, y, randomOptions

    def restore_game(self, high_score=0, current_score=0,
                     answer=0, randOptions=[0, 0, 0], question='0 - 0'):
        ''' Restore a game from the Journal '''
        self.hscore = high_score
        self.score = current_score
        self.n = answer
        self.randomOptions = randOptions
        self.strin = question
        self.restore_cb()

    def restore_cb(self):
        self.resume_game_flag = True

    def save_game(self):
        ''' Return game state for saving to Journal '''
        return self.hscore, self.score, self.n, self.randomOptions, self.strin

    def read_highscore(self):
        highscore = [0]
        file_path = os.path.join(get_activity_root(), 'data', 'highscore')
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as fp:
                    highscore = fp.readlines()
                return int(highscore[0])
            except (ValueError, IndexError) as e:
                logging.exception(e)
                return 0
        return int(highscore[0])

    def save_highscore(self):
        file_path = os.path.join(get_activity_root(), 'data', 'highscore')
        int_highscore = self.read_highscore()
        if not int_highscore > self.score:
            with open(file_path, "w") as fp:
                fp.write(str(self.score))

    def load_highscore(self):
        highscore = self.read_highscore()
        return highscore



if __name__ == '__main__':
    main()
