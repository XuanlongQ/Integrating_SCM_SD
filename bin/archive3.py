# import numpy as np
# import matplotlib.pyplot as plt

# # read the data from the CSV file
# data = np.genfromtxt('Integrating_SCM_SD/bin/output/var_covar/dimensions.csv', delimiter=',')

# # get the warmth and competence rows
# warmth = data[1,1:]
# competence = data[2,1:]
# status = data[6,1:]

# def cal_dimension_variance(data):
#     # Calculate the variance of each vector
#     variance_v1 = np.var(data)
#     print(f"Variance of data: {variance_v1}")
    
# # Calculate the covariance between the two vectors  
# def cal_dimension_cov(a,b):
#     # To calculate the covariance between the two vectors, we stack them and use np.cov
#     # Note that np.cov returns a covariance matrix  
#     covariance_matrix = np.cov(a,b)
#     print("Covariance matrix between the two vectors:")
#     print(covariance_matrix)

#     # The covariance between the two vectors is the off-diagonal element of the covariance matrix
#     covariance_v1_v2 = covariance_matrix[0, 1]
#     print(f"Covariance between vector 1 and vector 2: {covariance_v1_v2}")

# # Calculate the variance of each vector
# variance_w = cal_dimension_variance(warmth)
# variance_c = cal_dimension_variance(competence)
# variance_s = cal_dimension_variance(status)

# covariance_matrix_w_s = cal_dimension_cov(warmth,status)
# covariance_matrix_c_s = cal_dimension_cov(competence,status)
# print(covariance_matrix_w_s)
# print(covariance_matrix_c_s)

# # Plot two subpictures in one picture
# plt.figure(figsize=(10, 8))

# # Subplot 1: Scatter plot of warmth and competence
# plt.subplot(1, 2, 1)
# plt.scatter(warmth, competence, alpha=0.6)
# plt.xlabel('Warmth')
# plt.ylabel('Competence')
# plt.title('Scatter plot of Warmth and Competence')

# # Subplot 2: Scatter plot of warmth and status
# plt.subplot(1, 2, 2)
# plt.scatter(warmth, status, alpha=0.6)
# plt.xlabel('Warmth')
# plt.ylabel('Status')
# plt.title('Scatter plot of Warmth and Status')

# plt.tight_layout()  # Adjust the spacing between subplots
# plt.show()


# plt.figure(figsize=(10, 8))
# plt.scatter(warmth, competence,alpha=0.6)
# plt.show()



#=======
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the cosine similarities
cos_sim_w_c = 0.65
cos_sim_w_e = 0.74
cos_sim_c_e = 0.63

# Calculate the angles based on cosine similarities
angle_w_c = np.arccos(cos_sim_w_c)
angle_w_e = np.arccos(cos_sim_w_e)
angle_c_e = np.arccos(cos_sim_c_e)

# Define the "warmth" vector along the x-axis
warmth = np.array([1, 0, 0])

# Define the "competence" vector in the x-y plane with the calculated angle from the "warmth" vector
competence = np.array([np.cos(angle_w_c), np.sin(angle_w_c), 0])

# We already know the x-component of the "evaluation" vector
eval_x = cos_sim_w_e

# The y-component and z-component can be determined using the following system of equations:
# competence_x * eval_x + competence_y * eval_y = cos_sim_c_e
# eval_x^2 + eval_y^2 + eval_z^2 = 1 (since we are assuming unit vectors)

# Solve for eval_y using the first equation
eval_y = (cos_sim_c_e - competence[0] * eval_x) / competence[1]

# Solve for eval_z using the second equation, considering both positive and negative roots
eval_z_possible = 1 - eval_x**2 - eval_y**2
if eval_z_possible < 0:
    raise ValueError("The vectors with the given cosine similarities cannot exist in 3D space.")

eval_z_pos = np.sqrt(eval_z_possible)

# Choose the positive root for the "evaluation" vector
evaluation = np.array([eval_x, eval_y, eval_z_pos])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to plot the projections of vectors onto the planes
def plot_vector_projections(ax, vector, color):
    # Project onto the x-axis
    ax.plot([vector[0], vector[0]], [0, vector[1]], [0, vector[2]], color=color, linestyle='dashed', linewidth=1)
    # Project onto the y-axis
    ax.plot([0, vector[0]], [vector[1], vector[1]], [0, vector[2]], color=color, linestyle='dashed', linewidth=1)
    # Project onto the z-axis
    ax.plot([0, vector[0]], [0, vector[1]], [vector[2], vector[2]], color=color, linestyle='dashed', linewidth=1)

# Plot the vectors
ax.quiver(0, 0, 0, warmth[0], warmth[1], warmth[2], color='r', label='Warmth')
ax.quiver(0, 0, 0, competence[0], competence[1], competence[2], color='g', label='Competence')
ax.quiver(0, 0, 0, evaluation[0], evaluation[1], evaluation[2], color='b', label='Evaluation')

# Plot the projections
plot_vector_projections(ax, warmth, 'r')
plot_vector_projections(ax, competence, 'g')
plot_vector_projections(ax, evaluation, 'b')

# Set the axes limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add a legend
ax.legend()

# Show the plot
plt.show()


#######
import numpy as np

# Define the vectors as per the previous example
warmth = np.array([1, 0, 0])
competence = np.array([np.cos(angle_w_c), np.sin(angle_w_c), 0])
evaluation = np.array([eval_x, eval_y, eval_z_pos])

# Calculate the normal vector of the warmth-competence plane
# Since this is a 2D plane in a 3D space, and we know it's perpendicular to the z-axis,
# we can define the normal vector as [0, 0, 1] for simplicity.
normal_vector = np.array([0, 0, 1])

# Calculate the angle between the "evaluation" vector and the normal vector
# This angle is complementary to the angle between the "evaluation" vector and the plane.
angle_between = np.arccos(np.dot(evaluation, normal_vector) / (np.linalg.norm(evaluation) * np.linalg.norm(normal_vector)))

# Since the dot product gives the cosine of the angle between the vector and the normal to the plane,
# we need to subtract this angle from 90 degrees (or π/2 radians) to get the angle between the vector and the plane.
angle_with_plane = np.pi/2 - angle_between

# Convert the angle to degrees for a more intuitive understanding
angle_with_plane_degrees = np.degrees(angle_with_plane)

print(f"Angle between 'evaluation' dimension and 'warmth-competence' plane: {angle_with_plane_degrees:.2f} degrees")