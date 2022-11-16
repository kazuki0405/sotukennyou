import csv
import os
from statistics import mean

ROOT_PATH = "C:\sample\Dataset"



#配列宣言
class CSV_Load():
    def __init__(self):
        self.Start = []
        self.End = []
        self.Start_Square = [[0] * 220 for i in range(3460)]
        self.End_Square = [[0] * 220 for i in range(3460)]
        self.Pitch = []
        self.Intensity = []
        self.Start_Time = []
        self.End_Time = []
        self.Pitch_List = []
        self.Intensity_List = []
        self.Pitch_Square = [[0] * 220 for i in range(3460)]
        self.Intensity_Square = [[0] * 220 for i in range(3460)]
        self.cnt = 0
        self.i = 0
        self.j = 0

    #csvファイルを指定
    def process(self, file_path):

        #csvファイルを読み込み
        with open(file_path) as f:

            reader = csv.reader(f)

            #csvファイルのデータをループ
            for i in range(3460):
                for row in reader:
                    
                    #Start[row].append(str(row[0]))

                    #End[row].append(str(row[1]))

                    #A列を配列へ格納
                    self.Pitch.append(str(row[2]))

                    #B列を配列へ格納
                    self.Intensity.append(str(row[3]))


        target1 = "--undefined--"
        target2 = "Pitch[Hz]"
        target3 = "intensity[dB]"
        target4 = "s_t[s]"
        target5 = "e_t[s]"
        self.Pitch = [item for item in self.Pitch if item != target1]
        self.Pitch = [item for item in self.Pitch if item != target2]
        self.Intensity = [item for item in self.Intensity if item != target1]
        self.Intensity = [item for item in self.Intensity if item != target3]
        self.Start = [item for item in self.Start if item != target4]
        self.End = [item for item in self.End if item != target5]

        self.Start = list(map(float, self.Start))
        self.End = list(map(float, self.End))
        self.Pitch = list(map(float, self.Pitch))
        self.Intensity = list(map(float, self.Intensity))

        Pitch_mean = mean(self.Pitch)
        Intensity_mean = mean(self.Intensity)

        self.Pitch_List.append(Pitch_mean)
        self.Intensity_List.append(Intensity_mean)

        self.Pitch_Square[self.i][self.j] = Pitch_mean
        self.Intensity_Square[self.i][self.j] = self.Intensity_List
        print(self.cnt)
        print(self.Pitch_Square)

        """for i in range(3460):
            for j in range(220):
                Start_Square[i][j] = Start
                End_Square[i][j] = End"""


    def recursive_file_check(self, path):
        a = CSV_Load()
        
        if os.path.isdir(path):
            print(self.cnt)
            self.cnt += 1
            self.i += 1
            # directoryだったら中のファイルに対して再帰的にこの関数を実行
            files = os.listdir(path)
            for file in files:
                a.recursive_file_check(path + "\\" + file)

        else:
            # fileだったら処理
            a.process(path)

m = CSV_Load()

m.__init__()

m.recursive_file_check(ROOT_PATH)
