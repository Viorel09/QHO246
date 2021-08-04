
def observed():
  observations = []

  for count in range(7):
    print("PLease enter an observation: ")
    observations.append(input())

  return observations

def run():
  print("Counting observations...")
  observations = observed()
  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)

  for data in observations_set:
    print("{} observed {} times.".format(data[0], (data[1])))

run()