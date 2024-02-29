from g4f import set_cookies

set_cookies(".bing.com", {
    "_U":  "1BJKrxJSYb_YE84Wl6aSsND-uQ_MsiZT1IFjQkseVxDuhpWMN5cREP4wRq>
})

#from g4f.gui import run_gui
from g4f.api import run_api

#run_gui("0.0.0.0", 8080, debug=True)
run_api()
