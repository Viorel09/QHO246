
def observed():
  observations = []
  for count in range(5):
    print("Please enter an observation: ")
    observations.append(input())

  return observations

def remove_observations(observations):
  linerun = True

  while(linerun):
    print("Do you wish to remove an observation (yes/no)?")
    response = input()

    if(response == "yes"):
      print("Please enter the observation you wish to remove")
      observation = input()
      observations.remove(observation)
    else:
      linerun = False

def run():
  observations = observed()
  remove_observations(observations)

  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))

    observations_set.add(data)

  for data in sorted(observations_set):
    print("{} observed {} times." .format(data[0], (data[1])))

run()