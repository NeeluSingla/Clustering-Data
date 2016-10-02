import math
import collections
import sys



def CalculatingDistance(dataFileName, number_of_clusters, iter, initial_point_file):
    initial_data_array=[]
    all_data_array = []
    buckets={}
    file=open(initial_point_file)
    for k in range(number_of_clusters):
        list_temp = []
        initial_data_array.append(file.readline().split(','))
        list_temp.append(initial_data_array[k])
        buckets[k] = list_temp
    f = open(dataFileName, "r")
    for line in f:
        all_data_array.append(line.replace('\n','').split(','))

    for index in range(iter):
        for data_point in all_data_array:
            min = float(99999999999)
            point = 0
            count = 0
            for initial_point in initial_data_array:
                d = (float(data_point[0]) - float(initial_point[0]))**2 + (float(data_point[1]) - float(initial_point[1]))**2 +(float(data_point[2]) - float(initial_point[2]))**2+(float(data_point[3]) - float(initial_point[3]))**2
                d = math.sqrt(d)
                if d < min :
                    min  = d
                    point = count
                count = count + 1
            buckets[point].append(data_point)

        pointer = 0

        for list in buckets:
            x=float(0)
            y=float(0)
            z=float(0)
            t=float(0)
            for item in buckets.get(list):
                x = x + float(item[0])
                y = y + float(item[1])
                z = z + float(item[2])
                t = t + float(item[3])
            initial_data_array[list][0] = x/len(buckets.get(list))
            initial_data_array[list][1] = y/len(buckets.get(list))
            initial_data_array[list][2] = z/len(buckets.get(list))
            initial_data_array[list][3] = t/len(buckets.get(list))
            if index != iter-1:
                buckets.get(list).clear()
                buckets.get(list).append(initial_data_array[list])

    finalvalue = 0
    for list in buckets:
        dict = {}
        for item in buckets.get(list):
            if not initial_data_array.__contains__(item):
                name = item[4]
                if dict.__contains__(name) :
                    dict[name].append(item)
                else:
                    list=[]
                    list.append(item)
                    dict[name] = list
        max = -99
        name = ''
        for data in dict:
            if len(dict.get(data)) > max :
                max = len(dict.get(data))
                name = data

        finalvalue = finalvalue + max
        print('cluster ' + name)
        print('\n')
        dict = collections.OrderedDict(sorted(dict.items()))
        for data in dict:
            for g in dict.get(data):
                print(g)
        print('\n')

    j = len(all_data_array)-finalvalue
    print('Numberofpointsassignedtowrongcluster:' +str(j) )





















if __name__=='__main__':
	dataFileName=sys.argv[1]
	number_of_clusters=int(sys.argv[2])
	iter=int(sys.argv[3])
	initial_point_file=sys.argv[4]

CalculatingDistance(dataFileName, number_of_clusters, iter, initial_point_file)