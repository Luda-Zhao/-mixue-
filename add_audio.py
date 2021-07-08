from moviepy.editor import *

videoclip_1 = VideoFileClip("tmm.mp3")
videoclip_2 = VideoFileClip("./work/result.mp4")

audio_1 = videoclip_1.audio
videoclip_3 = concatenate_videoclips([videoclip_2,videoclip_2,videoclip_2])
videoclip_3 = videoclip_3.set_audio(audio_1)

videoclip_3.write_videofile("./work/giegie.mp4", audio_codec="aac")