
import numpy as np
import graphics as gr
import copy
import random as rand

innit_conditions = [ {"i" : 0, "position" : np.array([0.0,1.0]), "velocity" : np.array([1, 0.5]), "mass" : 1.0},
                     {"i" : 1, "position" : np.array([0.0,-1.0]), "velocity" : np.array([-1.5, 0.5]), "mass" : 1.0},
                     {"i" : 2, "position" : np.array([1.0,0.0]), "velocity" : np.array([0.5, -0.1]), "mass" : 1.0},]

system_one = [  {"i" : 0, "position" : np.array([0.0,1.0]), "velocity" : np.array([(1/(np.pi)), 0.0]), "mass" : 1.0},
             {"i" : 1, "position" : np.array([0.0,-1.0]), "velocity" : np.array([-(1/(np.pi)), 0.0]), "mass" : 1.0},]

def innit_random(n = 2):
    innit_conditions = [{"i" : None, "position" : np.array([None,None]), "velocity" : np.array([None, None]), "mass" : None} for i in range(n+1)] 
    # Random particles 
    for i in range(n):
        innit_conditions[i]["i"] = i
        innit_conditions[i]["position"] = np.array([rand.randint(-100,100)/100, rand.randint(-100,100)/100])
        innit_conditions[i]["velocity"] = np.array([rand.randint(-100,100)/100, rand.randint(-100,100)/100])
        innit_conditions[i]["mass"] = 1.0

    # Make sure that the overall momentum is zero
    innit_conditions[n]["i"] = n+1
    innit_conditions[n]["position"] = np.array([rand.randint(-100,100)/100, rand.randint(-100,100)/100])
    #find total momentum
    momentum = np.array([0.0,0.0])         
    for i in range(n):
        momentum += innit_conditions[i]["velocity"]
    #write momentum of correction particle 
    innit_conditions[n]["velocity"] = - momentum
    innit_conditions[n]["mass"] = 1.0
    
    return innit_conditions


def gravity(state, particle, time_step, G = 1):
    dimensions = len(particle["position"])
    force = np.array([float(0)] * dimensions)
    for j in [n for n in state if n["i"] != particle["i"]]:
        #find Distance
        d = particle["position"] - j["position"]
        d = np.linalg.norm(d)

        #find force
        force += -(particle["position"] - j["position"]) * ((G * particle["mass"] * j["mass"]) / d ** 3)
    acceleration = force * 1/particle["mass"]
    return acceleration


def simulation(iterations = 100 , total_time = 5, innit_conditions = innit_random(), acceleration_calculation = gravity):

    time_step = total_time/iterations
    state = innit_conditions
    dimensions = len(state[0]["position"])
    time = 0
    time_states = []
    
    for j in range(iterations):
        time += time_step
        for i in range(len(state)):
            #Find k_1
            particle = state[i]
            k_1 = acceleration_calculation(state, particle, 0)

            # Find k_2
            particle = state[i]
            particle["velocity"] += time_step / 6 * k_1
            particle["position"] += particle["velocity"] * (time_step / 2)
            k_2 = acceleration_calculation(state, particle, time_step/2)

            # Find k_4
            particle = state[i]
            k_4_temp = acceleration_calculation(state, particle, time_step)
            particle["velocity"] += k_4_temp * time_step
            particle["position"] += particle["velocity"] * time_step
            k_4 = acceleration_calculation(state, particle, time_step)

            #Find k_3
            particle["velocity"] += k_4 * time_step
            particle["position"] -= particle["velocity"] * (time_step / 2)
            k_3 = acceleration_calculation(state, particle, -time_step/2)
                                           
            # Evaluate the velocity and position ofor the next time step.
            state[i]["velocity"] += time_step / 6 * sum([k_1, k_2, k_2, k_3, k_3, k_4])
            state[i]["position"] += state[i]["velocity"] * time_step
            
            #print("position: " + str(state[i]["position"]) + "\n velocity " + str(state[i]["velocity"]))

        state_copy = copy.deepcopy(state)
        time_states.append(state_copy)
    return time_states



def print_sim(time_states, window_size = 1024, scale_factor = 50):
    window = gr.GraphWin("Simulation", window_size, window_size)
    
    for t in time_states:

        for i in t:
            #print("position: " + str(i["position"]) + "\n velocity " + str(i["velocity"]))
            p = gr.Point(int(i["position"][0]*scale_factor+window_size/2), int(i["position"][1]*scale_factor+window_size/2))
            c = gr.Circle(p, 1)
            c.draw(window)


    window.getMouse()
    window.close()
        
     
            
            
