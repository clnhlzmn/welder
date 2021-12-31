i = 0.000001
t_max = 0.02
i_max = int(t_max / i)

p_sw = int(0.0001 / i)
p_ac = int(0.01 / i)
ac_duty = 0.5

v_out = 15
v_in = 48
sw_duty = v_out / v_in
sw_on = int(p_sw * sw_duty)

sw_state = 0
ac_state = 0

with open('pwl.txt', 'w+') as out:
    on_time = 0
    for t in range(i_max):
        # Count duration that switch is on
        if sw_state:
            on_time = on_time + 1
        
        # If it's on long enough turn it off
        if on_time == sw_on:
            sw_state = 0
            on_time = 0
        
        # If its switch period time turn the switch on
        if t % p_sw == 0:
            sw_state = 1
        
        # Alternate ac state
        if t % (p_ac / 2) == 0:
            ac_state = not ac_state
        
        
        output = 48 if sw_state else 0
        output = output if ac_state else -output
        out.write("{} {}\n".format(t * i, output))
