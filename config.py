# Tumblr Setup
# Replace the values with your information
# OAuth keys can be generated from https://api.tumblr.com/console/calls/user/info
consumer_key='ShbOqI5zErQXOL7Qnd5XduXpY9XQUlBgJDpCLeq1OYqnY2KzSt' #replace with your key
consumer_secret='ulZradkbJGksjpl2MMlshAfJgEW6TNeSdZucykqeTp8jvwgnhu' #replace with your secret code
oath_token='uUcBuvJx8yhk4HJIZ39sfcYo0W4VoqcvUetR2EwcI5Sn8SLgNt' #replace with your oath token
oath_secret='iNJlqQJI6dwhAGmdNbMtD9u7VazmX2Rk5uW0fuIozIEjk97lz4' #replace with your oath secret code
tumblr_blog = 'soniaetjeremie' # replace with your tumblr account name without .tumblr.com
tagsForTumblr = "photobooth" # change to tags you want, separated with commas

#Config settings to change behavior of photo booth
monitor_w = 800    # width of the display monitor
monitor_h = 480    # height of the display monitor
file_path = '/home/pi/photobooth/pics/' # path to save images
clear_on_startup = False # True will clear previously stored photos as the program launches. False will leave all previous photos.
debounce = 0.3 # how long to debounce the button. Add more time if the button triggers too many times.
post_online = True # True to upload images. False to store locally only.
capture_count_pics = True # if true, show a photo count between taking photos. If false, do not. False is faster.
make_gifs = True   # True to make an animated gif. False to post 4 jpgs into one post.
hi_res_pics = False  # True to save high res pics from camera.
                    # If also uploading, the program will also convert each image to a smaller image before making the gif.
                    # False to first capture low res pics. False is faster.
                    # Careful, each photo costs against your daily Tumblr upload max.
camera_iso = 400    # adjust for lighting issues. Normal is 100 or 200. Sort of dark is 400. Dark is 800 max.
                    # available options: 100, 200, 320, 400, 500, 640, 800