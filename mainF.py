# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 22:51:43 2021

@author: priyanshu-lanjewar
"""

import json
import urllib.request
import turtle
screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-190, -90, 190, 90)
screen.bgpic('wmpgif.gif')
screen.title("ISS Tracker - PWL ")
screen.register_shape("issgif.gif")
iss  = turtle.Turtle()
iss.shape("issgif.gif")
iss.setheading(45)
iss.penup()

while True:
    url = "http://api.open-notify.org/iss-now.json"
    resp = urllib.request.urlopen(url)
    result = json.loads(resp.read())
    location =result["iss_position"]
    latitude = location['latitude']
    longitude = location['longitude']
    latitude = float(latitude)
    longitude = float(longitude)
    iss.goto(longitude,latitude)