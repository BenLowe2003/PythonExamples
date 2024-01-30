
import numpy as np
import graphics as gr
import copy
import random as rand

innit_conditions = [ {"i" : 0, "position" : np.array([0.0,1.0]), "velocity" : np.array([1, 0.5]), "mass" : 1.0},
                     {"i" : 1, "position" : np.array([0.0,-1.0]), "velocity" : np.array([-1.5, 0.5]), "mass" : 1.0},
                     {"i" : 2, "position" : np.array([1.0,0.0]), "velocity" : np.array([0.5, -0.1]), "mass" : 1.0},]
#fix
def innit_random(n):
    innit_conditions = [{"i" : None, "position" : np.array([None,None]), "velocity" : np.array([None, None]), "mass" : None} for i in range(n)] 
    for i in range(n):
        innit_conditions[i]["i"] = i
        innit_conditions[i]["position"] = np.array([rand.randint(-100,100)/100, rand.randint(-100,100)/100])
        innit_conditions[i]["velocity"] = np.array([rand.randint(-100,100)/100, rand.randint(-100,100)/100])
        innit_conditions[i]["mass"] = 1.0
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


def simulation(iterations = 10000 , total_time = 20, innit_conditions = innit_conditions, acceleration_calculation = gravity):

    time_step = total_time/iterations
    state = innit_conditions
    dimensions = len(state[0]["position"])
    time = 0
    time_states = []
    
    for j in range(iterations):
        time += time_step
        for i in range(len(state)):
            particle = state[i]
            k_1 = acceleration_calculation(state, particle, 0)
            factor = np.array([time_step / 2] * dimensions)
            particle["velocity"] = state[i]["velocity"] + k_1 * factor
            k_2 = acceleration_calculation(state, particle, time_step/2)
            particle["velocity"] = state[i]["velocity"] + k_2 * factor
            k_3 = acceleration_calculation(state, particle, time_step/2)
            factor = np.array([time_step] * dimensions)
            particle["velocity"] = state[i]["velocity"] + k_3 * factor
            k_4 = acceleration_calculation(state, particle, time_step)

            state[i]["velocity"] += time_step / 6 * sum([k_1, k_2, k_2, k_3, k_3, k_4])
            state[i]["position"] += state[i]["velocity"] * time_step
            
            #print("position: " + str(state[i]["position"]) + "\n velocity " + str(state[i]["velocity"]))

        state_copy = copy.deepcopy(state)
        time_states.append(state_copy)
    return time_states



def print_sim(time_states, window_size = 1024):
    window = gr.GraphWin("Simulation", window_size, window_size)
    
    for t in time_states:

        for i in t:
            #print("position: " + str(i["position"]) + "\n velocity " + str(i["velocity"]))
            p = gr.Point(int(i["position"][0]*100+window_size/2), int(i["position"][1]*+window_size/2))
            c = gr.Circle(p, 1, color = [255,255,255])
            c.draw(window)

    window.getMouse()
    window.close()
        









    
        
            
            
