import os
import time

# 音声を鳴らさないプレーヤー

class videoplayer:
    def __init__(self, file_path, fps):
        self.data_path = file_path
        self.fps = fps
        

    def play(self):
        self.start_time = time.perf_counter()
        with open(self.data_path, mode="r") as f:
            os.system("cls")
            self.frame = 0
            while True:
                try:
                    self.draw_terminal(next(f), self.frame)
                except StopIteration:
                    break

    def draw_terminal(self, string, frame):
        if "end\n" != string:
            for i in string:
                if i == "0":
                    print("\033[47m \033[0m", end="")
                elif i == "1":
                    print("\033[40m \033[0m", end="")
            print()
        else:
            self.wait_fps(frame + 1)
            print("\r\033[1024A", end="")
            self.frame += 1
    

    def wait_fps(self, next_frame):
        while True:
            if (time.perf_counter() - self.start_time) >= (1 / self.fps * next_frame):
                break



if __name__ == "__main__":
    file_path = "./data.txt"
    vp = videoplayer(file_path, 30)
    vp.play()