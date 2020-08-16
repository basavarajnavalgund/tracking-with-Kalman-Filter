import pandas as pd

#covariance(x, y) = summation[(x-xbar)(y-ybar)] / n
  
df = pd.read_csv("data/lidar1.txt",
                             sep="\t",
                             header=0,
                             names=["px", "py", "gpx", "gpy"])

print('\n\tLiDAR')
print('\n')
v = df.cov()
print(v)


print('\n\tRADAR')
print('\n')


df = pd.read_csv("data/radar1b.txt",
                             sep="\t",
                             header=0,
                             names=["rho", "phi", "rdot"])

v = df.cov()
print(v)

df = pd.read_csv("data/radar1.txt",
                             sep="\t",
                             header=0,
                             names=["px", "py", "gpx", "gpy"])

v = df.cov()
print(v)


df = pd.read_csv("data/radar1a.txt",
                             sep="\t",
                             header=0,
                             names=["vx", "vy", "gvx", "gvy"])


v = df.cov()
print(v)



print('\n\tWith residual\n\tLiDAR\n')

df = pd.read_csv("data/1lidar.txt",
                             sep="\t",
                             header=0,
                             names=["px", "py", "respx", "respy"])

v = df.cov()
print(v)







