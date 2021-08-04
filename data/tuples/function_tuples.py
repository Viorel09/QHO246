
def likelihood():
  likelihoods = (50,38,27,99,4)
  return min(likelihoods), max(likelihoods)

def run():
  x = likelihood()
  print("Minimum likelihood of falling : {} %" .format(x[0]))
  print("Minimum likelihood of falling : {} %" .format(x[1]))
run()