import os,glob,pickle


video_files = glob.glob(os.path.join('data', '*', '*.mp4'))
videos_exist = set()
for video in video_files:
        items = video.split('/')
        vid = items[-1][-15:-4]
        classname = items[-2]
        videos_exist.add((vid, classname))

fw = open('DONE.txt','wb')
# Pickle the list using the highest protocol available.
pickle.dump(videos_exist, fw, -1)
fw.close()

