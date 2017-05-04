import os

##############
#  Result 1  #
##############

# split video into frames (it has to run in my local machine since i installed the ffmpeg package locally)
# os.system('/Volumes/FFmpeg\ 85704-gcbfd44a/ffmpeg -i video/static_video1.MOV -r 1 -f image2 static_frames/%04d.png')

# image file resizing
# os.system("python batchScale.py static_frames/ new_static_frames/ scale 0.2")

# the resized files are 384 * 216
# os.system("python seam_carving.py -i new_static_frames/0001.png -r 250 200 -o resized_static_frames/0001.png")
# os.system("python seam_carving.py -i new_static_frames/0002.png -r 250 200 -o resized_static_frames/0002.png")
# os.system("python seam_carving.py -i new_static_frames/0003.png -r 250 200 -o resized_static_frames/0003.png")
# os.system("python seam_carving.py -i new_static_frames/0004.png -r 250 200 -o resized_static_frames/0004.png")
# os.system("python seam_carving.py -i new_static_frames/0005.png -r 250 200 -o resized_static_frames/0005.png")
# os.system("python seam_carving.py -i new_static_frames/0006.png -r 250 200 -o resized_static_frames/0006.png")
# os.system("python seam_carving.py -i new_static_frames/0007.png -r 250 200 -o resized_static_frames/0007.png")
# os.system("python seam_carving.py -i new_static_frames/0008.png -r 250 200 -o resized_static_frames/0008.png")
# os.system("python seam_carving.py -i new_static_frames/0009.png -r 250 200 -o resized_static_frames/0009.png")
# os.system("python seam_carving.py -i new_static_frames/0010.png -r 250 200 -o resized_static_frames/0010.png")
# os.system("python seam_carving.py -i new_static_frames/0011.png -r 250 200 -o resized_static_frames/0011.png")

# put frames together (it has to run in my local machine since i installed the ffmpeg package locally)
# os.system("/Volumes/FFmpeg\ 85704-gcbfd44a/ffmpeg -i resized_static_frames/%04d.png static_video.gif")

##############
#  Result 1  #
##############

# split video into frames (it has to run in my local machine since i installed the ffmpeg package locally)
# os.system('/Volumes/FFmpeg\ 85704-gcbfd44a/ffmpeg -i video/motion_video1.MOV -r 1 -f image2 motion_frames/%04d.png')

# image file resizing
# os.system("python batchScale.py motion_frames/ new_motion_frames/ scale 0.2")
#
# os.system("python seam_carving.py -i new_motion_frames/0001.png -r 200 250 -o resized_motion_frames/0001.png")
# os.system("python seam_carving.py -i new_motion_frames/0002.png -r 200 250 -o resized_motion_frames/0002.png")
# os.system("python seam_carving.py -i new_motion_frames/0003.png -r 200 250 -o resized_motion_frames/0003.png")
# os.system("python seam_carving.py -i new_motion_frames/0004.png -r 200 250 -o resized_motion_frames/0004.png")
# os.system("python seam_carving.py -i new_motion_frames/0005.png -r 200 250 -o resized_motion_frames/0005.png")
# os.system("python seam_carving.py -i new_motion_frames/0006.png -r 200 250 -o resized_motion_frames/0006.png")
# os.system("python seam_carving.py -i new_motion_frames/0007.png -r 200 250 -o resized_motion_frames/0007.png")
# os.system("python seam_carving.py -i new_motion_frames/0008.png -r 200 250 -o resized_motion_frames/0008.png")
# os.system("python seam_carving.py -i new_motion_frames/0009.png -r 200 250 -o resized_motion_frames/0009.png")

# put frames together (it has to run in my local machine since i installed the ffmpeg package locally)
# os.system("/Volumes/FFmpeg\ 85704-gcbfd44a/ffmpeg -i resized_motion_frames/%04d.png motion_video1.gif")


##############
#  Result 2  #
##############

# split video into frames (it has to run in my local machine since i installed the ffmpeg package locally)
# os.system('/Volumes/FFmpeg\ 85704-gcbfd44a/ffmpeg -i video/motion_video2.MOV -r 1 -f image2 motion_frames2/%04d.png')

# image file resizing
# os.system("python batchScale.py motion_frames2/ new_motion_frames2/ scale 0.2")

# os.system("python seam_carving.py -i new_motion_frames2/0001.png -r 250 200 -o resized_motion_frames2/0001.png")
# os.system("python seam_carving.py -i new_motion_frames2/0002.png -r 250 200 -o resized_motion_frames2/0002.png")
# os.system("python seam_carving.py -i new_motion_frames2/0003.png -r 250 200 -o resized_motion_frames2/0003.png")
# os.system("python seam_carving.py -i new_motion_frames2/0004.png -r 250 200 -o resized_motion_frames2/0004.png")
# os.system("python seam_carving.py -i new_motion_frames2/0005.png -r 250 200 -o resized_motion_frames2/0005.png")
# os.system("python seam_carving.py -i new_motion_frames2/0006.png -r 250 200 -o resized_motion_frames2/0006.png")
# os.system("python seam_carving.py -i new_motion_frames2/0007.png -r 250 200 -o resized_motion_frames2/0007.png")
# os.system("python seam_carving.py -i new_motion_frames2/0008.png -r 250 200 -o resized_motion_frames2/0008.png")
# os.system("python seam_carving.py -i new_motion_frames2/0009.png -r 250 200 -o resized_motion_frames2/0009.png")
# os.system("python seam_carving.py -i new_motion_frames2/0010.png -r 250 200 -o resized_motion_frames2/0010.png")
# os.system("python seam_carving.py -i new_motion_frames2/0011.png -r 250 200 -o resized_motion_frames2/0011.png")
# os.system("python seam_carving.py -i new_motion_frames2/0012.png -r 250 200 -o resized_motion_frames2/0012.png")

# put frames together (it has to run in my local machine since i installed the ffmpeg package locally)
# os.system("/Volumes/FFmpeg\ 85704-gcbfd44a/ffmpeg -i resized_motion_frames2/%04d.png motion_video2.gif")

##############
#  Result 3  #
##############

# split video into frames (it has to run in my local machine since i installed the ffmpeg package locally)
# os.system('/Volumes/FFmpeg\ 85704-gcbfd44a/ffmpeg -i video/motion_video3.MOV -r 1 -f image2 motion_frames3/%04d.png')

# image file resizing
# os.system("python batchScale.py motion_frames3/ new_motion_frames3/ scale 0.2")
#
# os.system("python seam_carving.py -i new_motion_frames3/0001.png -r 380 150 -o resized_motion_frames3/0001.png")
# os.system("python seam_carving.py -i new_motion_frames3/0002.png -r 380 150 -o resized_motion_frames3/0002.png")
# os.system("python seam_carving.py -i new_motion_frames3/0003.png -r 380 150 -o resized_motion_frames3/0003.png")
# os.system("python seam_carving.py -i new_motion_frames3/0004.png -r 380 150 -o resized_motion_frames3/0004.png")
# os.system("python seam_carving.py -i new_motion_frames3/0005.png -r 380 150 -o resized_motion_frames3/0005.png")
# os.system("python seam_carving.py -i new_motion_frames3/0006.png -r 380 150 -o resized_motion_frames3/0006.png")
# os.system("python seam_carving.py -i new_motion_frames3/0007.png -r 380 150 -o resized_motion_frames3/0007.png")
# os.system("python seam_carving.py -i new_motion_frames3/0008.png -r 380 150 -o resized_motion_frames3/0008.png")
# os.system("python seam_carving.py -i new_motion_frames3/0009.png -r 380 150 -o resized_motion_frames3/0009.png")
# os.system("python seam_carving.py -i new_motion_frames3/0010.png -r 380 150 -o resized_motion_frames3/0010.png")
# os.system("python seam_carving.py -i new_motion_frames3/0011.png -r 380 150 -o resized_motion_frames3/0011.png")
# os.system("python seam_carving.py -i new_motion_frames3/0012.png -r 380 150 -o resized_motion_frames3/0012.png")
# os.system("python seam_carving.py -i new_motion_frames3/0013.png -r 380 150 -o resized_motion_frames3/0013.png")
# os.system("python seam_carving.py -i new_motion_frames3/0014.png -r 380 150 -o resized_motion_frames3/0014.png")
# os.system("python seam_carving.py -i new_motion_frames3/0015.png -r 380 150 -o resized_motion_frames3/0015.png")
# os.system("python seam_carving.py -i new_motion_frames3/0016.png -r 380 150 -o resized_motion_frames3/0016.png")
# os.system("python seam_carving.py -i new_motion_frames3/0017.png -r 380 150 -o resized_motion_frames3/0017.png")
# os.system("python seam_carving.py -i new_motion_frames3/0018.png -r 380 150 -o resized_motion_frames3/0018.png")
# os.system("python seam_carving.py -i new_motion_frames3/0019.png -r 380 150 -o resized_motion_frames3/0019.png")

# put frames together (it has to run in my local machine since i installed the ffmpeg package locally)
# os.system("/Volumes/FFmpeg\ 85704-gcbfd44a/ffmpeg -i resized_motion_frames3/%04d.png motion_video3.gif")

# os.system("python seam_carving.py -i lotr.jpg_400x278.jpg -r 380 200 -o new_image.jpg")
# os.system("python seam_carving.py -i example1.png -r 405 200 -o issue_example1_result2.png.png")
