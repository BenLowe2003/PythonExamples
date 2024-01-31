
from math import floor


class space(self, field, length, resolution):
    self.field = field
    self.length = length
    self.area = length ** 2
    self.volume = length ** 3
    self.resolution = resolution
    self.array_length = length * resolution
    
    def step(self, dt, c):
        initial_field = self.field
        new_field = initial_field
        resolution = self.resolution
        length = self.length
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    dl = 1/resolution
                    
                    conv_i = [(i + a - 1) if 1 <= (i + a) <= length else ((length - 1) if (i + a) < 1 else 0) for a in range(3)]
                    conv_j = [(j + a - 1) if 1 <= (j + a) <= length else ((length - 1) if (j + a) < 1 else 0) for a in range(3)]
                    conv_k = [(k + a - 1) if 1 <= (k + a) <= length else ((length - 1) if (k + a) < 1 else 0) for a in range(3)]
                     
                    x_2nd_der = (initial_field[i+1][j][k] - initial_field[i-1][j][k] - 2 * initial_field[i][j][k]) / dl ** 2
                    y_2nd_der = (initial_field[i][j+1][k] - initial_field[i][j-1][k] - 2 * initial_field[i][j][k]) / dl ** 2
                    z_2nd_der = (initial_field[i][j][k+1] - initial_field[i][j][k-1] - 2 * initial_field[i][j][k]) / dl ** 2
                    
                    new_field[i][j][k] = (c ** 2) * (x_2nd_der + y_2nd_der + z_2nd_der)
        self.field = new_field
        return self
    
    def initialise_field(self, function):
        array_object = [ [ [0] * self.length for _ in range(self.length)] for _ in range(self.length)]
        for i in range(self.length):
            for j in range(self.length):
                for k in range(self.length):
                    x = i * 1/resolution
                    y = j * 1/resolution
                    z = k * 1/resolution
                    array_object[i][j][k] = function(x,y,z)
        self.field = array_object
        return self
                    

def compute_wave_solutions(initial_conditions, size, spacial_resolution, time, temporal_resolution, c):
    num_steps = floor(time / temporal_resolution)
    num_field_elements = floor(size * spacial_resolution)
    field_space = space(Null, size, spacial_resolution)
    field_space = field_space.initialise_field(initial_conditions)
    for t in range(num_steps):
        field_space = field_space.step(temporal_resolution, c)
    return field_space.field

 
def linear_function(x,y,z):
    return x*y*z




    
