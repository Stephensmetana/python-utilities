  
# I copied code from here https://www.programiz.com/python-programming/datetime/current-datetime
# TODO it would be nice to support an argument which specifies the timezone instead of hardcoding UTC
def getDateTime():
  from datetime import datetime, timezone
  # datetime object containing current date and time
  now = datetime.now(timezone.utc)
  # dd/mm/YY H:M:S
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  dt_string += " UTC"
  return dt_string

# This is similar to the code above except that slashes have been replaced with dashes to make it safe for filenames
def getDateTimeFormatedForFilename():
  from datetime import datetime, timezone
  # datetime object containing current date and time
  now = datetime.now(timezone.utc)
  dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
  dt_string += "_UTC"
  return dt_string

# Converts from seconds to hours, minutes, seconds - this is a wrapper for existing libraries 
def get_time_hh_mm_ss(seconds):
    from datetime import timedelta
    td = timedelta(seconds=seconds)
    return td

# Note: This assumes that there are only images and .txt and .log files in the directory
# A better implementation would be to have an argument that accepts a list of file extentions to count
def countNumberOfImagesInFolder(folder):
  import os
  count = 0
  # Iterate directory
  for f in os.listdir(folder):
      # check if current path is a file and also not a .txt file
      if (os.path.isfile(os.path.join(folder, f)) and not f.lower().endswith(".txt") and not f.lower().endswith(".log")):
          count += 1
  return count

#In Linux, if you use echo to write to a file echoing parentheses or & causes problems so we are using backslash to escape these characters before trying to echo them to a file
def reformatToSafeString(inputString):
  return inputString.replace("(", "\(").replace(")", "\)").replace("&", "\&")

"""" I dont know how to write google colab code that invokes the shell in a python file without a syntax error so this code is commented out for now

# This function assumes it is being called within Google Colab - it will likely not work anywhere else 
def writeToFile(filename, text):
  ! echo {text} >> {filename}

# This function assumes it is being called within Google Colab - it will likely not work anywhere else 
def clearFile(filename):
   ! echo "" > {filename}

# This function assumes it is being called within Google Colab - it will likely not work anywhere else 
def writeLineToFile(filename):
  ! echo "==============================" >> {filename}
"""