#input_csv_filename = 'input.csv' 
input_companionconfigfilename = 'template.companionconfig.json'
#output_companionconfigfilename = 'output.json'
false = False

# special keywords for custom actions (not lower third title) -> custom_actions_preview/prog will be used instead
custom_titles= [ 'PUBS', 'CUSTOM' ]
guest_titles= [ 'GUEST', 'GUEST01', 'GUEST02', 'GUEST03','GUEST04', 'GUEST05', 'GUEST06', 'GUEST07', 'GUEST08','GUEST09', 'GUEST10' ]

# for titles values read from a file instead of the excel sheet:
stored_data_filename = "invit" # a two-digits number will be added (invit01, invit02, ...)

# could be an object class instead (IMPROVEMENTS, see README.txt)
button_conf = {
    "style": "png",
    "text": "RO\\nFullname",
    "size": "auto",
    "alignment": "center:center",
    "pngalignment": "center:center",
    "color": 16777215,
    "bgcolor": 14818589,
    "latch": True,
    "relative_delay": False,
    "show_topbar": False,
    "rotary_actions": False
}

# could be an object class instead (IMPROVEMENTS, see README.txt)
action_test = {
    "id": "dy91Mi6Zk",
    "label": "f0d6ZANcR:COMMAND",
    "instance": "f0d6ZANcR",
    "action": "COMMAND",
    "options": {
        "cmd": "LOAD 2-10 \"BANDEAU-VIERGE\" CUT 0 Linear RIGHT"
    },
    "delay": 0
}

# set of action when pressing button (pressed once=latched) -> send to preview
# "id" = unique identifier (random)
# "label" = instance_id:command
# "instance" = instance_id
actions_preview = [
    {
        "id": "XXXXXXXXX",
        "label": "YYYYYYYYY:COMMAND",
        "instance": "YYYYYYYYY",
        "action": "COMMAND",
        "options": {
                    "cmd": "LOAD 2-10 \"BANDEAU-VIERGE\" CUT 0 Linear RIGHT"
        },
        "delay": 0
    },
    {
        "id": "3ECcUZ2uSl",
        "label": "f0d6ZANcR:GOTO",
        "instance": "f0d6ZANcR",
        "action": "GOTO",
        "options": {
                    "channel": "2",
                    "layer": "10",
                    "offset": "2"
        },
        "delay": 1
    },
    {
        "id": "M53dtLpC0C",
        "label": "bitfocus-companion:custom_variable_set_value",
        "instance": "bitfocus-companion",
        "action": "custom_variable_set_value",
        "options": {
                    "name": "prev",
                    "value": "XXXX"
        },
        "delay": 0
    },
    {
        "id": "AopqhKcHZD",
        "label": "f0d6ZANcR:CG ADD",
        "instance": "f0d6ZANcR",
        "action": "CG ADD",
        "options": {
                    "channel": "2",
                    "layer": "11",
                    "template_dd": "",
                    "template": "lower3rd",
                    "playonload": "true",
                    "templatelayer": "1",
                    "json": True,
                    "variables": "f0=\"Field1\", f1=\"Field2\""
        },
        "delay": 0
    }
]

# set of action when releasing button (pressed twice) -> send to program
actions_prog = [
    {
        "id": "7pB1DrUNs9",
        "label": "bitfocus-companion:custom_variable_set_value",
        "instance": "bitfocus-companion",
        "action": "custom_variable_set_value",
        "options": {
                    "name": "prog",
                    "value": "0000"
        },
        "delay": 1
    },
    {
        "id": "WGEBiPXjg-",
        "label": "f0d6ZANcR:COMMAND",
        "instance": "f0d6ZANcR",
        "action": "COMMAND",
        "options": {
                    "cmd": "PLAY 1-10 \"BANDEAU-VIERGE\" CUT 0 Linear RIGHT"
        },
        "delay": 1
    },
    {
        "id": "auyueb3gwg",
        "label": "f0d6ZANcR:CG ADD",
        "instance": "f0d6ZANcR",
        "action": "CG ADD",
        "options": {
                    "channel": 1,
                    "layer": "11",
                    "template_dd": "",
                    "template": "lower3rd",
                    "playonload": "true",
                    "templatelayer": "1",
                    "json": True,
                    "variables": "f0=\"Jose James\", f1=\"Trompette\""
        },
        "delay": 400
    },
    {
        "id": "Hy9IxZfaKZ",
        "label": "bitfocus-companion:bgcolor",
        "instance": "bitfocus-companion",
        "action": "bgcolor",
        "options": {
                    "color": 14818589,
                    "page": 0,
                    "bank": 0
        },
        "delay": 1
    }
]

# for a button that is not a title (ex:  social media banner, no text)
custom_actions_preview = [
    {
        "id": "XXXXXXXXX",
        "label": "YYYYYYYYY:COMMAND",
        "instance": "YYYYYYYYY",
        "action": "COMMAND",
        "options": {
                    "cmd": "LOAD 2-10 \"BANDEAU-SOCIALMEDIA\" CUT 0 Linear RIGHT"
        },
        "delay": 0
    },
    {
        "id": "3ECcUZ2uSl",
        "label": "f0d6ZANcR:GOTO",
        "instance": "f0d6ZANcR",
        "action": "GOTO",
        "options": {
                    "channel": "2",
                    "layer": "10",
                    "offset": "2"
        },
        "delay": 1
    },
    {
        "id": "M53dtLpC0C",
        "label": "bitfocus-companion:custom_variable_set_value",
        "instance": "bitfocus-companion",
        "action": "custom_variable_set_value",
        "options": {
                    "name": "prev",
                    "value": "XXXX"
        },
        "delay": 0
    }
]

# set of action when releasing button (pressed twice) -> send to program
custom_actions_prog = [
    {
        "id": "7pB1DrUNs9",
        "label": "bitfocus-companion:custom_variable_set_value",
        "instance": "bitfocus-companion",
        "action": "custom_variable_set_value",
        "options": {
                    "name": "prog",
                    "value": "0000"
        },
        "delay": 1
    },
    {
        "id": "WGEBiPXjg-",
        "label": "f0d6ZANcR:COMMAND",
        "instance": "f0d6ZANcR",
        "action": "COMMAND",
        "options": {
                    "cmd": "PLAY 1-10 \"BANDEAU-SOCIALMEDIA\" CUT 0 Linear RIGHT"
        },
        "delay": 1
    },
    {
        "id": "Hy9IxZfaKZ",
        "label": "bitfocus-companion:bgcolor",
        "instance": "bitfocus-companion",
        "action": "bgcolor",
        "options": {
                    "color": 14818589,
                    "page": 0,
                    "bank": 0
        },
        "delay": 1
    }
]

# for titles that are not present in the excel sheet but in an external data file (ftd stored data in casparcg data directory)
# GUESTFILENAME will be replaced by stored_data_filename + number
guest_actions_preview = [
    {
        "id": "XXXXXXXXX",
        "label": "YYYYYYYYY:COMMAND",
        "instance": "YYYYYYYYY",
        "action": "COMMAND",
        "options": {
                    "cmd": "LOAD 2-10 \"BANDEAU-VIERGE\" CUT 0 Linear RIGHT"
        },
        "delay": 0
    },
    {
        "id": "3ECcUZ2uSl",
        "label": "f0d6ZANcR:GOTO",
        "instance": "f0d6ZANcR",
        "action": "GOTO",
        "options": {
                    "channel": "2",
                    "layer": "10",
                    "offset": "2"
        },
        "delay": 1
    },
    {
        "id": "M53dtLpC0C",
        "label": "bitfocus-companion:custom_variable_set_value",
        "instance": "bitfocus-companion",
        "action": "custom_variable_set_value",
        "options": {
                    "name": "prev",
                    "value": "XXXX"
        },
        "delay": 0
    },
    {
        "id": "AopqhKcHZD",
        "label": "f0d6ZANcR:CG COMMAND",
        "instance": "f0d6ZANcR",
        "action": "COMMAND",
        "options": {
                    "cmd":"CG 2-10 ADD 1 \"LOWER3RD\" 1 \"GUESTFILENAME\""
        },
        "delay": 0
    }
]

# set of action when releasing button (pressed twice) -> send to program
guest_actions_prog = [
    {
        "id": "7pB1DrUNs9",
        "label": "bitfocus-companion:custom_variable_set_value",
        "instance": "bitfocus-companion",
        "action": "custom_variable_set_value",
        "options": {
                    "name": "prog",
                    "value": "0000"
        },
        "delay": 1
    },
    {
        "id": "WGEBiPXjg-",
        "label": "f0d6ZANcR:COMMAND",
        "instance": "f0d6ZANcR",
        "action": "COMMAND",
        "options": {
                    "cmd": "PLAY 1-10 \"BANDEAU-VIERGE\" CUT 0 Linear RIGHT"
        },
        "delay": 1
    },
    {
        "id": "auyueb3gwg",
        "label": "f0d6ZANcR:CG COMMAND",
        "instance": "f0d6ZANcR",
        "action": "COMMAND",
        "options": {
                    "cmd":"CG 2-11 ADD 1 \"LOWER3RD\" 1 \"GUESTFILENAME\""
        },
        "delay": 400
    },
    {
        "id": "Hy9IxZfaKZ",
        "label": "bitfocus-companion:bgcolor",
        "instance": "bitfocus-companion",
        "action": "bgcolor",
        "options": {
                    "color": 14818589,
                    "page": 0,
                    "bank": 0
        },
        "delay": 1
    }
]

action_unlatch = {
    "id": "v9pquAbQR",
    "label": "bitfocus-companion:panic_bank",
    "instance": "bitfocus-companion",
    "action": "panic_bank",
    "options": {
        "page": 0,
        "bank": -1,
        "unlatch": True
    },
    "delay": 0
}

feedbacks_button = [
    {
        "id": "rRahML5fQ",
        "type": "variable_value",
        "instance_id": "bitfocus-companion",
        "options": {
            "variable": "internal:custom_prog",
            "op": "ne",
            "value": "0401"
        },
        "style": {
            "bgcolor": 0
        }
    },
    {
        "id": "qbbQUcxy0",
        "type": "variable_value",
                "instance_id": "bitfocus-companion",
                "options": {
                    "variable": "internal:custom_prev",
                    "op": "ne",
                    "value": "0401"
                },
        "style": {
                    "bgcolor": 0
                }
    },
    {
        "id": "jL5ybGoGu",
        "type": "variable_value",
                "instance_id": "bitfocus-companion",
                "options": {
                    "variable": "internal:custom_prev",
                    "op": "eq",
                    "value": "0401"
                },
        "style": {
                    "bgcolor": 52224
                }
    },
    {
        "id": "2MjDRu9i9",
        "type": "variable_value",
                "instance_id": "bitfocus-companion",
                "options": {
                    "variable": "internal:custom_prog",
                    "op": "eq",
                    "value": "0401"
                },
        "style": {
                    "bgcolor": 16711680
                }
    }
]

# last line in streamdeck is reserved for page up/down, page nr, index of preview/program and OUTs 
buttons_conf_last_row = {
        "25": {
            "style": "pagedown",
            "bgcolor": "0"
        },
        "26": {
            "style": "pagenum",
            "bgcolor": "0"
        },
        "27": {
            "style": "pageup",
            "bgcolor": "0"
        },
        "28": {
            "style": "png",
            "text": "$(internal:custom_prev) ",
            "size": "auto",
            "alignment": "center:center",
            "pngalignment": "center:center",
            "color": 323879,
            "bgcolor": 0,
            "latch": false,
            "relative_delay": false,
            "show_topbar": false,
            "rotary_actions": false
        },
        "29": {
            "style": "png",
            "text": "$(internal:custom_prog) ",
            "size": "auto",
            "alignment": "center:center",
            "pngalignment": "center:center",
            "color": 15073794,
            "bgcolor": 0,
            "latch": false,
            "relative_delay": false,
            "show_topbar": false,
            "rotary_actions": false
        },
        "30": {},
        "31": {
            "style": "png",
            "text": "OUT PREV",
            "size": "auto",
            "alignment": "center:center",
            "pngalignment": "center:center",
            "color": 12753048,
            "bgcolor": 5064262,
            "latch": false,
            "relative_delay": false,
            "show_topbar": "default",
            "rotary_actions": false
        },
        "32": {
            "style": "png",
            "text": "OUT",
            "size": "auto",
            "alignment": "center:center",
            "pngalignment": "center:center",
            "color": 16711680,
            "bgcolor": 14537169,
            "latch": false,
            "relative_delay": false,
            "show_topbar": "default",
            "rotary_actions": false
        }
}

# will be on button 31
actions_preview_out = [
            {
                "id": "OXjkSUqoc",
                "label": "f0d6ZANcR:CLEAR",
                "instance": "f0d6ZANcR",
                "action": "CLEAR",
                "options": {
                    "channel": "2",
                    "layer": ""
                },
                "delay": 0
            },
            {
                "id": "-vatfXuFA7",
                "label": "bitfocus-companion:custom_variable_set_value",
                "instance": "bitfocus-companion",
                "action": "custom_variable_set_value",
                "options": {
                    "name": "prev",
                    "value": "0000"
                },
                "delay": 0
            }
]

# will be on button 32. 
# TODO : call to button preview_out 31 should NOT be hardcoded
actions_program_out = [
            {
                "id": "BHC9vvMdF",
                "label": "bitfocus-companion:panic",
                "instance": "bitfocus-companion",
                "action": "panic",
                "options": {},
                "delay": 0
            },
            {
                "id": "va014XxXgI",
                "label": "f0d6ZANcR:COMMAND",
                "instance": "f0d6ZANcR",
                "action": "COMMAND",
                "options": {
                    "cmd": "PLAY 1-10 EMPTY MIX 50"
                },
                "delay": 0
            },
            {
                "id": "kMcbwaIZXq",
                "label": "f0d6ZANcR:COMMAND",
                "instance": "f0d6ZANcR",
                "action": "COMMAND",
                "options": {
                    "cmd": "PLAY 1-11 EMPTY MIX 50"
                },
                "delay": 0
            },
            {
                "id": "bnrxk_pm-",
                "label": "bitfocus-companion:custom_variable_set_value",
                "instance": "bitfocus-companion",
                "action": "custom_variable_set_value",
                "options": {
                    "name": "prog",
                    "value": "0000"
                },
                "delay": 0
            },
            {
                "id": "4t_V66caS",
                "label": "bitfocus-companion:button_pressrelease",
                "instance": "bitfocus-companion",
                "action": "button_pressrelease",
                "options": {
                    "page": 0,
                    "bank": 31
                },
                "delay": 0
            }
]
