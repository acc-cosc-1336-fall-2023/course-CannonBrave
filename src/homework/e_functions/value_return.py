
def get_hour(epoch_seconds):
   result = int (epoch_seconds / 3600)
   return result

def get_minutes(epoch_seconds):
   result = epoch_seconds % 3600
   result = int(result/60)
   return result

def get_seconds(epoch_seconds):
   result = epoch_seconds % 3600
   result = int(result % 60)
   return result

