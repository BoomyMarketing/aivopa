# fix CP1251-mangled UTF-8 special characters in batch 23 pages
files = [
    'industries/hair-salon.html',
    'industries/driving-school.html',
    'industries/addiction-treatment.html',
    'industries/waterproofing.html',
    'industries/immigration-lawyer.html'
]

replacements = [
    # em dash U+2014 (E2 80 94) mangled via CP1251 -> D0B2 D082 E2809D
    (bytes([0xD0,0xB2,0xD0,0x82,0xE2,0x80,0x9D]), bytes([0xE2,0x80,0x94])),
    # en dash U+2013 (E2 80 93) mangled -> D0B2 D082 E2809C
    (bytes([0xD0,0xB2,0xD0,0x82,0xE2,0x80,0x9C]), bytes([0xE2,0x80,0x93])),
    # right single quote U+2019 (E2 80 99) mangled -> D0B2 D082 E284A2
    (bytes([0xD0,0xB2,0xD0,0x82,0xE2,0x84,0xA2]), bytes([0xE2,0x80,0x99])),
    # left single quote U+2018 (E2 80 98) mangled -> D0B2 D082 CB9C
    (bytes([0xD0,0xB2,0xD0,0x82,0xCB,0x9C]),       bytes([0xE2,0x80,0x98])),
]

for f in files:
    with open(f, 'rb') as fp:
        data = fp.read()
    n0 = len(data)
    count = 0
    for bad, good in replacements:
        c = data.count(bad)
        if c:
            data = data.replace(bad, good)
            count += c
    with open(f, 'wb') as fp:
        fp.write(data)
    print('%s: fixed %d chars, %d -> %d bytes' % (f, count, n0, len(data)))
