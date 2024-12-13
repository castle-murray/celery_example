from django.shortcuts import render, redirect
from datetime import datetime
import asyncio
import time
import os
from django.contrib import messages
import platform
from django.core.mail import send_mail

tickCount = 0

def homepage(request):
    return render(request, 'homepage.html')

def sendMsg(subject, msg):
    if platform.system() != 'Windows':
        ret = send_mail(
            subject, msg,
            "dynreports@appsbyjake.com",
            ["jakebgeller@gmail.com"],
            fail_silently=False,
        )
    else:
        print(subject, msg)

def tick():
    global tickCount
    tickCount += 1
    sendMsg("Example Tick - " + str(tickCount) + ", " + str(datetime.now()),"Hello from Example Tick")

def startNOHUPCode():
    sendMsg("Starting NOHUP Loop " + str(datetime.now()), "Looping")
    # while True:
    #     time.sleep(30)  # (3600)
    #     tick()
        # sendMsg("Waking at " + str(datetime.now()), "Waking Up")


def runAPS(request):
    tick()
    return redirect('homepage')

