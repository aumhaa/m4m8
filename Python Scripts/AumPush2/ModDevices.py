
ENDCODER_BANK_CONTROL1 = ['ModDevice_knob0', 'ModDevice_knob1', 'ModDevice_knob2', 'ModDevice_knob3']
ENDCODER_BANK_CONTROL2 = ['ModDevice_knob4', 'ModDevice_knob5', 'ModDevice_knob6', 'ModDevice_knob7']
ENDCODER_BANKS = {'NoDevice':[['CustomParameter_'+str(index+(bank*24)) for index in range(8)] + ENDCODER_BANK_CONTROL1 for bank in range(8)] + [['CustomParameter_'+str(index+((bank)*24)) for index in range(8)] + ENDCODER_BANK_CONTROL2 for bank in range(4,8)]}

MOD_BANK_DICT = {'EndCoders':['']}

MOD_TYPES = {'EndCoders':ENDCODER_BANKS}

MOD_CNTRL_OFFSETS = {}
