import json
from decimal import Decimal, ROUND_HALF_UP
import numpy as np
import cv2

class video2text:

    def __init__(self, video_path, output_path, width=None):
        self.video = cv2.VideoCapture(video_path)

        # 動画のサイズを取得
        self.video_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 動画のフレームを取得
        self.total_frame = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_rate = self.video.get(cv2.CAP_PROP_FPS)

        # 出力時のサイズを指定
        if width >= 1:
            self.ratio = (width / self.video_width)
            self.width = round(self.video_width * self.ratio)
            self.height = round(self.video_height * self.ratio / 2)
        else:
            self.width = self.video_width
            self.height = self.video_height


    def output(self):
        with open(output_path, mode="w") as f:
            for frame in range(self.total_frame):
                # 文字列の配列に変換
                img = self.image_proc(frame).astype(dtype="unicode")
                for i in range(len(img)):
                    f.writelines(img[i])
                    f.write("\n")
                f.write("end\n")
                # 進捗表示
                print(f"\r{Decimal((frame + 1) / self.total_frame * 100).quantize(Decimal("0.01"), ROUND_HALF_UP):2f}% {(str(frame + 1) + "/" + str(self.total_frame)).rjust(10)}", end="")


    def image_proc(self, frame):
        # フレーム部分を取得
        self.video.set(cv2.CAP_PROP_POS_FRAMES, frame)
        _, img = self.video.read()

        # サイズ変更
        img = cv2.resize(img, (self.width, self.height))

        # グレースケール化
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 2値化
        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        # 0と255を0と1に置き換え
        img = np.clip(img, 0, 1)

        img = 1 - img
        
        return img


if __name__ == "__main__":
    video_path = "./badapple.mp4"
    output_path = "./data.txt"
    width = 96
    v2t = video2text(video_path, output_path, width)
    v2t.output()