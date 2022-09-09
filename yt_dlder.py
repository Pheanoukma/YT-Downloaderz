from pytube import youtube

banner = """

    Youtube video downloader 

          v.2

Made by : Pheanoukmma

    github : github.com/pheanoukma

"""

bruh = input("Input the path for video save :")

SAVE_PATH = (bruh)

link=open(' files.txt','r')

for i in link:

    try:

        

    YT = YouTube(i)

    except:

        print("connection error (check ur internet)")

    mp4files = YT.filter('mp4')

    d_video = YT.get(mp4files[-1].extension,mp4files[-1].resolution)

    try : 

        d_video.download(SAVE_PATH)

    except : 

        print("AN ERROR OCCURED, Try again later")

print('Video downloaded!')   
