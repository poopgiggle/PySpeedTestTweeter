This is a script that I wrote to track (and tweet) Internet upload/download speeds.

To install this, first install requirements:

    pip install -r requirements.txt

Create a file called `pyspeedtestconfig.py` that has all your Twitter API OAuth keys, timezone information,
and logfile location in it. The format should be pretty self-explanatory.

Then set a cronjob to run `speedtester.py` however often you want to run it. Or run it some other way. I
didn't really put a whole lot of thought into this.
