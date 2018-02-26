
import serial


def ReadArduinoData(fileName):
    port = serial.Serial('COM30', 9600, timeout=1)
    print(port.name)



    file = open(fileName, 'w')
    endflag = True

    times = []
    weights = []
    amps = []
    accVoltages = []
    controlVoltages = []
    powers = []
    effectiveneses = []
    temperats = []

    port.flush()
    while endflag:
        x = port.readline()
        cortege = str(x)
        cortege = cortege[1:].replace("'","").replace('\\r\\n', '').split(' ')
        resultLine = ''
        try:
            startTime = float(cortege[0])
            startTimeMin = startTime/1000//60
            startTimeSec = startTime/1000%60
            times.append(startTime)
            weight = float(cortege[1])
            weights.append(weight)
            amp = float(cortege[2])
            amps.append(amp)
            accVoltage = float(cortege[3])
            accVoltages.append(accVoltage)
            controlVoltage = float(cortege[4])
            controlVoltages.append(controlVoltage)
            temperat = float(cortege[5])
            temperats.append(temperat)
            timeEnd = float(cortege[6])
            power = amp * accVoltage
            powers.append(power)
            if power == 0:
                power = 0.001
            effectiveness = weight / power
            effectiveneses.append(effectiveness)


            for e in cortege:
                resultLine += e
                resultLine += "\t"
                resultLine += "\n"

        except ValueError:
            continue

        resLine = "%.0f" % startTime + '\t' + "%.1f" % weight + '\t' + \
                  str(amp) + '\t' + str(accVoltage) + '\t' + \
                  str(controlVoltage) + '\t' + "%.1f" % temperat + "\t" + \
                  "%.4f" % power + '\t' + "%.4f" % effectiveness + '\n'
        print("%3d:%2.1f" % (startTimeMin, startTimeSec) + '\t' + str(weight) + '\t' + \
        str(amp) + '\t' + str(accVoltage) + '\t' + \
        str(controlVoltage) + '\t' + "%.1f" % temperat + "\t" + \
        "%.4f" % power + '\t' + "%.4f" % effectiveness + '\n')
        file.write(resLine)
        file.flush()

