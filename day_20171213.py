#!/usr/bin/env python3
"""
AoC solution day 13
2017-12-13
"""

def get_scanner_position(t, rg):
    k = t % rg
    p = t % (2 * (rg - 1))
    if p >= (rg - 1):
        return rg - (p % (rg - 1)) - 1
    else:
        return p


def calculate_severity(layers):
    print(layers)
    severity = 0
    for t in range(len(layers)):
        print('t: ', t)
        if layers[t]['wall'] == True:
            if 0 == get_scanner_position(t, layers[t]['range']):
                layers[t]['severity'] = layers[t]['range'] * t
                severity += layers[t]['range'] * t
                print(severity)

    return severity



if __name__ == '__main__':
    walls = []
    with open('data/input_data_20171213.txt', 'r') as f:
    # with open('data/test_13.txt', 'r') as f:
           for line in f:
               walls.append(line.rstrip())

    recs = [w.split() for w in walls]
    ws = []
    for w in recs:
        ls = []
        for l in w:
          ls.append(int(l.rstrip(':')))
        ws.append(ls) 

    walls = {}

    for w in ws:
        walls[w[0]] = w[1] 

    layers = [] 
    for l in range(ws[len(ws) - 1][0] + 1):
        if l in walls.keys():
            layer_status = {
                'wall': True,
                'range': walls[l],
                'severity': 0}
        else:
            layer_status = {
                'wall': False,
                'range': None,
                'severity': None}
        layers.append(layer_status)

    severity = calculate_severity(layers)
    print(severity)

