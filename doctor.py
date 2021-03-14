import math
def calculateBMR(age, sex, height, weight):
  '''
  Age in years
  sex 0 = female, 1 = male
  height in cm
  weight in Kg

  '''
  bmr = 0
  if sex:
    bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
  else:
    bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
  return bmr

def bmrToCaloriesNeeded(bmr,activity):
  '''
  activity to be measures on scale of 0 to 4 (or 1 to 5)
  0 being least exercise and stuff
  4 being means very active exercise
  '''
  a=0
  if activity==4:
    a=1.9
  elif activity==3:
    a=1.725
  elif activity==2:
    a=1.55
  elif activity==1:
    a=1.375
  else:
    a=1.2
  return bmr*a

def ratingCalorie(calorieIntake,calorieNeeded):
  '''
  gives rating at scale of 0 to 1
  1 = excellent
  0 = poor
  takes calorieIntake and calorieNeeded
  calorieIntake is the total calorie consumed till that point.
  ''' 
  rating=0;
  calR2,calR1=calorieNeeded*105/100,calorieNeeded*95/100
  if(calorieIntake>calR1 and calorieIntake<calR2):
    rating = 1
  else:
    dR1,dR2=abs(calR1-calorieIntake),abs(calR2-calorieIntake)
    dR=min(dR1,dR2)
    r= calR1 if dR==dR1 else calR2
    rating=1 - sigmoid(dR/r)
  return rating

def calorieQuota(calorieIntake,calorieNeeded):
  '''
  Returns how much calorie can be consumed more
  -1 means Over the limit, dont eat (fast)
  any other value means that much calorie can be taken more.
  '''
  if(calorieIntake>=calorieNeeded*105/100):
    return -1
  else:
    return calorieNeeded*105/100-calorieIntake

def sigmoid(x,s=4):
  return (1+math.e**(-x*s))**-1*2 - 1