
from g4f import set_cookies

set_cookies(".bing.com", {
    "_U":  "1BJKrxJSYb_YE84Wl6aSsND-uQ_MsiZT1IFjQkseVxDuhpWMN5cREP4wRqWCUzVzFgTjGwzDQch8yeVEuXn6SGNJrvxKwFEMb40nr95q9DNhibNJKXX__E03dURgBT-O6g1_oKu1oveDs-Mp3Nim0EsgCqI8Fj4zsHts2bHsWf9_AewfifC4RkWzNt-4Gxs1d6zq4CUBjxzvJefrQDuxo2LV86mqJ9Zst1pZt_2jiuIQ"
})

#from g4f.gui import run_gui
from g4f.api import run_api

#run_gui("0.0.0.0", 8080, debug=True)
run_api()
