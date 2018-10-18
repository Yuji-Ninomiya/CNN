# -*- coding: utf-8 -*-

import argparse

import cv2


def movie_to_image(num_cut):


    # キャプチャ動画読み込み（キャプチャ構造体生成）
    capture = cv2.VideoCapture(video_path)

    img_count = 0  # 保存した候補画像数
    frame_count = 0  # 読み込んだフレーム画像数

    cv2.namedWindow('video_frame', cv2.WINDOW_NORMAL)
    cv2.namedWindow('saved_frame', cv2.WINDOW_NORMAL)

    # フレーム画像がある限りループ
    while(capture.isOpened()):
         # フレーム画像一枚取得
        ret, frame = capture.read()
        if ret == False:
            break

        # 指定した数だけフレーム画像を間引いて保存
        if frame_count % num_cut == 0:
            img_file_name = image_path + str(img_count) + ".jpg"
            cv2.imwrite(img_file_name, frame)
            img_count += 1

        frame_count += 1

    # キャプチャ構造体開放
    capture.release()


if __name__ == '__main__':


    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required = True, help = "Path to the video")
    args = vars(ap.parse_args())

    video_path = args["video"]
    image_path = 'images/'


    # 間引き数を10にしてフレーム画像抽出
    movie_to_image(int(10))