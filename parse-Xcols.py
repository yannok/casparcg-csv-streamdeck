#!/usr/bin/env python3
import os
import json
import csv
import sys
import os
import string
import random
import re
import copy
from objectscompanion import *

# global variables
runorder_dict = {}
config_dict = {}
unique_id_list = []
guestfile_number = 0

# fill the runorder dictionary from CSV file
def parseCSV(csv_filename):
    global runorder_dict
    with open(csv_filename, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        # Extract headers from first row, if they exist
        headers = next(reader, None)
        for row in reader:
            for i, value in enumerate(row):
                # Generate a header name if none exist
                header = headers[i] if headers else f'column{i+1}'
                if header not in runorder_dict:
                    runorder_dict[header] = []
                runorder_dict[header].append(value)

def init_vars_data():
    global runorder_dict
    global order_number_index
    global page_number_index
    global button_number_index
    global custom_var_index
    global number_of_items
    global number_of_custom_variables
    global keys
    keys = list(runorder_dict.keys())
    # columns are : run_order | page_num | button_num | cutom_var1 | custom_var2 |...
    order_number_index = keys[0]
    page_number_index = keys[1]
    button_number_index = keys[2]
    custom_var_index = keys[3]
    number_of_items = len(runorder_dict[order_number_index])
    number_of_keys = len(runorder_dict)
    number_of_custom_variables = number_of_keys - 3
    

def init_vars_companion():
    global instance_id_caspar
    global instance_id_companion
    global config_dict
    for instance_name, instance_data in config_dict['instances'].items():
        if instance_data['instance_type'] == 'casparcg-server':
            instance_id_caspar = instance_name
        elif instance_data['instance_type'] == 'bitfocus-companion':
            instance_id_companion = instance_name
    print(instance_id_caspar, instance_id_companion)
    
def clear_all_buttons_in_page_range(first_page, last_page):
    global runorder_dict
    for page in range(first_page, last_page):
      for button in range (1, 32):
        config_dict["config"][str(page)][str(button)] = {}
        config_dict["actions"][str(page)][str(button)] = {}
        config_dict["release_actions"][str(page)][str(button)] = {}
        config_dict["feedbacks"][str(page)][str(button)] = {}

def open_companion_config(filename):
    global config_dict
    with open(filename, 'r') as f:
        config_dict = json.load(f)

def write_companion_config(filename):
    global config_dict
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(config_dict, f, indent=4, ensure_ascii=False)
    
def configure_all_title_buttons():
    global runorder_dict
    global button_conf
    for i in range(0, number_of_items):
        button_copy = button_conf.copy() # otherwise it is passed as a reference
        button_copy["text"] = runorder_dict[order_number_index][i] + "\\n" + runorder_dict[custom_var_index][i] # fullname is at custom_var_index position
        config_dict["config"][str(runorder_dict[page_number_index][i])][str(runorder_dict[button_number_index][i])] = button_copy

# for each custom action defined, modify all the required fields (instances, variables values, ID, ...)
def parse_action_item(action_item, order_number):
    global guestfile_number
    # generate a new unique ID
    unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
    action_item['id'] = unique_id
    unique_id_list.append(unique_id) # store it to check unicity at the end
    # fill "label" and "instance" with correct instance (either companion or casparcg instance in this case)
    instance_id = instance_id_caspar
    if "bitfocus" in action_item['label'].lower():
        instance_id = instance_id_companion
    action_item['label'] = re.sub(r'^.*:', instance_id + ":", action_item['label']) # replace first part of the label string
    action_item['instance'] = instance_id
    # for custom PROG/PREV_OUT actions, no order_number is provided
    if order_number >= 0:
      # fill correct prev variable value with page-button nrs
      if "custom_variable_set_value" in action_item['action']:
          action_item['options']['value'] = runorder_dict[page_number_index][order_number].zfill(2) + runorder_dict[button_number_index][order_number].zfill(2)
      # fill template variables in CG ADD command
      if "CG ADD" in action_item['action']:
          template_variables = ""
          for field_nr in range (0, number_of_custom_variables):
              # ex: f0="Kim Bora", f1="Piano", f2="Sonate"
              try:
                if runorder_dict[keys[3 + field_nr]][order_number] != "":
                  template_variables += "f" + str(field_nr) + '=\"' + runorder_dict[keys[3 + field_nr]][order_number] + '\", ' # custom variables start from key 3
              except IndexError:
                print("no value for this field :", field_nr)
                continue
          if template_variables != "":
              action_item['options']['variables'] = template_variables
      if "COMMAND" in action_item['action'] and "GUESTFILENAME" in action_item['options']['cmd']:
          guestfilename = stored_data_filename + "{:02d}".format(guestfile_number) # ex: invit01
          action_item['options']['cmd'] = action_item['options']['cmd'].replace("GUESTFILENAME", guestfilename)


def parse_feedback_item(feedback_item, order_number):
    # generate a new unique ID
    unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
    feedback_item['id'] = unique_id
    unique_id_list.append(unique_id) # store it to check unicity at the end
    # fill instance_id with internal id (no exisiting casparcg feedback)
    feedback_item['instance_id'] = instance_id_companion
    # fill correct prev variable value using page-button numbers (four digits)
    if feedback_item['type'] == "variable_value":
        if feedback_item['options']['variable'] == "internal:custom_prog" or feedback_item['options']['variable'] == "internal:custom_prev":
            feedback_item['options']['value'] = runorder_dict[page_number_index][order_number].zfill(2) + runorder_dict[button_number_index][order_number].zfill(2)
      

def configure_all_title_prev_actions():
    global runorder_dict
    global button_conf
    global unique_id_list
    global guestfile_number
    guestfile_number = 0
    
    # for each entry in the csv (dict)
    for order_number in range(0, number_of_items):
      actions_preview_copy = []
      # FOR CUSTOM_ACTION (not title), USE custom_actions_preview/prog instead of actions_preview/prog
      # check if fullname is a reserved custom word:
      if (runorder_dict[custom_var_index][order_number] in custom_titles):
        actions_preview_copy = copy.deepcopy(custom_actions_preview) # deepcopy required here! (otherwise all actions will be equal to the last assignement)
      # FOR GUESTS (not title, not custom), USE guest_actions_preview/prog instead of actions_preview/prog
      elif (runorder_dict[custom_var_index][order_number] in guest_titles):
        actions_preview_copy = copy.deepcopy(guest_actions_preview) # deepcopy
        guestfile_number += 1
      else:
        actions_preview_copy = copy.deepcopy(actions_preview) # deepcopy
      # modify each action according to the data provided:
      for action_item in actions_preview_copy:
          parse_action_item(action_item, order_number)
      print ("action for line ", order_number, ":\n", actions_preview_copy)
      config_dict['actions'][str(runorder_dict[page_number_index][order_number])][str(runorder_dict[button_number_index][order_number])] = actions_preview_copy


def configure_all_title_prog_actions():
    global runorder_dict
    global button_conf
    global unique_id_list
    global guestfile_number
    guestfile_number = 0
    
    # for each entry in the csv (dict)
    for order_number in range(0, number_of_items):
      actions_prog_copy = []
      # FOR CUSTOM_ACTION (not title), USE custom_actions_preview/prog instead of actions_preview/prog
      # check if fullname is a reserved custom word:
      if (runorder_dict[custom_var_index][order_number] in custom_titles):
        actions_prog_copy = copy.deepcopy(custom_actions_prog) # deepcopy required here! (otherwise all actions will be equal to the last assignement)
      # FOR GUEST (not title, not custom), USE guest_actions_preview/prog instead of actions_preview/prog
      elif (runorder_dict[custom_var_index][order_number] in guest_titles):
        actions_prog_copy = copy.deepcopy(guest_actions_prog) # deepcopy required here! (otherwise all actions will be equal to the last assignement)
        guestfile_number += 1
      else:
        actions_prog_copy = copy.deepcopy(actions_prog) # deepcopy
      # modify each action according to the data provided:
      for action_item in actions_prog_copy:
        parse_action_item(action_item, order_number)
      #print ("release action for line ", order_number, ":\n", actions_prog_copy)
      config_dict['release_actions'][str(runorder_dict[page_number_index][order_number])][str(runorder_dict[button_number_index][order_number])] = actions_prog_copy

def configure_all_feedbacks():
    for order_number in range(0, number_of_items):
        feedbacks_button_copy = copy.deepcopy(feedbacks_button) # deepcopy
        # modify each action according to the data provided:
        for feedback_item in feedbacks_button_copy:
            parse_feedback_item(feedback_item, order_number)
        #print ("feedback item for line ", order_number, ":\n", feedbacks_button_copy)
        config_dict['feedbacks'][str(runorder_dict[page_number_index][order_number])][str(runorder_dict[button_number_index][order_number])] = feedbacks_button_copy
       
def copy_last_row_template_on_pages(first_page, last_page):
    for page in range(first_page, last_page + 1):
        # button labels and pages
        config_dict['config'][str(page)].update(buttons_conf_last_row)

def copy_out_actions_on_pages(first_page, last_page, prev_out_btn_nr, prog_out_btn_nr):
    for page in range(first_page, last_page + 1):
        # OUT PREVIEW
        actions_preview_out_copy = copy.deepcopy(actions_preview_out)
        for action_preview_out_item in actions_preview_out_copy:
            parse_action_item(action_preview_out_item, -1)  # order_number = -1 because this item is not linked to a CSV entry
        config_dict['actions'][str(page)][str(prev_out_btn_nr)]= actions_preview_out_copy
        
        # OUT PROGRAM
        actions_program_out_copy = copy.deepcopy(actions_program_out)
        for action_program_out_item in actions_program_out_copy:
            parse_action_item(action_program_out_item, -1)
        config_dict['actions'][str(page)][str(prog_out_btn_nr)] = actions_program_out_copy

def add_unlatch_all_but_me_actions():
    global runorder_dict
    # for each entry in the csv (dict)
    for order_number in range(0, number_of_items):
      page_order_number = runorder_dict[page_number_index][order_number]
      button_order_number = runorder_dict[button_number_index][order_number]
      # unlatch all other buttons in the csv
      for unlatched_entry in range(0, number_of_items):
        if unlatched_entry != order_number: # "but me"
            action_unlatch_copy = copy.deepcopy(action_unlatch)
            parse_action_item(action_unlatch_copy, -1) # generate unique ID and set instance_id
            action_unlatch_copy['options']['page'] = runorder_dict[page_number_index][unlatched_entry]
            action_unlatch_copy['options']['bank'] = runorder_dict[button_number_index][unlatched_entry]
            config_dict['actions'][page_order_number][button_order_number].append(action_unlatch_copy)


def add_unlatch_all_on_out_buttons(first_page, last_page, prev_out_btn_nr, prog_out_btn_nr):
    global runorder_dict
    # for each CSV entry, add unlatch actions on button prev_out_btn_nr (31) and prog_out_btn_nr (32) on all pages
    for order_number in range(0, number_of_items):
        for page in range(first_page, last_page + 1):
            # OUT PREVIEW
            action_unlatch_copy = copy.deepcopy(action_unlatch)
            parse_action_item(action_unlatch_copy, -1) # generate unique ID and set instance_id
            action_unlatch_copy['options']['page'] = runorder_dict[page_number_index][order_number]
            action_unlatch_copy['options']['bank'] = runorder_dict[button_number_index][order_number]
            config_dict['actions'][str(page)][str(prev_out_btn_nr)].append(action_unlatch_copy)
            # OUT PROGRAM : no need to addd unlatch actions because OUT PROG button calls automatically OUT_PREV Button
               
    
# check if the random strings generated for the id are all different
def verify_all_unique_ids():
    global unique_id_list
    if len(unique_id_list) == len(set(unique_id_list)): # set(list) removes any duplicate in list
        print("All items in the list are unique!")
    else:
        print("There are duplicates in the list.")


def main():
    parseCSV(sys.argv[1]) # Get the CSV file path from command-line arguments
    init_vars_data()
    open_companion_config(input_companionconfigfilename)
    # add custom button in the dictionary
    init_vars_companion()
    clear_all_buttons_in_page_range(1,99)
    configure_all_title_buttons()
    configure_all_title_prev_actions()
    configure_all_title_prog_actions()
    configure_all_feedbacks()
    copy_last_row_template_on_pages(1, 99)
    copy_out_actions_on_pages(1, 99, 31, 32)
    add_unlatch_all_but_me_actions()
    add_unlatch_all_on_out_buttons(1, 99, 31, 32)
    verify_all_unique_ids() # almost no chance to generate twice the same id but should be checked anyway
    output_filename=os.path.splitext(sys.argv[1])[0] + ".companionconfig"
    write_companion_config(output_filename)


if __name__ == "__main__":
    main()
