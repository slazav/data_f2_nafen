import numpy

def sweep_packer(file):
    data = file.readlines()
    packed_data = {'Date': [], 'Time': [], 'Date_Time_Num':[], 'Freq': [], 'Vx': [], 'Vy': []}

    date,time,date_time_num = [], [], []
    for ind in range(0, len(data)):

        line = data[ind]

        if line[0:4] == 'freq':

            if ind == 0:

                sweep_number = 1

                freq, vx, vy = [], [], []
                date.append(line[21:31])
                time.append(line[32:40])
                date_time = numpy.datetime64(line[27:31]+'-'+line[24:26]+'-'+line[21:23] + 'T' + line[32:40])
                date_time_num.append(date_time.astype(int))
            else:
                sweep_number = sweep_number + 1


                packed_data['Freq'].append(numpy.array(freq))
                packed_data['Vx'].append(numpy.array(vx))
                packed_data['Vy'].append(numpy.array(vy))
                freq, vx, vy = [], [], []
                date.append(line[21:31])
                time.append(line[32:40])
                date_time = numpy.datetime64(line[27:31]+'-'+line[24:26]+'-'+line[21:23] + 'T' + line[32:40])
                date_time_num.append(date_time.astype(int))

        elif ind == len(data)-1:
            packed_data['Freq'].append(numpy.array(freq))
            packed_data['Vx'].append(numpy.array(vx))
            packed_data['Vy'].append(numpy.array(vy))


        else:
            data_line = line.split()
            freq.append(float(data_line[0]))
            vx.append(float(data_line[1]))
            vy.append(float(data_line[2]))


    packed_data['Date'] = date
    packed_data['Time'] = time
    packed_data['Date_Time_Num'] = numpy.array(date_time_num)
    return packed_data

