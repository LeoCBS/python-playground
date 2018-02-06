# pipeline.py
#
# An example of setting up a processing pipeline with generators

access_log = "ausdhuash test auhsd aushdua ahduasd auhdu uhasd"


def grep(pattern,lines):
    for line in lines:
        if pattern in line:
             yield line

if __name__ == '__main__':
    from follow import follow

    # Set up a processing pipe : tail -f | grep python
    loglines = follow(access_log)
    pylines  = grep("python",loglines)

    # Pull results out of the processing pipeline
    for line in pylines:
        print(line)