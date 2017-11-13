from buffydata import script
i = 0
lines = script.splitlines()
with open('buffyS01E01.txt', 'a') as buffy:
    buffy.write('script=[')
for line in lines:
    if ":" in line[0:15]:
        outParts = (line.split(':  '))
        output = outParts[0] + ': ' + outParts[1]
        print(output)
        with open('buffyS01E01.txt', 'a') as buffy:
            buffy.write('"' + output + '",\n')
        i+= 1
    else:
        continue
with open('buffyS01E01.txt', 'a') as buffy:
    buffy.write(']')