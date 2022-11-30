# Notes for battery housing design

units = 'mm'
l, w, h = 'l', 'w', 'h'
batt_dimms = {
    l: 89.9 * 2,
    w: 70.31,
    #    h: 101.1
} # dimms for actual battery walls

inner_offset = 1.0

wall_width = 5.0

outer_dimms = {}

for key in batt_dimms:
    print(f'{key}: {batt_dimms[key]+1}')
    outer_dimms[key] = batt_dimms[key] + wall_width + inner_offset
    print(f'---> {outer_dimms[key]}')

# print(outer_dimms)

