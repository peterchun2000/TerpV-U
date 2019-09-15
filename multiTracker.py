#!/usr/bin/python
#
# Copyright 2018 BIG VISION LLC ALL RIGHTS RESERVED
# 
from __future__ import print_function
import sys
import cv2
from random import randint
import time
import numpy as np

from flask_table import Table, Col
from w3lib.html import replace_entities

t0 = time.time()
tracked_times=[]
obj_location_list=[]
first = True
data_time_sum = 0

def get_data_sum():
  for data in obj_location_list:
    data_time_sum += obj_location_list[data]


class Usage:
  def __init__(self, x, y, start_time):
    self.x = x
    self.y = y
    self.start_time = start_time
    self.total_time = 0.0

trackerTypes = ['BOOSTING', 'MIL', 'KCF','TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

def createTrackerByName(trackerType):
  # Create a tracker based on tracker name
  if trackerType == trackerTypes[0]:
    tracker = cv2.TrackerBoosting_create()
  elif trackerType == trackerTypes[1]: 
    tracker = cv2.TrackerMIL_create()
  elif trackerType == trackerTypes[2]:
    tracker = cv2.TrackerKCF_create()
  elif trackerType == trackerTypes[3]:
    tracker = cv2.TrackerTLD_create()
  elif trackerType == trackerTypes[4]:
    tracker = cv2.TrackerMedianFlow_create()
  elif trackerType == trackerTypes[5]:
    tracker = cv2.TrackerGOTURN_create()
  elif trackerType == trackerTypes[6]:
    tracker = cv2.TrackerMOSSE_create()
  elif trackerType == trackerTypes[7]:
    tracker = cv2.TrackerCSRT_create()
  else:
    tracker = None
    print('Incorrect tracker name')
    print('Available trackers are:')
    for t in trackerTypes:
      print(t)
    
  return tracker

# if __name__ == '__main__':

#   print("Default tracking algoritm is CSRT \n"
#         "Available tracking algorithms are:\n")
#   for t in trackerTypes:
#       print(t)      

def match_with_obj(center_x_in, center_y_in):
  counter = 0
  for single_location in obj_location_list:
    checking_center_x = single_location.x 
    checking_center_y = single_location.y
    # print("subtracting x " + str(checking_center_x - center_x_in))
    # print("subtracting y" + str(checking_center_y - center_y_in))
    if abs(checking_center_x - center_x_in)<= 15 and abs(checking_center_y - center_y_in)<= 15:
      print("returned index" +str(counter))
      return counter
    elif counter+1 == len(obj_location_list):
      return -1
    counter +=1
  return 0

class ItemTable(Table):
  # start_time = Col('Start Time')
  total_time = Col('Total Time')

# Get some objects
class Item(object):
  def __init__(self, total_time):
    # self.start_time = start_time
    self.total_time = total_time

def make_table():
  items = []

  for obj in obj_location_list:
    items.append(Item(obj.total_time))
            
  # Populate the table
  table = ItemTable(items)

  table_html = str(table.__html__().replace("<table>",'<table class="table">'))
  # print(table_html)
  table_html = replace_entities(table_html)

  # counter1 = count(1)
  # table_html = re.sub('data-target="#demo', lambda m: m.group() + str(next(counter1)), table_html)
  
  # table_html = table_html.replace("</td></tr>", '</td></tr> <tr> <td colspan="6" class="hiddenRow"style="padding:0!important;"><div class="accordian-body collapse" id="demo"> <ul class="list-group"> [cmmt] </ul> </div></td></tr>')
  # counter2 = count(1)
  # table_html = re.sub('id="demo', lambda m: m.group() + str(next(counter2)), table_html)
  # for key, value in theme_dict.items():
  #     for sub_theme in value:
  #         table_html = table_html.replace('[cmmt]', get_cmmts(sub_theme.theme, theme_dict),1)
  # g.theme_dict = result_list

  return table_html

def get_cmmts(sub_theme_in, theme_dict_in):
    theme_dict = theme_dict_in

    result_str = ""
    for key, value in theme_dict.items():
        for sub_theme in value:
            if(sub_theme == SubTheme(sub_theme_in)):
                for ind_cmmt in sub_theme.comments:
    
                    result_str += '<li class="list-group-item">'+'<b>' + ind_cmmt.file_name + '</b>' + '<br>' + ind_cmmt.comment+"</li>"
    return result_str



def begin_tracking():
  global first
  trackerType = "CSRT"      

  # Set video to load
  videoPath = "videos/run.mp4"
  
  # Create a video capture object to read videos
  cap = cv2.VideoCapture(1)
 
  # Read first frame
  success, frame = cap.read()
  # quit if unable to read the video file
  if not success:
    print('Failed to read video')
    sys.exit(1)

  ## Select boxes
  bboxes = []
  colors = [] 

  # OpenCV's selectROI function doesn't work for selecting multiple objects in Python
  # So we will call this function in a loop till we are done selecting all objects
  while True:
    # draw bounding boxes over objects
    # selectROI's default behaviour is to draw box starting from the center
    # when fromCenter is set to false, you can draw box starting from top left corner
    bbox = cv2.selectROI('MultiTracker', frame)
    bboxes.append(bbox)
    colors.append((randint(64, 255), randint(64, 255), randint(64, 255)))
    print("Press q to quit selecting boxes and start tracking")
    print("Press any other key to select next object")
    k = cv2.waitKey(0) & 0xFF
    if (k == 113):  # q is pressed
      break
  
  print('Selected bounding boxes {}'.format(bboxes))

  ## Initialize MultiTracker
  # There are two ways you can initialize multitracker
  # 1. tracker = cv2.MultiTracker("CSRT")
  # All the trackers added to this multitracker
  # will use CSRT algorithm as default
  # 2. tracker = cv2.MultiTracker()
  # No default algorithm specified

  # Initialize MultiTracker with tracking algo
  # Specify tracker type
  
  # Create MultiTracker object
  multiTracker = cv2.MultiTracker_create()

  # Initialize MultiTracker 
  for bbox in bboxes:
    multiTracker.add(createTrackerByName(trackerType), frame, bbox)


  # Process video and track objects
  while cap.isOpened():
    success, frame = cap.read()
    if not success:
      break
    
    # get updated location of objects in subsequent frames
    success, boxes = multiTracker.update(frame)

    # draw tracked objects
    for i, newbox in enumerate(boxes):
      # box = cv2.boxPoints(i)
      t1 = time.time()
      print("t1  ", t1)
      total = t1-t0
      p1 = (int(newbox[0]), int(newbox[1]))
      center_x = (newbox[0] + newbox[3])/2
      center_y = (newbox[2] + newbox[3])/2
      center_text = "Center: "+str(center_x) +", " +str(center_y)
      print(center_text)
      index_of_obj = match_with_obj(center_x,center_y)
      if index_of_obj != -1 and not first:
        obj_location_list[index_of_obj].total_time = t1 - obj_location_list[index_of_obj].start_time

        print("time for index "+str(index_of_obj)+  ": "+str(obj_location_list[index_of_obj].total_time))
      else:
        obj_location_list.append(Usage(center_x,center_y,time.time() ))
        print("making new")
        first = False
      p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
      cv2.rectangle(frame, p1, p2, colors[i], 2, 1)

    # show frame
    cv2.imshow('MultiTracker', frame)
    

    # quit on ESC button
    if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
      print(str(make_table()))
      return str(make_table())
      
