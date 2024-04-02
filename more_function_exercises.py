
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp * (5/9) + 32
  return f_temp


print("32°F in Celsius:", f_to_c(32))  
print("0°C in Fahrenheit:", c_to_f(0)) 

def get_force(mass, acceleration):
  force = mass * acceleration
  return force

print("The GE train supplie " + str(get_force(train_mass, train_acceleration)) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
  energy = mass * c**2
  return energy
print("A 1kg bomb supplies " + str(get_energy(bomb_mass)) + " Joules")

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")
