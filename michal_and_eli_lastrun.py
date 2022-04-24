#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on April 17, 2022, at 20:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'michal_and_eli'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\OneDrive - Open University of Israel\\sofi\\work\\seminar-asi_tal\\michal_eli - final\\michal_and_eli_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
win.mouseVisible = False
agree = visual.ImageStim(
    win=win,
    name='agree', 
    image='intro/Slide1.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
any_key = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='intro/Slide2.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(2,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
any_key_2 = keyboard.Keyboard()

# Initialize components for Routine "imageLoader"
imageLoaderClock = core.Clock()
#image_dict = dict()
image_T=[]
image_N=[]

# Initialize components for Routine "image_list"
image_listClock = core.Clock()

# Initialize components for Routine "Times_list"
Times_listClock = core.Clock()
# Set experiment start values for variable component block_number
block_number = 0
block_numberContainer = []

# Initialize components for Routine "example"
exampleClock = core.Clock()
error_msg=""
good_answer_counter=0
practice_helpL_2 = visual.TextStim(win=win, name='practice_helpL_2',
    text='\u200e\u200fכאשר מופיעה תמונה בצד שמאל\nיש ללחוץ מהר ככל הניתן על המקש \nD\n',
    font='Arial',
    pos=(-0.5, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);
practice_help_R_2 = visual.TextStim(win=win, name='practice_help_R_2',
    text='\u200e\u200fכאשר מופיעה תמונה בצד ימין\nיש ללחוץ מהר ככל הניתן על המקש \nK',
    font='Arial',
    pos=(0.5, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-2.0);
fixation_practice_2 = visual.ShapeStim(
    win=win, name='fixation_practice_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
NN_N_L_p_2 = visual.ImageStim(
    win=win,
    name='NN_N_L_p_2', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5,-0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
NN_L_resp_p_2 = keyboard.Keyboard()
NN_N_R_p_2 = visual.ImageStim(
    win=win,
    name='NN_N_R_p_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, -0.1), size=(0.5,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
NN_R_resp_p_2 = keyboard.Keyboard()

# Initialize components for Routine "example_rest"
example_restClock = core.Clock()
rest_text_3 = visual.TextStim(win=win, name='rest_text_3',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
practice_help_L_rest_2 = visual.TextStim(win=win, name='practice_help_L_rest_2',
    text='\u200e\u200fכאשר מופיעה תמונה בצד שמאל\nיש ללחוץ מהר ככל הניתן על המקש \nD\n',
    font='Arial',
    pos=(-0.5, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);
practice_help_R_rest_2 = visual.TextStim(win=win, name='practice_help_R_rest_2',
    text='\u200e\u200fכאשר מופיעה תמונה בצד ימין\nיש ללחוץ מהר ככל הניתן על המקש \nK',
    font='Arial',
    pos=(0.5, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-2.0);
fixation_practice_3 = visual.ShapeStim(
    win=win, name='fixation_practice_3', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)

# Initialize components for Routine "before_practice"
before_practiceClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='intro/Slide3.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(2,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
any_key_3 = keyboard.Keyboard()

# Initialize components for Routine "Times_list"
Times_listClock = core.Clock()
# Set experiment start values for variable component block_number
block_number = 0
block_numberContainer = []

# Initialize components for Routine "practice"
practiceClock = core.Clock()
error_msg=""
good_answer_counter=0
practice_helpL = visual.TextStim(win=win, name='practice_helpL',
    text='\u200e\u200fכאשר מופיעה תמונה בצד שמאל\nיש ללחוץ מהר ככל הניתן על המקש \nD\n',
    font='Arial',
    pos=(-0.5, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);
practice_help_R = visual.TextStim(win=win, name='practice_help_R',
    text='\u200e\u200fכאשר מופיעה תמונה בצד ימין\nיש ללחוץ מהר ככל הניתן על המקש \nK',
    font='Arial',
    pos=(0.5, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-2.0);
fixation_practice = visual.ShapeStim(
    win=win, name='fixation_practice', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
NN_N_L_p = visual.ImageStim(
    win=win,
    name='NN_N_L_p', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5,-0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
NN_L_resp_p = keyboard.Keyboard()
NN_N_R_p = visual.ImageStim(
    win=win,
    name='NN_N_R_p', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, -0.1), size=(0.5,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
NN_R_resp_p = keyboard.Keyboard()

# Initialize components for Routine "rest_practice"
rest_practiceClock = core.Clock()
rest_text_2 = visual.TextStim(win=win, name='rest_text_2',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
practice_help_L_rest = visual.TextStim(win=win, name='practice_help_L_rest',
    text='\u200e\u200fכאשר מופיעה תמונה בצד שמאל\nיש ללחוץ מהר ככל הניתן על המקש \nD\n',
    font='Arial',
    pos=(-0.5, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);
practice_help_R_rest = visual.TextStim(win=win, name='practice_help_R_rest',
    text='\u200e\u200fכאשר מופיעה תמונה בצד ימין\nיש ללחוץ מהר ככל הניתן על המקש \nK',
    font='Arial',
    pos=(0.5, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-2.0);
fixation_rest_2 = visual.ShapeStim(
    win=win, name='fixation_rest_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)

# Initialize components for Routine "start_trials"
start_trialsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='שלב האימון הסתיים \n\nכעת מתחיל הניסוי',
    font='Open Sans',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);

# Initialize components for Routine "countdown_to_start"
countdown_to_startClock = core.Clock()
count=5
countdown = visual.TextStim(win=win, name='countdown',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Times_list"
Times_listClock = core.Clock()
# Set experiment start values for variable component block_number
block_number = 0
block_numberContainer = []

# Initialize components for Routine "NN"
NNClock = core.Clock()
error_msg=""
fixation_NN = visual.ShapeStim(
    win=win, name='fixation_NN', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
NN_N_L = visual.ImageStim(
    win=win,
    name='NN_N_L', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
NN_L_resp = keyboard.Keyboard()
NN_N_R = visual.ImageStim(
    win=win,
    name='NN_N_R', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
NN_R_resp = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
# Set experiment start values for variable component image_L
image_L = ''
image_LContainer = []
# Set experiment start values for variable component image_R
image_R = ''
image_RContainer = []
# Set experiment start values for variable component Times_L
Times_L = ''
Times_LContainer = []
# Set experiment start values for variable component Times_R
Times_R = ''
Times_RContainer = []
# Set experiment start values for variable component good_answer
good_answer = False
good_answerContainer = []
# Set experiment start values for variable component Routine_type
Routine_type = ""
Routine_typeContainer = []
# Set experiment start values for variable component inbetweenTime
inbetweenTime = 0
inbetweenTimeContainer = []
rest_text = visual.TextStim(win=win, name='rest_text',
    text='',
    font='Open Sans',
    pos=(0,0.3), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-7.0);
fixation_rest = visual.ShapeStim(
    win=win, name='fixation_rest', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)

# Initialize components for Routine "Times_list"
Times_listClock = core.Clock()
# Set experiment start values for variable component block_number
block_number = 0
block_numberContainer = []

# Initialize components for Routine "NT"
NTClock = core.Clock()
error_msg=""
fixation_NT = visual.ShapeStim(
    win=win, name='fixation_NT', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
NT_N_L = visual.ImageStim(
    win=win,
    name='NT_N_L', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
NT_L_resp = keyboard.Keyboard()
NT_T_R = visual.ImageStim(
    win=win,
    name='NT_T_R', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
NT_R_resp = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
# Set experiment start values for variable component image_L
image_L = ''
image_LContainer = []
# Set experiment start values for variable component image_R
image_R = ''
image_RContainer = []
# Set experiment start values for variable component Times_L
Times_L = ''
Times_LContainer = []
# Set experiment start values for variable component Times_R
Times_R = ''
Times_RContainer = []
# Set experiment start values for variable component good_answer
good_answer = False
good_answerContainer = []
# Set experiment start values for variable component Routine_type
Routine_type = ""
Routine_typeContainer = []
# Set experiment start values for variable component inbetweenTime
inbetweenTime = 0
inbetweenTimeContainer = []
rest_text = visual.TextStim(win=win, name='rest_text',
    text='',
    font='Open Sans',
    pos=(0,0.3), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-7.0);
fixation_rest = visual.ShapeStim(
    win=win, name='fixation_rest', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)

# Initialize components for Routine "Times_list"
Times_listClock = core.Clock()
# Set experiment start values for variable component block_number
block_number = 0
block_numberContainer = []

# Initialize components for Routine "TN"
TNClock = core.Clock()
error_msg=""
fixation_TN = visual.ShapeStim(
    win=win, name='fixation_TN', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
TN_T_L_ = visual.ImageStim(
    win=win,
    name='TN_T_L_', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
TN_L_resp = keyboard.Keyboard()
TN_N_R = visual.ImageStim(
    win=win,
    name='TN_N_R', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
TN_R_resp = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
# Set experiment start values for variable component image_L
image_L = ''
image_LContainer = []
# Set experiment start values for variable component image_R
image_R = ''
image_RContainer = []
# Set experiment start values for variable component Times_L
Times_L = ''
Times_LContainer = []
# Set experiment start values for variable component Times_R
Times_R = ''
Times_RContainer = []
# Set experiment start values for variable component good_answer
good_answer = False
good_answerContainer = []
# Set experiment start values for variable component Routine_type
Routine_type = ""
Routine_typeContainer = []
# Set experiment start values for variable component inbetweenTime
inbetweenTime = 0
inbetweenTimeContainer = []
rest_text = visual.TextStim(win=win, name='rest_text',
    text='',
    font='Open Sans',
    pos=(0,0.3), height=0.09, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-7.0);
fixation_rest = visual.ShapeStim(
    win=win, name='fixation_rest', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)

# Initialize components for Routine "bey"
beyClock = core.Clock()
buy_msg = visual.TextStim(win=win, name='buy_msg',
    text='הניסוי הסתיים. \nתודה על השתתפותך.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
buy_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
any_key.keys = []
any_key.rt = []
_any_key_allKeys = []
# keep track of which components have finished
welcomeComponents = [agree, any_key]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *agree* updates
    if agree.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        agree.frameNStart = frameN  # exact frame index
        agree.tStart = t  # local t and not account for scr refresh
        agree.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(agree, 'tStartRefresh')  # time at next scr refresh
        agree.setAutoDraw(True)
    if agree.status == STARTED:
        if bool(any_key.corr==1):
            # keep track of stop time/frame for later
            agree.tStop = t  # not accounting for scr refresh
            agree.frameNStop = frameN  # exact frame index
            win.timeOnFlip(agree, 'tStopRefresh')  # time at next scr refresh
            agree.setAutoDraw(False)
    
    # *any_key* updates
    if any_key.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        any_key.frameNStart = frameN  # exact frame index
        any_key.tStart = t  # local t and not account for scr refresh
        any_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(any_key, 'tStartRefresh')  # time at next scr refresh
        any_key.status = STARTED
        # keyboard checking is just starting
        any_key.clock.reset()  # now t=0
    if any_key.status == STARTED:
        theseKeys = any_key.getKeys(keyList=['space'], waitRelease=False)
        _any_key_allKeys.extend(theseKeys)
        if len(_any_key_allKeys):
            any_key.keys = _any_key_allKeys[0].name  # just the first key pressed
            any_key.rt = _any_key_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if any_key.keys in ['', [], None]:  # No response was made
    any_key.keys = None
thisExp.addData('any_key.keys',any_key.keys)
if any_key.keys != None:  # we had a response
    thisExp.addData('any_key.rt', any_key.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
any_key_2.keys = []
any_key_2.rt = []
_any_key_2_allKeys = []
# keep track of which components have finished
instructionsComponents = [image, any_key_2]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        if bool(any_key.corr==1):
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # *any_key_2* updates
    if any_key_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        any_key_2.frameNStart = frameN  # exact frame index
        any_key_2.tStart = t  # local t and not account for scr refresh
        any_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(any_key_2, 'tStartRefresh')  # time at next scr refresh
        any_key_2.status = STARTED
        # keyboard checking is just starting
        any_key_2.clock.reset()  # now t=0
    if any_key_2.status == STARTED:
        theseKeys = any_key_2.getKeys(keyList=['space'], waitRelease=False)
        _any_key_2_allKeys.extend(theseKeys)
        if len(_any_key_2_allKeys):
            any_key_2.keys = _any_key_2_allKeys[0].name  # just the first key pressed
            any_key_2.rt = _any_key_2_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if any_key_2.keys in ['', [], None]:  # No response was made
    any_key_2.keys = None
thisExp.addData('any_key_2.keys',any_key_2.keys)
if any_key_2.keys != None:  # we had a response
    thisExp.addData('any_key_2.rt', any_key_2.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
load = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('LIST_All.xlsx'),
    seed=None, name='load')
thisExp.addLoop(load)  # add the loop to the experiment
thisLoad = load.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoad.rgb)
if thisLoad != None:
    for paramName in thisLoad:
        exec('{} = thisLoad[paramName]'.format(paramName))

for thisLoad in load:
    currentLoop = load
    # abbreviate parameter names if possible (e.g. rgb = thisLoad.rgb)
    if thisLoad != None:
        for paramName in thisLoad:
            exec('{} = thisLoad[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "imageLoader"-------
    continueRoutine = True
    # update component parameters for each repeat
    #if category not in image_dict:
    #    image_dict[category] = []
    if category=='N':
        image_N.append(stim_image)
    if category=='T':
        image_T.append(stim_image)
    #image_dict[category].append(stim_image)
    count=5
    # keep track of which components have finished
    imageLoaderComponents = []
    for thisComponent in imageLoaderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    imageLoaderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "imageLoader"-------
    while continueRoutine:
        # get current time
        t = imageLoaderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=imageLoaderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imageLoaderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "imageLoader"-------
    for thisComponent in imageLoaderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "imageLoader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'load'


# ------Prepare to start Routine "image_list"-------
continueRoutine = True
# update component parameters for each repeat
imageTL=[]
imageNL=[]
imageTR=[]
imageNR=[]
imageNL=image_N.copy()
imageNR=image_N.copy()
imageTL=image_T.copy()
imageTR=image_T.copy()
# keep track of which components have finished
image_listComponents = []
for thisComponent in image_listComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
image_listClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "image_list"-------
while continueRoutine:
    # get current time
    t = image_listClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=image_listClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in image_listComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "image_list"-------
for thisComponent in image_listComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "image_list" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Times_list"-------
continueRoutine = True
# update component parameters for each repeat
times_counter=0
testKD=0
beforeL=0
beforeR=0
L_counter=0
R_counter=0
L_keys=[]
num_keys=False
times=np.repeat([0.1,0.3,0.9],5)
shuffle(imageNR)
shuffle(imageNL)
shuffle(imageTR)
shuffle(imageTL)
shuffle(times)
keys_counter_R=0
keys_counter_L=0
end_routine=False
keys_R=[]
keys_L=[]
block_number+=1
# keep track of which components have finished
Times_listComponents = []
for thisComponent in Times_listComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Times_listClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Times_list"-------
while continueRoutine:
    # get current time
    t = Times_listClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Times_listClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Times_listComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Times_list"-------
for thisComponent in Times_listComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
times_counter=0
# the Routine "Times_list" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
example_loop_2 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='example_loop_2')
thisExp.addLoop(example_loop_2)  # add the loop to the experiment
thisExample_loop_2 = example_loop_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExample_loop_2.rgb)
if thisExample_loop_2 != None:
    for paramName in thisExample_loop_2:
        exec('{} = thisExample_loop_2[paramName]'.format(paramName))

for thisExample_loop_2 in example_loop_2:
    currentLoop = example_loop_2
    # abbreviate parameter names if possible (e.g. rgb = thisExample_loop_2.rgb)
    if thisExample_loop_2 != None:
        for paramName in thisExample_loop_2:
            exec('{} = thisExample_loop_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "example"-------
    continueRoutine = True
    # update component parameters for each repeat
    end_routine=False
    good_answer=False
    keys_counter_R=0
    keys_counter_L=0
    startTimeL = globalClock.getTime()
    image_L_set=imageNL[L_counter]
    image_R_set=imageNR[R_counter]
    press_time_R=0
    press_time_L=0
    name="NT"
    
    NN_N_L_p_2.setImage(imageNL[L_counter])
    NN_L_resp_p_2.keys = []
    NN_L_resp_p_2.rt = []
    _NN_L_resp_p_2_allKeys = []
    NN_N_R_p_2.setImage(imageNR[R_counter])
    NN_R_resp_p_2.keys = []
    NN_R_resp_p_2.rt = []
    _NN_R_resp_p_2_allKeys = []
    # keep track of which components have finished
    exampleComponents = [practice_helpL_2, practice_help_R_2, fixation_practice_2, NN_N_L_p_2, NN_L_resp_p_2, NN_N_R_p_2, NN_R_resp_p_2]
    for thisComponent in exampleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    exampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "example"-------
    while continueRoutine:
        # get current time
        t = exampleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=exampleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        keys_counter_R=len(NN_R_resp_p_2.keys)
        keys_counter_L=len(NN_L_resp_p_2.keys)
        if keys_counter_L==0:
            if keys_counter_R>1:
                end_routine=True
        else:
            if keys_counter_R > 0:
                end_routine=True
        if globalClock.getTime() - startTimeL >= 20:
            end_routine=True
        
        # *practice_helpL_2* updates
        if practice_helpL_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_helpL_2.frameNStart = frameN  # exact frame index
            practice_helpL_2.tStart = t  # local t and not account for scr refresh
            practice_helpL_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_helpL_2, 'tStartRefresh')  # time at next scr refresh
            practice_helpL_2.setAutoDraw(True)
        if practice_helpL_2.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                practice_helpL_2.tStop = t  # not accounting for scr refresh
                practice_helpL_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_helpL_2, 'tStopRefresh')  # time at next scr refresh
                practice_helpL_2.setAutoDraw(False)
        
        # *practice_help_R_2* updates
        if practice_help_R_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_help_R_2.frameNStart = frameN  # exact frame index
            practice_help_R_2.tStart = t  # local t and not account for scr refresh
            practice_help_R_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_help_R_2, 'tStartRefresh')  # time at next scr refresh
            practice_help_R_2.setAutoDraw(True)
        if practice_help_R_2.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                practice_help_R_2.tStop = t  # not accounting for scr refresh
                practice_help_R_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_help_R_2, 'tStopRefresh')  # time at next scr refresh
                practice_help_R_2.setAutoDraw(False)
        
        # *fixation_practice_2* updates
        if fixation_practice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_practice_2.frameNStart = frameN  # exact frame index
            fixation_practice_2.tStart = t  # local t and not account for scr refresh
            fixation_practice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_practice_2, 'tStartRefresh')  # time at next scr refresh
            fixation_practice_2.setAutoDraw(True)
        if fixation_practice_2.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                fixation_practice_2.tStop = t  # not accounting for scr refresh
                fixation_practice_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_practice_2, 'tStopRefresh')  # time at next scr refresh
                fixation_practice_2.setAutoDraw(False)
        
        # *NN_N_L_p_2* updates
        if NN_N_L_p_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            NN_N_L_p_2.frameNStart = frameN  # exact frame index
            NN_N_L_p_2.tStart = t  # local t and not account for scr refresh
            NN_N_L_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NN_N_L_p_2, 'tStartRefresh')  # time at next scr refresh
            NN_N_L_p_2.setAutoDraw(True)
        if NN_N_L_p_2.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                NN_N_L_p_2.tStop = t  # not accounting for scr refresh
                NN_N_L_p_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NN_N_L_p_2, 'tStopRefresh')  # time at next scr refresh
                NN_N_L_p_2.setAutoDraw(False)
        
        # *NN_L_resp_p_2* updates
        waitOnFlip = False
        if NN_L_resp_p_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            NN_L_resp_p_2.frameNStart = frameN  # exact frame index
            NN_L_resp_p_2.tStart = t  # local t and not account for scr refresh
            NN_L_resp_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NN_L_resp_p_2, 'tStartRefresh')  # time at next scr refresh
            NN_L_resp_p_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NN_L_resp_p_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NN_L_resp_p_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NN_L_resp_p_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NN_L_resp_p_2.tStartRefresh + times[times_counter]-frameTolerance:
                # keep track of stop time/frame for later
                NN_L_resp_p_2.tStop = t  # not accounting for scr refresh
                NN_L_resp_p_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NN_L_resp_p_2, 'tStopRefresh')  # time at next scr refresh
                NN_L_resp_p_2.status = FINISHED
        if NN_L_resp_p_2.status == STARTED and not waitOnFlip:
            theseKeys = NN_L_resp_p_2.getKeys(keyList=None, waitRelease=False)
            _NN_L_resp_p_2_allKeys.extend(theseKeys)
            if len(_NN_L_resp_p_2_allKeys):
                NN_L_resp_p_2.keys = [key.name for key in _NN_L_resp_p_2_allKeys]  # storing all keys
                NN_L_resp_p_2.rt = [key.rt for key in _NN_L_resp_p_2_allKeys]
        
        # *NN_N_R_p_2* updates
        if NN_N_R_p_2.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
            # keep track of start time/frame for later
            NN_N_R_p_2.frameNStart = frameN  # exact frame index
            NN_N_R_p_2.tStart = t  # local t and not account for scr refresh
            NN_N_R_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NN_N_R_p_2, 'tStartRefresh')  # time at next scr refresh
            NN_N_R_p_2.setAutoDraw(True)
        if NN_N_R_p_2.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                NN_N_R_p_2.tStop = t  # not accounting for scr refresh
                NN_N_R_p_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NN_N_R_p_2, 'tStopRefresh')  # time at next scr refresh
                NN_N_R_p_2.setAutoDraw(False)
        
        # *NN_R_resp_p_2* updates
        waitOnFlip = False
        if NN_R_resp_p_2.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
            # keep track of start time/frame for later
            NN_R_resp_p_2.frameNStart = frameN  # exact frame index
            NN_R_resp_p_2.tStart = t  # local t and not account for scr refresh
            NN_R_resp_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NN_R_resp_p_2, 'tStartRefresh')  # time at next scr refresh
            NN_R_resp_p_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NN_R_resp_p_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NN_R_resp_p_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NN_R_resp_p_2.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                NN_R_resp_p_2.tStop = t  # not accounting for scr refresh
                NN_R_resp_p_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NN_R_resp_p_2, 'tStopRefresh')  # time at next scr refresh
                NN_R_resp_p_2.status = FINISHED
        if NN_R_resp_p_2.status == STARTED and not waitOnFlip:
            theseKeys = NN_R_resp_p_2.getKeys(keyList=None, waitRelease=False)
            _NN_R_resp_p_2_allKeys.extend(theseKeys)
            if len(_NN_R_resp_p_2_allKeys):
                NN_R_resp_p_2.keys = [key.name for key in _NN_R_resp_p_2_allKeys]  # storing all keys
                NN_R_resp_p_2.rt = [key.rt for key in _NN_R_resp_p_2_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exampleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "example"-------
    for thisComponent in exampleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    times_counter+=1
    L_counter+=1
    R_counter+=1
    if R_counter==13 or L_counter==13 or times_counter==13:
        R_counter==0
        L_counter==0
        times_counter=0
        shuffle(imageNR)
        shuffle(imageNL)
    keys_counter_R=len(NN_R_resp_p_2.keys)
    keys_counter_L=len(NN_L_resp_p_2.keys)
    keys_R=NN_R_resp_p_2.keys
    keys_L=NN_L_resp_p_2.keys
    error_msg=""
    # no answer was recorded
    if keys_counter_R ==0 and keys_counter_L==0:
        error_msg="לא ענית"
    # was late to answer before the socnd pic came
    if keys_counter_L==0:
        if keys_counter_R<2:
            error_msg="לא עניתם"    
        else:
            if keys_R[0]!='d' or keys_R[1]!="k":
                error_msg= "נא ללחוץ על המקש המתאים"
            else:
                good_answer=True
    else:
        if keys_counter_L>1:
            error_msg="ענית מהר מדי"
        else:
            if keys_counter_R==0:
                error_msg="לא ענית"
            else:
                if keys_L[0]=='d' and keys_R[0]=="k":
                    good_answer=True
                else:
                    error_msg= "נא ללחוץ על המקש המתאים"
    if good_answer:
        good_answer_counter+=1
    else:
        good_answer_counter=0
    if good_answer_counter==6:
        trials.finished=True
        
    # check responses
    if NN_L_resp_p_2.keys in ['', [], None]:  # No response was made
        NN_L_resp_p_2.keys = None
    example_loop_2.addData('NN_L_resp_p_2.keys',NN_L_resp_p_2.keys)
    if NN_L_resp_p_2.keys != None:  # we had a response
        example_loop_2.addData('NN_L_resp_p_2.rt', NN_L_resp_p_2.rt)
    # check responses
    if NN_R_resp_p_2.keys in ['', [], None]:  # No response was made
        NN_R_resp_p_2.keys = None
    example_loop_2.addData('NN_R_resp_p_2.keys',NN_R_resp_p_2.keys)
    if NN_R_resp_p_2.keys != None:  # we had a response
        example_loop_2.addData('NN_R_resp_p_2.rt', NN_R_resp_p_2.rt)
    # the Routine "example" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "example_rest"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    rest_text_3.setText(error_msg)
    # keep track of which components have finished
    example_restComponents = [rest_text_3, practice_help_L_rest_2, practice_help_R_rest_2, fixation_practice_3]
    for thisComponent in example_restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    example_restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "example_rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = example_restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=example_restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_text_3* updates
        if rest_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_text_3.frameNStart = frameN  # exact frame index
            rest_text_3.tStart = t  # local t and not account for scr refresh
            rest_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_text_3, 'tStartRefresh')  # time at next scr refresh
            rest_text_3.setAutoDraw(True)
        if rest_text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_text_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                rest_text_3.tStop = t  # not accounting for scr refresh
                rest_text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_text_3, 'tStopRefresh')  # time at next scr refresh
                rest_text_3.setAutoDraw(False)
        
        # *practice_help_L_rest_2* updates
        if practice_help_L_rest_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_help_L_rest_2.frameNStart = frameN  # exact frame index
            practice_help_L_rest_2.tStart = t  # local t and not account for scr refresh
            practice_help_L_rest_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_help_L_rest_2, 'tStartRefresh')  # time at next scr refresh
            practice_help_L_rest_2.setAutoDraw(True)
        if practice_help_L_rest_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_help_L_rest_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                practice_help_L_rest_2.tStop = t  # not accounting for scr refresh
                practice_help_L_rest_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_help_L_rest_2, 'tStopRefresh')  # time at next scr refresh
                practice_help_L_rest_2.setAutoDraw(False)
        
        # *practice_help_R_rest_2* updates
        if practice_help_R_rest_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_help_R_rest_2.frameNStart = frameN  # exact frame index
            practice_help_R_rest_2.tStart = t  # local t and not account for scr refresh
            practice_help_R_rest_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_help_R_rest_2, 'tStartRefresh')  # time at next scr refresh
            practice_help_R_rest_2.setAutoDraw(True)
        if practice_help_R_rest_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_help_R_rest_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                practice_help_R_rest_2.tStop = t  # not accounting for scr refresh
                practice_help_R_rest_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_help_R_rest_2, 'tStopRefresh')  # time at next scr refresh
                practice_help_R_rest_2.setAutoDraw(False)
        
        # *fixation_practice_3* updates
        if fixation_practice_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_practice_3.frameNStart = frameN  # exact frame index
            fixation_practice_3.tStart = t  # local t and not account for scr refresh
            fixation_practice_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_practice_3, 'tStartRefresh')  # time at next scr refresh
            fixation_practice_3.setAutoDraw(True)
        if fixation_practice_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_practice_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fixation_practice_3.tStop = t  # not accounting for scr refresh
                fixation_practice_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_practice_3, 'tStopRefresh')  # time at next scr refresh
                fixation_practice_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in example_restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "example_rest"-------
    for thisComponent in example_restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'example_loop_2'


# ------Prepare to start Routine "before_practice"-------
continueRoutine = True
# update component parameters for each repeat
any_key_3.keys = []
any_key_3.rt = []
_any_key_3_allKeys = []
# keep track of which components have finished
before_practiceComponents = [image_3, any_key_3]
for thisComponent in before_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
before_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "before_practice"-------
while continueRoutine:
    # get current time
    t = before_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=before_practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    if image_3.status == STARTED:
        if bool(any_key.corr==1):
            # keep track of stop time/frame for later
            image_3.tStop = t  # not accounting for scr refresh
            image_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
            image_3.setAutoDraw(False)
    
    # *any_key_3* updates
    if any_key_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        any_key_3.frameNStart = frameN  # exact frame index
        any_key_3.tStart = t  # local t and not account for scr refresh
        any_key_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(any_key_3, 'tStartRefresh')  # time at next scr refresh
        any_key_3.status = STARTED
        # keyboard checking is just starting
        any_key_3.clock.reset()  # now t=0
    if any_key_3.status == STARTED:
        theseKeys = any_key_3.getKeys(keyList=['space'], waitRelease=False)
        _any_key_3_allKeys.extend(theseKeys)
        if len(_any_key_3_allKeys):
            any_key_3.keys = _any_key_3_allKeys[0].name  # just the first key pressed
            any_key_3.rt = _any_key_3_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in before_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "before_practice"-------
for thisComponent in before_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)
# check responses
if any_key_3.keys in ['', [], None]:  # No response was made
    any_key_3.keys = None
thisExp.addData('any_key_3.keys',any_key_3.keys)
if any_key_3.keys != None:  # we had a response
    thisExp.addData('any_key_3.rt', any_key_3.rt)
thisExp.nextEntry()
# the Routine "before_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Times_list"-------
continueRoutine = True
# update component parameters for each repeat
times_counter=0
testKD=0
beforeL=0
beforeR=0
L_counter=0
R_counter=0
L_keys=[]
num_keys=False
times=np.repeat([0.1,0.3,0.9],5)
shuffle(imageNR)
shuffle(imageNL)
shuffle(imageTR)
shuffle(imageTL)
shuffle(times)
keys_counter_R=0
keys_counter_L=0
end_routine=False
keys_R=[]
keys_L=[]
block_number+=1
# keep track of which components have finished
Times_listComponents = []
for thisComponent in Times_listComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Times_listClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Times_list"-------
while continueRoutine:
    # get current time
    t = Times_listClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Times_listClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Times_listComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Times_list"-------
for thisComponent in Times_listComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
times_counter=0
# the Routine "Times_list" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=50.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    end_routine=False
    good_answer=False
    keys_counter_R=0
    keys_counter_L=0
    startTimeL = globalClock.getTime()
    image_L_set=imageNL[L_counter]
    image_R_set=imageNR[R_counter]
    press_time_R=0
    press_time_L=0
    name="NT"
    if R_counter==13 or L_counter==13:
        R_counter==0
        L_counter==0
        shuffle(imageNR)
        shuffle(imageNL)
    NN_N_L_p.setImage(imageNL[L_counter])
    NN_L_resp_p.keys = []
    NN_L_resp_p.rt = []
    _NN_L_resp_p_allKeys = []
    NN_N_R_p.setImage(imageNR[R_counter])
    NN_R_resp_p.keys = []
    NN_R_resp_p.rt = []
    _NN_R_resp_p_allKeys = []
    # keep track of which components have finished
    practiceComponents = [practice_helpL, practice_help_R, fixation_practice, NN_N_L_p, NN_L_resp_p, NN_N_R_p, NN_R_resp_p]
    for thisComponent in practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        keys_counter_R=len(NN_R_resp_p.keys)
        keys_counter_L=len(NN_L_resp_p.keys)
        if keys_counter_L==0:
            if keys_counter_R>1:
                end_routine=True
        else:
            if keys_counter_R > 0:
                end_routine=True
        if globalClock.getTime() - startTimeL >= 20:
            end_routine=True
        
        # *practice_helpL* updates
        if practice_helpL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_helpL.frameNStart = frameN  # exact frame index
            practice_helpL.tStart = t  # local t and not account for scr refresh
            practice_helpL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_helpL, 'tStartRefresh')  # time at next scr refresh
            practice_helpL.setAutoDraw(True)
        if practice_helpL.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                practice_helpL.tStop = t  # not accounting for scr refresh
                practice_helpL.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_helpL, 'tStopRefresh')  # time at next scr refresh
                practice_helpL.setAutoDraw(False)
        
        # *practice_help_R* updates
        if practice_help_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_help_R.frameNStart = frameN  # exact frame index
            practice_help_R.tStart = t  # local t and not account for scr refresh
            practice_help_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_help_R, 'tStartRefresh')  # time at next scr refresh
            practice_help_R.setAutoDraw(True)
        if practice_help_R.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                practice_help_R.tStop = t  # not accounting for scr refresh
                practice_help_R.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_help_R, 'tStopRefresh')  # time at next scr refresh
                practice_help_R.setAutoDraw(False)
        
        # *fixation_practice* updates
        if fixation_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_practice.frameNStart = frameN  # exact frame index
            fixation_practice.tStart = t  # local t and not account for scr refresh
            fixation_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_practice, 'tStartRefresh')  # time at next scr refresh
            fixation_practice.setAutoDraw(True)
        if fixation_practice.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                fixation_practice.tStop = t  # not accounting for scr refresh
                fixation_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_practice, 'tStopRefresh')  # time at next scr refresh
                fixation_practice.setAutoDraw(False)
        
        # *NN_N_L_p* updates
        if NN_N_L_p.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            NN_N_L_p.frameNStart = frameN  # exact frame index
            NN_N_L_p.tStart = t  # local t and not account for scr refresh
            NN_N_L_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NN_N_L_p, 'tStartRefresh')  # time at next scr refresh
            NN_N_L_p.setAutoDraw(True)
        if NN_N_L_p.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                NN_N_L_p.tStop = t  # not accounting for scr refresh
                NN_N_L_p.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NN_N_L_p, 'tStopRefresh')  # time at next scr refresh
                NN_N_L_p.setAutoDraw(False)
        
        # *NN_L_resp_p* updates
        waitOnFlip = False
        if NN_L_resp_p.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            NN_L_resp_p.frameNStart = frameN  # exact frame index
            NN_L_resp_p.tStart = t  # local t and not account for scr refresh
            NN_L_resp_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NN_L_resp_p, 'tStartRefresh')  # time at next scr refresh
            NN_L_resp_p.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NN_L_resp_p.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NN_L_resp_p.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NN_L_resp_p.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NN_L_resp_p.tStartRefresh + times[times_counter]-frameTolerance:
                # keep track of stop time/frame for later
                NN_L_resp_p.tStop = t  # not accounting for scr refresh
                NN_L_resp_p.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NN_L_resp_p, 'tStopRefresh')  # time at next scr refresh
                NN_L_resp_p.status = FINISHED
        if NN_L_resp_p.status == STARTED and not waitOnFlip:
            theseKeys = NN_L_resp_p.getKeys(keyList=None, waitRelease=False)
            _NN_L_resp_p_allKeys.extend(theseKeys)
            if len(_NN_L_resp_p_allKeys):
                NN_L_resp_p.keys = [key.name for key in _NN_L_resp_p_allKeys]  # storing all keys
                NN_L_resp_p.rt = [key.rt for key in _NN_L_resp_p_allKeys]
        
        # *NN_N_R_p* updates
        if NN_N_R_p.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
            # keep track of start time/frame for later
            NN_N_R_p.frameNStart = frameN  # exact frame index
            NN_N_R_p.tStart = t  # local t and not account for scr refresh
            NN_N_R_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NN_N_R_p, 'tStartRefresh')  # time at next scr refresh
            NN_N_R_p.setAutoDraw(True)
        if NN_N_R_p.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                NN_N_R_p.tStop = t  # not accounting for scr refresh
                NN_N_R_p.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NN_N_R_p, 'tStopRefresh')  # time at next scr refresh
                NN_N_R_p.setAutoDraw(False)
        
        # *NN_R_resp_p* updates
        waitOnFlip = False
        if NN_R_resp_p.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
            # keep track of start time/frame for later
            NN_R_resp_p.frameNStart = frameN  # exact frame index
            NN_R_resp_p.tStart = t  # local t and not account for scr refresh
            NN_R_resp_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NN_R_resp_p, 'tStartRefresh')  # time at next scr refresh
            NN_R_resp_p.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NN_R_resp_p.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NN_R_resp_p.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NN_R_resp_p.status == STARTED:
            if bool(end_routine==True):
                # keep track of stop time/frame for later
                NN_R_resp_p.tStop = t  # not accounting for scr refresh
                NN_R_resp_p.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NN_R_resp_p, 'tStopRefresh')  # time at next scr refresh
                NN_R_resp_p.status = FINISHED
        if NN_R_resp_p.status == STARTED and not waitOnFlip:
            theseKeys = NN_R_resp_p.getKeys(keyList=None, waitRelease=False)
            _NN_R_resp_p_allKeys.extend(theseKeys)
            if len(_NN_R_resp_p_allKeys):
                NN_R_resp_p.keys = [key.name for key in _NN_R_resp_p_allKeys]  # storing all keys
                NN_R_resp_p.rt = [key.rt for key in _NN_R_resp_p_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    times_counter+=1
    L_counter+=1
    R_counter+=1
    if R_counter==13 or L_counter==13 or times_counter==13:
        R_counter==0
        L_counter==0
        times_counter=0
        shuffle(imageNR)
        shuffle(imageNL)
    keys_counter_R=len(NN_R_resp_p.keys)
    keys_counter_L=len(NN_L_resp_p.keys)
    keys_R=NN_R_resp_p.keys
    keys_L=NN_L_resp_p.keys
    error_msg=""
    # no answer was recorded
    if keys_counter_R ==0 and keys_counter_L==0:
        error_msg="לא ענית"
    # was late to answer before the socnd pic came
    if keys_counter_L==0:
        if keys_counter_R<2:
            error_msg="לא עניתם"    
        else:
            if keys_R[0]!='d' or keys_R[1]!="k":
                error_msg= "נא ללחוץ על המקש המתאים"
            else:
                good_answer=True
    else:
        if keys_counter_L>1:
            error_msg="ענית מהר מדי"
        else:
            if keys_counter_R==0:
                error_msg="לא ענית"
            else:
                if keys_L[0]=='d' and keys_R[0]=="k":
                    good_answer=True
                else:
                    error_msg= "נא ללחוץ על המקש המתאים"
    if good_answer:
        good_answer_counter+=1
    else:
        good_answer_counter=0
    if good_answer_counter==6:
        practice_loop.finished=True
        
    # check responses
    if NN_L_resp_p.keys in ['', [], None]:  # No response was made
        NN_L_resp_p.keys = None
    practice_loop.addData('NN_L_resp_p.keys',NN_L_resp_p.keys)
    if NN_L_resp_p.keys != None:  # we had a response
        practice_loop.addData('NN_L_resp_p.rt', NN_L_resp_p.rt)
    # check responses
    if NN_R_resp_p.keys in ['', [], None]:  # No response was made
        NN_R_resp_p.keys = None
    practice_loop.addData('NN_R_resp_p.keys',NN_R_resp_p.keys)
    if NN_R_resp_p.keys != None:  # we had a response
        practice_loop.addData('NN_R_resp_p.rt', NN_R_resp_p.rt)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rest_practice"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    rest_text_2.setText(error_msg)
    # keep track of which components have finished
    rest_practiceComponents = [rest_text_2, practice_help_L_rest, practice_help_R_rest, fixation_rest_2]
    for thisComponent in rest_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rest_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rest_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rest_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_text_2* updates
        if rest_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_text_2.frameNStart = frameN  # exact frame index
            rest_text_2.tStart = t  # local t and not account for scr refresh
            rest_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_text_2, 'tStartRefresh')  # time at next scr refresh
            rest_text_2.setAutoDraw(True)
        if rest_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                rest_text_2.tStop = t  # not accounting for scr refresh
                rest_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_text_2, 'tStopRefresh')  # time at next scr refresh
                rest_text_2.setAutoDraw(False)
        
        # *practice_help_L_rest* updates
        if practice_help_L_rest.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_help_L_rest.frameNStart = frameN  # exact frame index
            practice_help_L_rest.tStart = t  # local t and not account for scr refresh
            practice_help_L_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_help_L_rest, 'tStartRefresh')  # time at next scr refresh
            practice_help_L_rest.setAutoDraw(True)
        if practice_help_L_rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_help_L_rest.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                practice_help_L_rest.tStop = t  # not accounting for scr refresh
                practice_help_L_rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_help_L_rest, 'tStopRefresh')  # time at next scr refresh
                practice_help_L_rest.setAutoDraw(False)
        
        # *practice_help_R_rest* updates
        if practice_help_R_rest.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            practice_help_R_rest.frameNStart = frameN  # exact frame index
            practice_help_R_rest.tStart = t  # local t and not account for scr refresh
            practice_help_R_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_help_R_rest, 'tStartRefresh')  # time at next scr refresh
            practice_help_R_rest.setAutoDraw(True)
        if practice_help_R_rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_help_R_rest.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                practice_help_R_rest.tStop = t  # not accounting for scr refresh
                practice_help_R_rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_help_R_rest, 'tStopRefresh')  # time at next scr refresh
                practice_help_R_rest.setAutoDraw(False)
        
        # *fixation_rest_2* updates
        if fixation_rest_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_rest_2.frameNStart = frameN  # exact frame index
            fixation_rest_2.tStart = t  # local t and not account for scr refresh
            fixation_rest_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_rest_2, 'tStartRefresh')  # time at next scr refresh
            fixation_rest_2.setAutoDraw(True)
        if fixation_rest_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_rest_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fixation_rest_2.tStop = t  # not accounting for scr refresh
                fixation_rest_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_rest_2, 'tStopRefresh')  # time at next scr refresh
                fixation_rest_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rest_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest_practice"-------
    for thisComponent in rest_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 50.0 repeats of 'practice_loop'


# ------Prepare to start Routine "start_trials"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
start_trialsComponents = [text]
for thisComponent in start_trialsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_trials"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = start_trialsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_trialsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_trialsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_trials"-------
for thisComponent in start_trialsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
ready_to_trial = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ready_to_trial')
thisExp.addLoop(ready_to_trial)  # add the loop to the experiment
thisReady_to_trial = ready_to_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReady_to_trial.rgb)
if thisReady_to_trial != None:
    for paramName in thisReady_to_trial:
        exec('{} = thisReady_to_trial[paramName]'.format(paramName))

for thisReady_to_trial in ready_to_trial:
    currentLoop = ready_to_trial
    # abbreviate parameter names if possible (e.g. rgb = thisReady_to_trial.rgb)
    if thisReady_to_trial != None:
        for paramName in thisReady_to_trial:
            exec('{} = thisReady_to_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "countdown_to_start"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    countdown.setText(count)
    # keep track of which components have finished
    countdown_to_startComponents = [countdown]
    for thisComponent in countdown_to_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    countdown_to_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "countdown_to_start"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = countdown_to_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=countdown_to_startClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *countdown* updates
        if countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown.frameNStart = frameN  # exact frame index
            countdown.tStart = t  # local t and not account for scr refresh
            countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown, 'tStartRefresh')  # time at next scr refresh
            countdown.setAutoDraw(True)
        if countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                countdown.tStop = t  # not accounting for scr refresh
                countdown.frameNStop = frameN  # exact frame index
                win.timeOnFlip(countdown, 'tStopRefresh')  # time at next scr refresh
                countdown.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdown_to_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "countdown_to_start"-------
    for thisComponent in countdown_to_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    count -=1
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'ready_to_trial'


# set up handler to look after randomisation of conditions etc
block_random = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks.xlsx'),
    seed=None, name='block_random')
thisExp.addLoop(block_random)  # add the loop to the experiment
thisBlock_random = block_random.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_random.rgb)
if thisBlock_random != None:
    for paramName in thisBlock_random:
        exec('{} = thisBlock_random[paramName]'.format(paramName))

for thisBlock_random in block_random:
    currentLoop = block_random
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_random.rgb)
    if thisBlock_random != None:
        for paramName in thisBlock_random:
            exec('{} = thisBlock_random[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    NN_complete = data.TrialHandler(nReps=Task_NN, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='NN_complete')
    thisExp.addLoop(NN_complete)  # add the loop to the experiment
    thisNN_complete = NN_complete.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNN_complete.rgb)
    if thisNN_complete != None:
        for paramName in thisNN_complete:
            exec('{} = thisNN_complete[paramName]'.format(paramName))
    
    for thisNN_complete in NN_complete:
        currentLoop = NN_complete
        # abbreviate parameter names if possible (e.g. rgb = thisNN_complete.rgb)
        if thisNN_complete != None:
            for paramName in thisNN_complete:
                exec('{} = thisNN_complete[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Times_list"-------
        continueRoutine = True
        # update component parameters for each repeat
        times_counter=0
        testKD=0
        beforeL=0
        beforeR=0
        L_counter=0
        R_counter=0
        L_keys=[]
        num_keys=False
        times=np.repeat([0.1,0.3,0.9],5)
        shuffle(imageNR)
        shuffle(imageNL)
        shuffle(imageTR)
        shuffle(imageTL)
        shuffle(times)
        keys_counter_R=0
        keys_counter_L=0
        end_routine=False
        keys_R=[]
        keys_L=[]
        block_number+=1
        # keep track of which components have finished
        Times_listComponents = []
        for thisComponent in Times_listComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Times_listClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Times_list"-------
        while continueRoutine:
            # get current time
            t = Times_listClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Times_listClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Times_listComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Times_list"-------
        for thisComponent in Times_listComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        times_counter=0
        # the Routine "Times_list" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        NN_routine = data.TrialHandler(nReps=15.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='NN_routine')
        thisExp.addLoop(NN_routine)  # add the loop to the experiment
        thisNN_routine = NN_routine.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisNN_routine.rgb)
        if thisNN_routine != None:
            for paramName in thisNN_routine:
                exec('{} = thisNN_routine[paramName]'.format(paramName))
        
        for thisNN_routine in NN_routine:
            currentLoop = NN_routine
            # abbreviate parameter names if possible (e.g. rgb = thisNN_routine.rgb)
            if thisNN_routine != None:
                for paramName in thisNN_routine:
                    exec('{} = thisNN_routine[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "NN"-------
            continueRoutine = True
            # update component parameters for each repeat
            end_routine=False
            good_answer=False
            keys_counter_R=0
            keys_counter_L=0
            startTimeL = globalClock.getTime()
            image_L_set=imageNL[L_counter]
            image_R_set=imageNR[R_counter]
            press_time_R=0
            press_time_L=0
            name="NN"
            NN_N_L.setImage(imageNL[L_counter])
            NN_L_resp.keys = []
            NN_L_resp.rt = []
            _NN_L_resp_allKeys = []
            NN_N_R.setImage(imageNR[R_counter])
            NN_R_resp.keys = []
            NN_R_resp.rt = []
            _NN_R_resp_allKeys = []
            # keep track of which components have finished
            NNComponents = [fixation_NN, NN_N_L, NN_L_resp, NN_N_R, NN_R_resp]
            for thisComponent in NNComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            NNClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "NN"-------
            while continueRoutine:
                # get current time
                t = NNClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=NNClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                keys_counter_R=len(NN_R_resp.keys)
                keys_counter_L=len(NN_L_resp.keys)
                if keys_counter_L==0:
                    if keys_counter_R>1:
                        end_routine=True
                else:
                    if keys_counter_R > 0:
                        end_routine=True
                if globalClock.getTime() - startTimeL >= 20:
                    end_routine=True
                
                # *fixation_NN* updates
                if fixation_NN.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_NN.frameNStart = frameN  # exact frame index
                    fixation_NN.tStart = t  # local t and not account for scr refresh
                    fixation_NN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_NN, 'tStartRefresh')  # time at next scr refresh
                    fixation_NN.setAutoDraw(True)
                if fixation_NN.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        fixation_NN.tStop = t  # not accounting for scr refresh
                        fixation_NN.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_NN, 'tStopRefresh')  # time at next scr refresh
                        fixation_NN.setAutoDraw(False)
                
                # *NN_N_L* updates
                if NN_N_L.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    NN_N_L.frameNStart = frameN  # exact frame index
                    NN_N_L.tStart = t  # local t and not account for scr refresh
                    NN_N_L.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NN_N_L, 'tStartRefresh')  # time at next scr refresh
                    NN_N_L.setAutoDraw(True)
                if NN_N_L.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        NN_N_L.tStop = t  # not accounting for scr refresh
                        NN_N_L.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(NN_N_L, 'tStopRefresh')  # time at next scr refresh
                        NN_N_L.setAutoDraw(False)
                
                # *NN_L_resp* updates
                waitOnFlip = False
                if NN_L_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    NN_L_resp.frameNStart = frameN  # exact frame index
                    NN_L_resp.tStart = t  # local t and not account for scr refresh
                    NN_L_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NN_L_resp, 'tStartRefresh')  # time at next scr refresh
                    NN_L_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(NN_L_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(NN_L_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if NN_L_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > NN_L_resp.tStartRefresh + times[times_counter]-frameTolerance:
                        # keep track of stop time/frame for later
                        NN_L_resp.tStop = t  # not accounting for scr refresh
                        NN_L_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(NN_L_resp, 'tStopRefresh')  # time at next scr refresh
                        NN_L_resp.status = FINISHED
                if NN_L_resp.status == STARTED and not waitOnFlip:
                    theseKeys = NN_L_resp.getKeys(keyList=None, waitRelease=False)
                    _NN_L_resp_allKeys.extend(theseKeys)
                    if len(_NN_L_resp_allKeys):
                        NN_L_resp.keys = [key.name for key in _NN_L_resp_allKeys]  # storing all keys
                        NN_L_resp.rt = [key.rt for key in _NN_L_resp_allKeys]
                
                # *NN_N_R* updates
                if NN_N_R.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
                    # keep track of start time/frame for later
                    NN_N_R.frameNStart = frameN  # exact frame index
                    NN_N_R.tStart = t  # local t and not account for scr refresh
                    NN_N_R.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NN_N_R, 'tStartRefresh')  # time at next scr refresh
                    NN_N_R.setAutoDraw(True)
                if NN_N_R.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        NN_N_R.tStop = t  # not accounting for scr refresh
                        NN_N_R.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(NN_N_R, 'tStopRefresh')  # time at next scr refresh
                        NN_N_R.setAutoDraw(False)
                
                # *NN_R_resp* updates
                waitOnFlip = False
                if NN_R_resp.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
                    # keep track of start time/frame for later
                    NN_R_resp.frameNStart = frameN  # exact frame index
                    NN_R_resp.tStart = t  # local t and not account for scr refresh
                    NN_R_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NN_R_resp, 'tStartRefresh')  # time at next scr refresh
                    NN_R_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(NN_R_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(NN_R_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if NN_R_resp.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        NN_R_resp.tStop = t  # not accounting for scr refresh
                        NN_R_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(NN_R_resp, 'tStopRefresh')  # time at next scr refresh
                        NN_R_resp.status = FINISHED
                if NN_R_resp.status == STARTED and not waitOnFlip:
                    theseKeys = NN_R_resp.getKeys(keyList=None, waitRelease=False)
                    _NN_R_resp_allKeys.extend(theseKeys)
                    if len(_NN_R_resp_allKeys):
                        NN_R_resp.keys = [key.name for key in _NN_R_resp_allKeys]  # storing all keys
                        NN_R_resp.rt = [key.rt for key in _NN_R_resp_allKeys]
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in NNComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "NN"-------
            for thisComponent in NNComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            L_counter+=1
            R_counter+=1
            keys_counter_R=len(NN_R_resp.keys)
            keys_counter_L=len(NN_L_resp.keys)
            keys_R=NN_R_resp.keys
            keys_L=NN_L_resp.keys
            error_msg=""
            # no answer was recorded
            if keys_counter_R ==0 and keys_counter_L==0:
                error_msg="לא ענית"
            # was late to answer before the socnd pic came
            if keys_counter_L==0:
                if keys_counter_R<2:
                    error_msg="לא עניתם"    
                else:
                    if keys_R[0]!='d' or keys_R[1]!="k":
                        error_msg= "נא ללחוץ על המקש המתאים"
                    else:
                        good_answer=True
                        press_time_R=NN_R_resp.rt[1]
                        press_time_L=NN_R_resp.rt[0]+times[times_counter]
            else:
                if keys_counter_L>1:
                    error_msg="ענית מהר מדי"
                else:
                    if keys_counter_R==0:
                        error_msg="לא ענית"
                    else:
                        if keys_L[0]=='d' and keys_R[0]=="k":
                            press_time_R=NN_R_resp.rt[0]
                            press_time_L=NN_L_resp.rt[0]
                            good_answer=True
                        else:
                            error_msg= "נא ללחוץ על המקש המתאים"
            times_counter=times_counter+1
            # check responses
            if NN_L_resp.keys in ['', [], None]:  # No response was made
                NN_L_resp.keys = None
            NN_routine.addData('NN_L_resp.keys',NN_L_resp.keys)
            if NN_L_resp.keys != None:  # we had a response
                NN_routine.addData('NN_L_resp.rt', NN_L_resp.rt)
            # check responses
            if NN_R_resp.keys in ['', [], None]:  # No response was made
                NN_R_resp.keys = None
            NN_routine.addData('NN_R_resp.keys',NN_R_resp.keys)
            if NN_R_resp.keys != None:  # we had a response
                NN_routine.addData('NN_R_resp.rt', NN_R_resp.rt)
            # the Routine "NN" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "rest"-------
            continueRoutine = True
            # update component parameters for each repeat
            image_L = image_L_set  # Set routine start values for image_L
            image_R = image_R_set  # Set routine start values for image_R
            Times_L = press_time_L  # Set routine start values for Times_L
            Times_R = press_time_R  # Set routine start values for Times_R
            good_answer = good_answer  # Set routine start values for good_answer
            Routine_type = name  # Set routine start values for Routine_type
            inbetweenTime = times[times_counter-1]  # Set routine start values for inbetweenTime
            rest_text.setText(error_msg)
            # keep track of which components have finished
            restComponents = [rest_text, fixation_rest]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "rest"-------
            while continueRoutine:
                # get current time
                t = restClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=restClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rest_text* updates
                if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rest_text.frameNStart = frameN  # exact frame index
                    rest_text.tStart = t  # local t and not account for scr refresh
                    rest_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
                    rest_text.setAutoDraw(True)
                if rest_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rest_text.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        rest_text.tStop = t  # not accounting for scr refresh
                        rest_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rest_text, 'tStopRefresh')  # time at next scr refresh
                        rest_text.setAutoDraw(False)
                
                # *fixation_rest* updates
                if fixation_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_rest.frameNStart = frameN  # exact frame index
                    fixation_rest.tStart = t  # local t and not account for scr refresh
                    fixation_rest.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_rest, 'tStartRefresh')  # time at next scr refresh
                    fixation_rest.setAutoDraw(True)
                if fixation_rest.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_rest.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_rest.tStop = t  # not accounting for scr refresh
                        fixation_rest.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_rest, 'tStopRefresh')  # time at next scr refresh
                        fixation_rest.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "rest"-------
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('image_L.routineEndVal', image_L)  # Save end routine value
            thisExp.addData('image_R.routineEndVal', image_R)  # Save end routine value
            thisExp.addData('Times_L.routineEndVal', Times_L)  # Save end routine value
            thisExp.addData('Times_R.routineEndVal', Times_R)  # Save end routine value
            thisExp.addData('good_answer.routineEndVal', good_answer)  # Save end routine value
            thisExp.addData('Routine_type.routineEndVal', Routine_type)  # Save end routine value
            thisExp.addData('inbetweenTime.routineEndVal', inbetweenTime)  # Save end routine value
            # the Routine "rest" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 15.0 repeats of 'NN_routine'
        
    # completed Task_NN repeats of 'NN_complete'
    
    
    # set up handler to look after randomisation of conditions etc
    NT_complete = data.TrialHandler(nReps=Task_NT, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='NT_complete')
    thisExp.addLoop(NT_complete)  # add the loop to the experiment
    thisNT_complete = NT_complete.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNT_complete.rgb)
    if thisNT_complete != None:
        for paramName in thisNT_complete:
            exec('{} = thisNT_complete[paramName]'.format(paramName))
    
    for thisNT_complete in NT_complete:
        currentLoop = NT_complete
        # abbreviate parameter names if possible (e.g. rgb = thisNT_complete.rgb)
        if thisNT_complete != None:
            for paramName in thisNT_complete:
                exec('{} = thisNT_complete[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Times_list"-------
        continueRoutine = True
        # update component parameters for each repeat
        times_counter=0
        testKD=0
        beforeL=0
        beforeR=0
        L_counter=0
        R_counter=0
        L_keys=[]
        num_keys=False
        times=np.repeat([0.1,0.3,0.9],5)
        shuffle(imageNR)
        shuffle(imageNL)
        shuffle(imageTR)
        shuffle(imageTL)
        shuffle(times)
        keys_counter_R=0
        keys_counter_L=0
        end_routine=False
        keys_R=[]
        keys_L=[]
        block_number+=1
        # keep track of which components have finished
        Times_listComponents = []
        for thisComponent in Times_listComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Times_listClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Times_list"-------
        while continueRoutine:
            # get current time
            t = Times_listClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Times_listClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Times_listComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Times_list"-------
        for thisComponent in Times_listComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        times_counter=0
        # the Routine "Times_list" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        NT_routine = data.TrialHandler(nReps=15.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='NT_routine')
        thisExp.addLoop(NT_routine)  # add the loop to the experiment
        thisNT_routine = NT_routine.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisNT_routine.rgb)
        if thisNT_routine != None:
            for paramName in thisNT_routine:
                exec('{} = thisNT_routine[paramName]'.format(paramName))
        
        for thisNT_routine in NT_routine:
            currentLoop = NT_routine
            # abbreviate parameter names if possible (e.g. rgb = thisNT_routine.rgb)
            if thisNT_routine != None:
                for paramName in thisNT_routine:
                    exec('{} = thisNT_routine[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "NT"-------
            continueRoutine = True
            # update component parameters for each repeat
            end_routine=False
            good_answer=False
            keys_counter_R=0
            keys_counter_L=0
            startTimeL = globalClock.getTime()
            image_L_set=imageNL[L_counter]
            image_R_set=imageTR[R_counter]
            press_time_R=0
            press_time_L=0
            name="NT"
            NT_N_L.setImage(imageNL[L_counter])
            NT_L_resp.keys = []
            NT_L_resp.rt = []
            _NT_L_resp_allKeys = []
            NT_T_R.setImage(imageTR[R_counter])
            NT_R_resp.keys = []
            NT_R_resp.rt = []
            _NT_R_resp_allKeys = []
            # keep track of which components have finished
            NTComponents = [fixation_NT, NT_N_L, NT_L_resp, NT_T_R, NT_R_resp]
            for thisComponent in NTComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            NTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "NT"-------
            while continueRoutine:
                # get current time
                t = NTClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=NTClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                keys_counter_R=len(NT_R_resp.keys)
                keys_counter_L=len(NT_L_resp.keys)
                if keys_counter_L==0:
                    if keys_counter_R>1:
                        end_routine=True
                else:
                    if keys_counter_R > 0:
                        end_routine=True
                if globalClock.getTime() - startTimeL >= 20:
                    end_routine=True
                
                # *fixation_NT* updates
                if fixation_NT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_NT.frameNStart = frameN  # exact frame index
                    fixation_NT.tStart = t  # local t and not account for scr refresh
                    fixation_NT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_NT, 'tStartRefresh')  # time at next scr refresh
                    fixation_NT.setAutoDraw(True)
                if fixation_NT.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        fixation_NT.tStop = t  # not accounting for scr refresh
                        fixation_NT.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_NT, 'tStopRefresh')  # time at next scr refresh
                        fixation_NT.setAutoDraw(False)
                
                # *NT_N_L* updates
                if NT_N_L.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    NT_N_L.frameNStart = frameN  # exact frame index
                    NT_N_L.tStart = t  # local t and not account for scr refresh
                    NT_N_L.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NT_N_L, 'tStartRefresh')  # time at next scr refresh
                    NT_N_L.setAutoDraw(True)
                if NT_N_L.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        NT_N_L.tStop = t  # not accounting for scr refresh
                        NT_N_L.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(NT_N_L, 'tStopRefresh')  # time at next scr refresh
                        NT_N_L.setAutoDraw(False)
                
                # *NT_L_resp* updates
                waitOnFlip = False
                if NT_L_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    NT_L_resp.frameNStart = frameN  # exact frame index
                    NT_L_resp.tStart = t  # local t and not account for scr refresh
                    NT_L_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NT_L_resp, 'tStartRefresh')  # time at next scr refresh
                    NT_L_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(NT_L_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(NT_L_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if NT_L_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > NT_L_resp.tStartRefresh + times[times_counter]-frameTolerance:
                        # keep track of stop time/frame for later
                        NT_L_resp.tStop = t  # not accounting for scr refresh
                        NT_L_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(NT_L_resp, 'tStopRefresh')  # time at next scr refresh
                        NT_L_resp.status = FINISHED
                if NT_L_resp.status == STARTED and not waitOnFlip:
                    theseKeys = NT_L_resp.getKeys(keyList=None, waitRelease=False)
                    _NT_L_resp_allKeys.extend(theseKeys)
                    if len(_NT_L_resp_allKeys):
                        NT_L_resp.keys = [key.name for key in _NT_L_resp_allKeys]  # storing all keys
                        NT_L_resp.rt = [key.rt for key in _NT_L_resp_allKeys]
                
                # *NT_T_R* updates
                if NT_T_R.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
                    # keep track of start time/frame for later
                    NT_T_R.frameNStart = frameN  # exact frame index
                    NT_T_R.tStart = t  # local t and not account for scr refresh
                    NT_T_R.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NT_T_R, 'tStartRefresh')  # time at next scr refresh
                    NT_T_R.setAutoDraw(True)
                if NT_T_R.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        NT_T_R.tStop = t  # not accounting for scr refresh
                        NT_T_R.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(NT_T_R, 'tStopRefresh')  # time at next scr refresh
                        NT_T_R.setAutoDraw(False)
                
                # *NT_R_resp* updates
                waitOnFlip = False
                if NT_R_resp.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
                    # keep track of start time/frame for later
                    NT_R_resp.frameNStart = frameN  # exact frame index
                    NT_R_resp.tStart = t  # local t and not account for scr refresh
                    NT_R_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NT_R_resp, 'tStartRefresh')  # time at next scr refresh
                    NT_R_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(NT_R_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(NT_R_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if NT_R_resp.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        NT_R_resp.tStop = t  # not accounting for scr refresh
                        NT_R_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(NT_R_resp, 'tStopRefresh')  # time at next scr refresh
                        NT_R_resp.status = FINISHED
                if NT_R_resp.status == STARTED and not waitOnFlip:
                    theseKeys = NT_R_resp.getKeys(keyList=None, waitRelease=False)
                    _NT_R_resp_allKeys.extend(theseKeys)
                    if len(_NT_R_resp_allKeys):
                        NT_R_resp.keys = [key.name for key in _NT_R_resp_allKeys]  # storing all keys
                        NT_R_resp.rt = [key.rt for key in _NT_R_resp_allKeys]
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in NTComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "NT"-------
            for thisComponent in NTComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            L_counter+=1
            R_counter+=1
            keys_counter_R=len(NT_R_resp.keys)
            keys_counter_L=len(NT_L_resp.keys)
            keys_R=NT_R_resp.keys
            keys_L=NT_L_resp.keys
            error_msg=""
            # no answer was recorded
            if keys_counter_R ==0 and keys_counter_L==0:
                error_msg="לא ענית"
            # was late to answer before the socnd pic came
            if keys_counter_L==0:
                if keys_counter_R<2:
                    error_msg="לא עניתם"    
                else:
                    if keys_R[0]!='d' or keys_R[1]!="k":
                        error_msg= "נא ללחוץ על המקש המתאים"
                    else:
                        good_answer=True
                        press_time_R=NT_R_resp.rt[1]
                        press_time_L=NT_R_resp.rt[0]+times[times_counter]
            else:
                if keys_counter_L>1:
                    error_msg="ענית מהר מדי"
                else:
                    if keys_counter_R==0:
                        error_msg="לא ענית"
                    else:
                        if keys_L[0]=='d' and keys_R[0]=="k":
                            press_time_R=NT_R_resp.rt[0]
                            press_time_L=NT_L_resp.rt[0]
                            good_answer=True
                        else:
                            error_msg= "נא ללחוץ על המקש המתאים"
            
            times_counter=times_counter+1
            # check responses
            if NT_L_resp.keys in ['', [], None]:  # No response was made
                NT_L_resp.keys = None
            NT_routine.addData('NT_L_resp.keys',NT_L_resp.keys)
            if NT_L_resp.keys != None:  # we had a response
                NT_routine.addData('NT_L_resp.rt', NT_L_resp.rt)
            # check responses
            if NT_R_resp.keys in ['', [], None]:  # No response was made
                NT_R_resp.keys = None
            NT_routine.addData('NT_R_resp.keys',NT_R_resp.keys)
            if NT_R_resp.keys != None:  # we had a response
                NT_routine.addData('NT_R_resp.rt', NT_R_resp.rt)
            # the Routine "NT" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "rest"-------
            continueRoutine = True
            # update component parameters for each repeat
            image_L = image_L_set  # Set routine start values for image_L
            image_R = image_R_set  # Set routine start values for image_R
            Times_L = press_time_L  # Set routine start values for Times_L
            Times_R = press_time_R  # Set routine start values for Times_R
            good_answer = good_answer  # Set routine start values for good_answer
            Routine_type = name  # Set routine start values for Routine_type
            inbetweenTime = times[times_counter-1]  # Set routine start values for inbetweenTime
            rest_text.setText(error_msg)
            # keep track of which components have finished
            restComponents = [rest_text, fixation_rest]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "rest"-------
            while continueRoutine:
                # get current time
                t = restClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=restClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rest_text* updates
                if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rest_text.frameNStart = frameN  # exact frame index
                    rest_text.tStart = t  # local t and not account for scr refresh
                    rest_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
                    rest_text.setAutoDraw(True)
                if rest_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rest_text.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        rest_text.tStop = t  # not accounting for scr refresh
                        rest_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rest_text, 'tStopRefresh')  # time at next scr refresh
                        rest_text.setAutoDraw(False)
                
                # *fixation_rest* updates
                if fixation_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_rest.frameNStart = frameN  # exact frame index
                    fixation_rest.tStart = t  # local t and not account for scr refresh
                    fixation_rest.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_rest, 'tStartRefresh')  # time at next scr refresh
                    fixation_rest.setAutoDraw(True)
                if fixation_rest.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_rest.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_rest.tStop = t  # not accounting for scr refresh
                        fixation_rest.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_rest, 'tStopRefresh')  # time at next scr refresh
                        fixation_rest.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "rest"-------
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('image_L.routineEndVal', image_L)  # Save end routine value
            thisExp.addData('image_R.routineEndVal', image_R)  # Save end routine value
            thisExp.addData('Times_L.routineEndVal', Times_L)  # Save end routine value
            thisExp.addData('Times_R.routineEndVal', Times_R)  # Save end routine value
            thisExp.addData('good_answer.routineEndVal', good_answer)  # Save end routine value
            thisExp.addData('Routine_type.routineEndVal', Routine_type)  # Save end routine value
            thisExp.addData('inbetweenTime.routineEndVal', inbetweenTime)  # Save end routine value
            # the Routine "rest" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 15.0 repeats of 'NT_routine'
        
    # completed Task_NT repeats of 'NT_complete'
    
    
    # set up handler to look after randomisation of conditions etc
    TN_complete = data.TrialHandler(nReps=Task_TN, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='TN_complete')
    thisExp.addLoop(TN_complete)  # add the loop to the experiment
    thisTN_complete = TN_complete.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTN_complete.rgb)
    if thisTN_complete != None:
        for paramName in thisTN_complete:
            exec('{} = thisTN_complete[paramName]'.format(paramName))
    
    for thisTN_complete in TN_complete:
        currentLoop = TN_complete
        # abbreviate parameter names if possible (e.g. rgb = thisTN_complete.rgb)
        if thisTN_complete != None:
            for paramName in thisTN_complete:
                exec('{} = thisTN_complete[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Times_list"-------
        continueRoutine = True
        # update component parameters for each repeat
        times_counter=0
        testKD=0
        beforeL=0
        beforeR=0
        L_counter=0
        R_counter=0
        L_keys=[]
        num_keys=False
        times=np.repeat([0.1,0.3,0.9],5)
        shuffle(imageNR)
        shuffle(imageNL)
        shuffle(imageTR)
        shuffle(imageTL)
        shuffle(times)
        keys_counter_R=0
        keys_counter_L=0
        end_routine=False
        keys_R=[]
        keys_L=[]
        block_number+=1
        # keep track of which components have finished
        Times_listComponents = []
        for thisComponent in Times_listComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Times_listClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Times_list"-------
        while continueRoutine:
            # get current time
            t = Times_listClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Times_listClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Times_listComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Times_list"-------
        for thisComponent in Times_listComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        times_counter=0
        # the Routine "Times_list" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        TN_routine = data.TrialHandler(nReps=15.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='TN_routine')
        thisExp.addLoop(TN_routine)  # add the loop to the experiment
        thisTN_routine = TN_routine.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTN_routine.rgb)
        if thisTN_routine != None:
            for paramName in thisTN_routine:
                exec('{} = thisTN_routine[paramName]'.format(paramName))
        
        for thisTN_routine in TN_routine:
            currentLoop = TN_routine
            # abbreviate parameter names if possible (e.g. rgb = thisTN_routine.rgb)
            if thisTN_routine != None:
                for paramName in thisTN_routine:
                    exec('{} = thisTN_routine[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "TN"-------
            continueRoutine = True
            # update component parameters for each repeat
            end_routine=False
            good_answer=False
            keys_counter_R=0
            keys_counter_L=0
            startTimeL = globalClock.getTime()
            image_L_set=imageTL[L_counter]
            image_R_set=imageNR[R_counter]
            press_time_R=0
            press_time_L=0
            name="TN"
            TN_T_L_.setImage(imageTL[L_counter])
            TN_L_resp.keys = []
            TN_L_resp.rt = []
            _TN_L_resp_allKeys = []
            TN_N_R.setImage(imageNR[R_counter])
            TN_R_resp.keys = []
            TN_R_resp.rt = []
            _TN_R_resp_allKeys = []
            # keep track of which components have finished
            TNComponents = [fixation_TN, TN_T_L_, TN_L_resp, TN_N_R, TN_R_resp]
            for thisComponent in TNComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TNClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TN"-------
            while continueRoutine:
                # get current time
                t = TNClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TNClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                keys_counter_R=len(TN_R_resp.keys)
                keys_counter_L=len(TN_L_resp.keys)
                if keys_counter_L==0:
                    if keys_counter_R>1:
                        end_routine=True
                else:
                    if keys_counter_R > 0:
                        end_routine=True
                if globalClock.getTime() - startTimeL >= 20:
                    end_routine=True
                
                # *fixation_TN* updates
                if fixation_TN.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_TN.frameNStart = frameN  # exact frame index
                    fixation_TN.tStart = t  # local t and not account for scr refresh
                    fixation_TN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_TN, 'tStartRefresh')  # time at next scr refresh
                    fixation_TN.setAutoDraw(True)
                if fixation_TN.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        fixation_TN.tStop = t  # not accounting for scr refresh
                        fixation_TN.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_TN, 'tStopRefresh')  # time at next scr refresh
                        fixation_TN.setAutoDraw(False)
                
                # *TN_T_L_* updates
                if TN_T_L_.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    TN_T_L_.frameNStart = frameN  # exact frame index
                    TN_T_L_.tStart = t  # local t and not account for scr refresh
                    TN_T_L_.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TN_T_L_, 'tStartRefresh')  # time at next scr refresh
                    TN_T_L_.setAutoDraw(True)
                if TN_T_L_.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        TN_T_L_.tStop = t  # not accounting for scr refresh
                        TN_T_L_.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(TN_T_L_, 'tStopRefresh')  # time at next scr refresh
                        TN_T_L_.setAutoDraw(False)
                
                # *TN_L_resp* updates
                waitOnFlip = False
                if TN_L_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    TN_L_resp.frameNStart = frameN  # exact frame index
                    TN_L_resp.tStart = t  # local t and not account for scr refresh
                    TN_L_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TN_L_resp, 'tStartRefresh')  # time at next scr refresh
                    TN_L_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(TN_L_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(TN_L_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if TN_L_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > TN_L_resp.tStartRefresh + times[times_counter]-frameTolerance:
                        # keep track of stop time/frame for later
                        TN_L_resp.tStop = t  # not accounting for scr refresh
                        TN_L_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(TN_L_resp, 'tStopRefresh')  # time at next scr refresh
                        TN_L_resp.status = FINISHED
                if TN_L_resp.status == STARTED and not waitOnFlip:
                    theseKeys = TN_L_resp.getKeys(keyList=None, waitRelease=False)
                    _TN_L_resp_allKeys.extend(theseKeys)
                    if len(_TN_L_resp_allKeys):
                        TN_L_resp.keys = [key.name for key in _TN_L_resp_allKeys]  # storing all keys
                        TN_L_resp.rt = [key.rt for key in _TN_L_resp_allKeys]
                
                # *TN_N_R* updates
                if TN_N_R.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
                    # keep track of start time/frame for later
                    TN_N_R.frameNStart = frameN  # exact frame index
                    TN_N_R.tStart = t  # local t and not account for scr refresh
                    TN_N_R.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TN_N_R, 'tStartRefresh')  # time at next scr refresh
                    TN_N_R.setAutoDraw(True)
                if TN_N_R.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        TN_N_R.tStop = t  # not accounting for scr refresh
                        TN_N_R.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(TN_N_R, 'tStopRefresh')  # time at next scr refresh
                        TN_N_R.setAutoDraw(False)
                
                # *TN_R_resp* updates
                waitOnFlip = False
                if TN_R_resp.status == NOT_STARTED and tThisFlip >= times[times_counter]-frameTolerance:
                    # keep track of start time/frame for later
                    TN_R_resp.frameNStart = frameN  # exact frame index
                    TN_R_resp.tStart = t  # local t and not account for scr refresh
                    TN_R_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TN_R_resp, 'tStartRefresh')  # time at next scr refresh
                    TN_R_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(TN_R_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(TN_R_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if TN_R_resp.status == STARTED:
                    if bool(end_routine==True):
                        # keep track of stop time/frame for later
                        TN_R_resp.tStop = t  # not accounting for scr refresh
                        TN_R_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(TN_R_resp, 'tStopRefresh')  # time at next scr refresh
                        TN_R_resp.status = FINISHED
                if TN_R_resp.status == STARTED and not waitOnFlip:
                    theseKeys = TN_R_resp.getKeys(keyList=None, waitRelease=False)
                    _TN_R_resp_allKeys.extend(theseKeys)
                    if len(_TN_R_resp_allKeys):
                        TN_R_resp.keys = [key.name for key in _TN_R_resp_allKeys]  # storing all keys
                        TN_R_resp.rt = [key.rt for key in _TN_R_resp_allKeys]
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TNComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TN"-------
            for thisComponent in TNComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            L_counter+=1
            R_counter+=1
            keys_counter_R=len(TN_R_resp.keys)
            keys_counter_L=len(TN_L_resp.keys)
            keys_R=TN_R_resp.keys
            keys_L=TN_L_resp.keys
            error_msg=""
            # no answer was recorded
            if keys_counter_R ==0 and keys_counter_L==0:
                error_msg="לא ענית"
            # was late to answer before the socnd pic came
            if keys_counter_L==0:
                if keys_counter_R<2:
                    error_msg="לא עניתם"    
                else:
                    if keys_R[0]!='d' or keys_R[1]!="k":
                        error_msg= "נא ללחוץ על המקש המתאים"
                    else:
                        good_answer=True
                        press_time_R=TN_R_resp.rt[1]
                        press_time_L=TN_R_resp.rt[0]+times[times_counter]
            else:
                if keys_counter_L>1:
                    error_msg="ענית מהר מדי"
                else:
                    if keys_counter_R==0:
                        error_msg="לא ענית"
                    else:
                        if keys_L[0]=='d' and keys_R[0]=="k":
                            press_time_R=TN_R_resp.rt[0]
                            press_time_L=TN_L_resp.rt[0]
                            good_answer=True
                        else:
                            error_msg= "נא ללחוץ על המקש המתאים"
            times_counter=times_counter+1
            
            # check responses
            if TN_L_resp.keys in ['', [], None]:  # No response was made
                TN_L_resp.keys = None
            TN_routine.addData('TN_L_resp.keys',TN_L_resp.keys)
            if TN_L_resp.keys != None:  # we had a response
                TN_routine.addData('TN_L_resp.rt', TN_L_resp.rt)
            # check responses
            if TN_R_resp.keys in ['', [], None]:  # No response was made
                TN_R_resp.keys = None
            TN_routine.addData('TN_R_resp.keys',TN_R_resp.keys)
            if TN_R_resp.keys != None:  # we had a response
                TN_routine.addData('TN_R_resp.rt', TN_R_resp.rt)
            # the Routine "TN" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "rest"-------
            continueRoutine = True
            # update component parameters for each repeat
            image_L = image_L_set  # Set routine start values for image_L
            image_R = image_R_set  # Set routine start values for image_R
            Times_L = press_time_L  # Set routine start values for Times_L
            Times_R = press_time_R  # Set routine start values for Times_R
            good_answer = good_answer  # Set routine start values for good_answer
            Routine_type = name  # Set routine start values for Routine_type
            inbetweenTime = times[times_counter-1]  # Set routine start values for inbetweenTime
            rest_text.setText(error_msg)
            # keep track of which components have finished
            restComponents = [rest_text, fixation_rest]
            for thisComponent in restComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "rest"-------
            while continueRoutine:
                # get current time
                t = restClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=restClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rest_text* updates
                if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rest_text.frameNStart = frameN  # exact frame index
                    rest_text.tStart = t  # local t and not account for scr refresh
                    rest_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
                    rest_text.setAutoDraw(True)
                if rest_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rest_text.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        rest_text.tStop = t  # not accounting for scr refresh
                        rest_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rest_text, 'tStopRefresh')  # time at next scr refresh
                        rest_text.setAutoDraw(False)
                
                # *fixation_rest* updates
                if fixation_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_rest.frameNStart = frameN  # exact frame index
                    fixation_rest.tStart = t  # local t and not account for scr refresh
                    fixation_rest.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_rest, 'tStartRefresh')  # time at next scr refresh
                    fixation_rest.setAutoDraw(True)
                if fixation_rest.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_rest.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_rest.tStop = t  # not accounting for scr refresh
                        fixation_rest.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_rest, 'tStopRefresh')  # time at next scr refresh
                        fixation_rest.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "rest"-------
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('image_L.routineEndVal', image_L)  # Save end routine value
            thisExp.addData('image_R.routineEndVal', image_R)  # Save end routine value
            thisExp.addData('Times_L.routineEndVal', Times_L)  # Save end routine value
            thisExp.addData('Times_R.routineEndVal', Times_R)  # Save end routine value
            thisExp.addData('good_answer.routineEndVal', good_answer)  # Save end routine value
            thisExp.addData('Routine_type.routineEndVal', Routine_type)  # Save end routine value
            thisExp.addData('inbetweenTime.routineEndVal', inbetweenTime)  # Save end routine value
            # the Routine "rest" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 15.0 repeats of 'TN_routine'
        
    # completed Task_TN repeats of 'TN_complete'
    
# completed 2.0 repeats of 'block_random'


# ------Prepare to start Routine "bey"-------
continueRoutine = True
# update component parameters for each repeat
buy_key.keys = []
buy_key.rt = []
_buy_key_allKeys = []
# keep track of which components have finished
beyComponents = [buy_msg, buy_key]
for thisComponent in beyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bey"-------
while continueRoutine:
    # get current time
    t = beyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *buy_msg* updates
    if buy_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buy_msg.frameNStart = frameN  # exact frame index
        buy_msg.tStart = t  # local t and not account for scr refresh
        buy_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buy_msg, 'tStartRefresh')  # time at next scr refresh
        buy_msg.setAutoDraw(True)
    if buy_msg.status == STARTED:
        if bool(buy_key.corr==1):
            # keep track of stop time/frame for later
            buy_msg.tStop = t  # not accounting for scr refresh
            buy_msg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(buy_msg, 'tStopRefresh')  # time at next scr refresh
            buy_msg.setAutoDraw(False)
    
    # *buy_key* updates
    if buy_key.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buy_key.frameNStart = frameN  # exact frame index
        buy_key.tStart = t  # local t and not account for scr refresh
        buy_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buy_key, 'tStartRefresh')  # time at next scr refresh
        buy_key.status = STARTED
        # keyboard checking is just starting
        buy_key.clock.reset()  # now t=0
    if buy_key.status == STARTED:
        theseKeys = buy_key.getKeys(keyList=None, waitRelease=False)
        _buy_key_allKeys.extend(theseKeys)
        if len(_buy_key_allKeys):
            buy_key.keys = _buy_key_allKeys[0].name  # just the first key pressed
            buy_key.rt = _buy_key_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bey"-------
for thisComponent in beyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if buy_key.keys in ['', [], None]:  # No response was made
    buy_key.keys = None
thisExp.addData('buy_key.keys',buy_key.keys)
if buy_key.keys != None:  # we had a response
    thisExp.addData('buy_key.rt', buy_key.rt)
thisExp.nextEntry()
# the Routine "bey" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
