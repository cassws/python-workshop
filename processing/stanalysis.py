from starTrekS01E01and02 import STscript
with open('starTrekOutput.txt', 'a') as st:
    st.write('script=[')
lines = STscript.splitlines()
for line in lines:
    if "***" not in line:
        outParts = (line.split(': '))
        output = outParts[0] + ': ' + outParts[1]
        with open('starTrekOutput.txt', 'a') as st:
            st.write('"' + output + '",\n')

with open('starTrekOutput.txt', 'a') as st:
    st.write(']')
